
# Live Barcode Debugger

This project provides a Python script that monitors keyboard input in real time and interprets it as barcode scans. It is useful for debugging barcode scanners that act as keyboards.

## Features

- Displays every keystroke instantly in the terminal
- Detects continuous scans using a time window
- Marks new scan sequences
- Exits the program with the `Esc` key

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/) library

## Installation

Install the required library with pip:

```
pip install pynput
```

## Usage

Start the script in the terminal:

```
python scanner_test.py
```

Follow the instructions in the terminal. Every keystroke is displayed live. Press `Esc` to exit the program.

## Notes

- The script is suitable for macOS and other desktop operating systems.
- Barcode scanners recognized as keyboards can be tested directly.

## License

This project is licensed under the MIT License.
