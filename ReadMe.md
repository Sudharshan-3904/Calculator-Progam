**Calculator Program README**

## Overview
This is a simple calculator program built using the Tkinter library in Python. The program creates a graphical user interface (GUI) where users can input mathematical expressions and view the results.

## Features
- Supports basic arithmetic operations: addition, subtraction, multiplication, division
- Includes buttons for digits 0-9, decimal point, and operators (+, -, \*, /)
- Has an equals button to evaluate the expression and display the result
- Includes a clear button to reset the calculator

## Usage
1. Run the program by executing the Python script.
2. The GUI will appear with a text entry field at the top displaying the current expression.
3. Click on buttons to input digits, operators, and decimal points.
4. Press the equals button to evaluate the expression and display the result.
5. Use the clear button to reset the calculator.

## Code Structure
The code is structured as follows:

- `button_press(num)` function: handles button clicks for digits 0-9 and operators.
- `equals()` function: evaluates the current expression when the equals button is pressed.
- `clear()` function: resets the calculator by clearing the current expression.
- The main program creates a Tkinter window with buttons and labels, sets up event handlers for button clicks.

## Requirements
- Python 3.x (tested on Python 3.8)
- Tkinter library (comes bundled with most Python installations)

## Notes
- This is a basic implementation of a calculator program and does not include advanced features like memory management or scientific notation.
- The program uses the `eval()` function to evaluate mathematical expressions, which can pose security risks if used with untrusted input. However, in this case, the input is limited to digits, operators, and decimal points.

## Future Improvements
- Add support for more advanced mathematical operations (e.g., exponentiation, roots)
- Implement a memory management system
- Enhance user interface with additional features (e.g., buttons for square root, percentage calculation)