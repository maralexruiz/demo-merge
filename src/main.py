#!/usr/bin/env python3
"""
Main application for the demo-merge project.
This is a simple calculator application used to demonstrate Git merge strategies.
"""

from calculator import Calculator
from utils import display_banner, get_user_input


def main():
    """Main entry point for the calculator application."""
    display_banner()

    calc = Calculator()

    print("Simple Calculator")
    print("=" * 50)
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == 'quit':
            print("Goodbye!")
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = get_user_input("Enter first number: ")
            num2 = get_user_input("Enter second number: ")

            if operation == 'add':
                result = calc.add(num1, num2)
            elif operation == 'subtract':
                result = calc.subtract(num1, num2)
            elif operation == 'multiply':
                result = calc.multiply(num1, num2)
            elif operation == 'divide':
                result = calc.divide(num1, num2)

            print(f"Result: {result}")
            print()
        except ValueError as e:
            print(f"Error: {e}")
            print()


if __name__ == "__main__":
    main()
