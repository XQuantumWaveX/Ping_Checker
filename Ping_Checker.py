import argparse
import requests
import time
import random
import sys
from itertools import product

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# Parameters
SPEEDS = ["slow", "fast", "variable"]
GROWTHS = ["slow", "rapid"]
SIZES = ["bigger", "same"]
STACKINGS = ["no", "yes"]
DELAYS = ["none", "fixed", "dynamic"]

# Generate all 72 combinations
TEST_TYPES = {}
num = 1
for speed, growth, size, stack, delay in product(SPEEDS, GROWTHS, SIZES, STACKINGS, DELAYS):
    TEST_TYPES[num] = {
        "speed": speed,
        "growth": growth,
        "size_change": size,
        "stacking": stack,
        "delay": delay
    }
    num += 1

# Color helpers
def color_speed(speed):
    return Colors.GREEN if speed == "fast" else Colors.RED if speed == "slow" else Colors.YELLOW

def color_growth(growth):
    return Colors.CYAN if growth == "rapid" else Colors.MAGENTA

def color_size(size_change):
    return Colors.BLUE if size_change == "bigger" else Colors.WHITE

def color_delay(delay):
    return Colors.CYAN if delay=="dynamic" else Colors.MAGENTA if delay=="fixed" else Colors.WHITE

# Interactive test runner
def interactive_test(url, max_requests, config):
    print(f"\n=== Running Test ===")
    print(f"Speed: {color_speed(config['speed'])}{config['speed']}{Colors.RESET}, "
          f"Growth Rate: {color_growth(config['growth'])}{config['growth']}{Colors.RESET}, "
          f"Size Change: {color_size(config['size_change'])}{config['size_change']}{Colors.RESET}, "
          f"Stacking: {config['stacking']}, Delay: {color_delay(config['delay'])}{config['delay']}{Colors.RESET}\n")

    base_size = 100
    size = base_size
    pings_received = 0
    current_delay = 0.5

    for count in range(1, max_requests + 1):
        stack = random.randint(1,10) if config["stacking"] == "yes" else 1

        if config["size_change"] == "bigger":
            growth_factor = 1.05 if config["growth"] == "slow" else 1.2
            size = int(size * growth_factor)

        if config["speed"] == "slow":
            current_delay = max(current_delay, 0.2)
        elif config["speed"] == "fast":
            current_delay = max(current_delay*0.95, 0.01)
        else:  # variable
            current_delay = random.uniform(0.01, 0.5)

        delay_time = 0 if config["delay"]=="none" else 0.5 if config["delay"]=="fixed" else current_delay

        for s in range(stack):
            try:
                start_time = time.time()
                response = requests.get(url, timeout=5)
                elapsed = time.time() - start_time

                if response.status_code >= 400:
                    print(f"\n{Colors.RED}Pings denied on Ping {count} with size {size}B (HTTP {response.status_code}){Colors.RESET}")
                    return

                pings_received += 1
                print(f"Ping {count}-{s+1}: status={response.status_code}, time={elapsed:.3f}s, "
                      f"size={color_size(config['size_change'])}{size}B{Colors.RESET}, "
                      f"Speed: {color_speed(config['speed'])}{config['speed']}{Colors.RESET}, "
                      f"Pings received: {pings_received}   ", end="\r")
                sys.stdout.flush()

            except requests.exceptions.RequestException:
                print(f"\n{Colors.RED}Pings denied on Ping {count} with size {size}B (request failed){Colors.RESET}")
                return

        time.sleep(delay_time)

    print(f"\n\nTest finished. Total Pings received: {pings_received}")

# Match easy mode selections to a test type
def find_test_type(speed, growth, size, stacking, delay):
    for key, val in TEST_TYPES.items():
        if val['speed']==speed and val['growth']==growth and val['size_change']==size and val['stacking']==stacking and val['delay']==delay:
            return val
    return None

def main():
    # Choose mode
    mode = ""
    while mode.lower() not in ["easy","advanced"]:
        mode = input("Select mode (easy / advanced): ").strip().lower()

    parser = argparse.ArgumentParser(description="HTTP ping test.")
    parser.add_argument("--url", required=True, help="URL to test")
    parser.add_argument("--max_requests", type=int, required=True, help="Number of requests")
    args = parser.parse_args()

    if mode=="advanced":
        print("Select a test type (1-72):")
        print("+-----+----------+--------+-------------+----------+---------+")
        print("| Num | Speed    | Growth | Size Change | Stacking | Delay   |")
        print("+-----+----------+--------+-------------+----------+---------+")
        for i in range(1,len(TEST_TYPES)+1):
            t = TEST_TYPES[i]
            print(f"| {i:<3} | {t['speed']:<8} | {t['growth']:<6} | {t['size_change']:<11} | {t['stacking']:<8} | {t['delay']:<7} |")
        print("+-----+----------+--------+-------------+----------+---------+")

        test_type = 0
        while test_type not in range(1,len(TEST_TYPES)+1):
            try:
                test_type = int(input(f"Enter test type number (1-{len(TEST_TYPES)}): "))
            except ValueError:
                pass

        config = TEST_TYPES[test_type]

    else:  # easy mode
        print("Easy Mode: Answer the following prompts")
        # Prompt interactive selections
        def choose_option(prompt, options):
            choice = ""
            while choice.lower() not in options:
                choice = input(f"{prompt} (Options: {', '.join(options)}): ").strip().lower()
            return choice

        speed = choose_option("Choose Speed", SPEEDS)
        growth = choose_option("Choose Growth", GROWTHS)
        size = choose_option("Choose Size Change", SIZES)
        stacking = choose_option("Choose Stacking", STACKINGS)
        delay = choose_option("Choose Delay", DELAYS)

        config = find_test_type(speed, growth, size, stacking, delay)
        if config is None:
            print("Invalid combination, using default first test type")
            config = TEST_TYPES[1]

    interactive_test(args.url, args.max_requests, config)

if __name__ == "__main__":
    main()
