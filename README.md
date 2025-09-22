# Ping_Checker
A tool to check when an website denys an request.

A Python-based interactive **HTTP ping tester** that simulates different
network conditions by varying speed, growth, size, stacking, and delay.\
The tool can run in **easy mode** (guided prompts) or **advanced mode**
(full 72 pre-defined test types).

------------------------------------------------------------------------

## Features

-   **Interactive Test Runner**\
    Runs HTTP pings against a given URL with configurable parameters.

-   **Two Modes**

    -   **Easy Mode** → Guided prompts to select speed, growth, size
        change, stacking, and delay.\
    -   **Advanced Mode** → Choose from 72 pre-configured test types.

-   **Color-Coded Output**\
    ANSI colors highlight important metrics such as speed, growth, size,
    and delay.

-   **Real-Time Feedback**\
    Prints ping responses, elapsed time, packet sizes, and progress
    updates live.

-   **Failure Handling**\
    Stops when requests fail or are denied.

------------------------------------------------------------------------

## Parameters

The tool varies the following test attributes:

  ------------------------------------------------------------------------
  Parameter      Options                                    Description
  -------------- ------------------------------------------ --------------
  **Speed**      `slow`, `fast`, `variable`                 Adjusts ping
                                                            frequency

  **Growth**     `slow`, `rapid`                            Controls
                                                            payload growth

  **Size**       `bigger`, `same`                           Payload size
                                                            changes

  **Stacking**   `yes`, `no`                                Sends multiple
                                                            stacked pings
                                                            per iteration (IN TESTING)

  **Delay**      `none`, `fixed`, `dynamic`                 Adds
                                                            artificial
                                                            delay between
                                                            requests
  ------------------------------------------------------------------------

This results in **72 unique test types**.

------------------------------------------------------------------------

## Installation

Clone this repository and install dependencies:

``` bash
git clone https://github.com/XQuantumWaveX/Ping_Checker/
cd Ping_Checker
pip install requests
```

------------------------------------------------------------------------

## Usage

### Run the tool

``` bash
python Ping_Test.py --url https://example.com --max_requests 50
```

You will be prompted to select **easy mode** or **advanced mode**.

------------------------------------------------------------------------

### Easy Mode

Guided selection of parameters:

    Select mode (easy / advanced): easy
    Choose Speed (Options: slow, fast, variable): fast
    Choose Growth (Options: slow, rapid): rapid
    Choose Size Change (Options: bigger, same): bigger
    Choose Stacking (Options: no, yes): yes
    Choose Delay (Options: none, fixed, dynamic): dynamic

------------------------------------------------------------------------

### Advanced Mode

Lists all 72 predefined test types in a table. Example:

    Select mode (easy / advanced): advanced
    Select a test type (1-72):
    +-----+----------+--------+-------------+----------+---------+
    | Num | Speed    | Growth | Size Change | Stacking | Delay   |
    +-----+----------+--------+-------------+----------+---------+
    | 1   | slow     | slow   | bigger      | no       | none    |
    | 2   | slow     | slow   | bigger      | no       | fixed   |
    ...
    Enter test type number (1-72): 15

------------------------------------------------------------------------

## Example Output

    === Running Test ===
    Speed: fast, Growth Rate: rapid, Size Change: bigger, Stacking: yes, Delay: dynamic

    Ping 3-2: status=200, time=0.045s, size=144B, Speed: fast, Pings received: 10

------------------------------------------------------------------------

## Notes

-   Best used against test or staging environments.
-   May generate **high request loads** depending on settings.
-   Not recommended for use against production systems without
    permission.
-   SCRIPT OUTPUT DEPENDS ON NETWORK SPEED AND CPU SPEED

    I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS SCRIPT. PEOPLE WHO USE THIS SCRIPT NEED TO BE AWARE OF THEIR ACTIONS.

------------------------------------------------------------------------





TO ADD:

- An option to stay between different Byte Sizes if you want to know the EXACT Byte
