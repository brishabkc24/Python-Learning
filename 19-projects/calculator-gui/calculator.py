"""
Calculator (Tkinter)
====================
A desktop calculator with a grid of buttons. It works one operation at
a time (for example 12+3, 7/2, 6*7). Division by zero and incomplete
sums show an error dialog instead of crashing. The keyboard works too:
digits, + - * /, Enter for =, Backspace, and Escape to clear.

Run: python calculator.py
"""

import operator
import tkinter as tk
from tkinter import messagebox

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

# Button labels in the order they appear on screen, row by row.
KEY_ROWS = [
    ["C", "<-", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."],
]


class Calculator(tk.Tk):
    """The main window. Everything the calculator needs is stored on self."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        self.display = tk.StringVar()
        self.history = tk.StringVar(value="")
        self.build_widgets()
        self.bind_keyboard()

    def build_widgets(self):
        tk.Label(self, textvariable=self.history, anchor="e", fg="grey").grid(
            row=0, column=0, columnspan=4, sticky="we", padx=6)
        tk.Entry(self, textvariable=self.display, justify="right", font=("Arial", 18),
                 state="readonly", width=16).grid(row=1, column=0, columnspan=4, padx=6, pady=(0, 6))

        for row_index, row in enumerate(KEY_ROWS, start=2):
            for column_index, key in enumerate(row):
                button = tk.Button(self, text=key, width=5, height=2,
                                   command=lambda k=key: self.press(k))
                # "0" is a double-width key, "=" is a double-height key.
                if key == "0":
                    button.config(width=12)
                    button.grid(row=row_index, column=0, columnspan=2, padx=2, pady=2)
                elif key == "=":
                    button.config(height=5)
                    button.grid(row=row_index, column=3, rowspan=2, padx=2, pady=2)
                else:
                    button.grid(row=row_index, column=column_index, padx=2, pady=2)

    def bind_keyboard(self):
        for character in "0123456789.+-*/":
            self.bind(character, lambda event, k=character: self.press(k))
        self.bind("<Return>", lambda event: self.press("="))
        self.bind("<BackSpace>", lambda event: self.press("<-"))
        self.bind("<Escape>", lambda event: self.press("C"))

    def press(self, key):
        """Handle every button and keyboard key in one place."""
        if key == "C":
            self.display.set("")
            self.history.set("")
        elif key == "<-":
            self.display.set(self.display.get()[:-1])
        elif key == "=":
            self.calculate()
        else:
            self.display.set(self.display.get() + key)

    def calculate(self):
        expression = self.display.get()
        try:
            answer = evaluate(expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
            self.display.set("")
            return
        except ValueError:
            messagebox.showerror("Error", "Enter a complete sum such as 12+3.")
            return
        self.history.set(f"{expression} =")
        self.display.set(format_number(answer))


def evaluate(expression):
    """Compute 'number operator number'. Raise ValueError for anything else."""
    for symbol, operation in OPERATIONS.items():
        if symbol in expression:
            left, right = expression.split(symbol, 1)
            return operation(float(left), float(right))
    return float(expression)          # a plain number evaluates to itself


def format_number(number):
    """Show 15.0 as 15 but keep 3.5 as 3.5."""
    if number == int(number):
        return str(int(number))
    return str(round(number, 8))


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
