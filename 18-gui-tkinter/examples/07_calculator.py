"""
Demonstrates a simple calculator: a StringVar display and a grid of
buttons created in a loop. It handles one operation at a time, such as
12+3 or 7/2, and shows an error dialog for division by zero.
Run: python 07_calculator.py   (click the keys or type: digits, + - * /, Enter, Escape)
"""

import operator
import tkinter as tk
from tkinter import messagebox

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def press(key):
    """Append a digit or operator to the display."""
    display.set(display.get() + key)


def clear(event=None):
    display.set("")


def calculate(event=None):
    """Split the display at its operator and show the answer."""
    expression = display.get()
    try:
        for symbol, operation in OPERATIONS.items():
            if symbol in expression:
                left, right = expression.split(symbol)
                answer = operation(float(left), float(right))
                break
        else:
            answer = float(expression)      # no operator: just a number
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear()
        return
    except ValueError:
        messagebox.showerror("Error", "Enter a sum like 12+3.")
        clear()
        return

    if answer == int(answer):           # show 6, not 6.0, but keep 3.5
        display.set(str(int(answer)))
    else:
        display.set(str(round(answer, 6)))


window = tk.Tk()
window.title("Calculator")

display = tk.StringVar()
tk.Entry(window, textvariable=display, justify="right", font=("Arial", 16),
         width=16, state="readonly").grid(row=0, column=0, columnspan=4, padx=5, pady=5)

keys = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]
for row_index, row in enumerate(keys, start=1):
    for column_index, key in enumerate(row):
        if key == "=":
            action = calculate
        else:
            # k=key freezes the current key for this button only.
            action = lambda k=key: press(k)
        tk.Button(window, text=key, width=5, height=2, command=action).grid(
            row=row_index, column=column_index, padx=2, pady=2)

tk.Button(window, text="C", width=24, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

for character in "0123456789.+-*/":     # keyboard support
    window.bind(character, lambda event, k=character: press(k))
window.bind("<Return>", calculate)
window.bind("<Escape>", clear)

window.mainloop()
