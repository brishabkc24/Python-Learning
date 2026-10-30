"""
Demonstrates the smallest useful Tkinter program: a window with a title
and a size, a label, and a button that changes the label when clicked.
Run: python 01_first_window.py
A window opens. Each click on the button updates the message and the
click count. Close the window to end the program.
"""

import tkinter as tk

click_count = 0


def change_text():
    """Update the label every time the button is clicked."""
    global click_count
    click_count += 1
    message.config(text=f"You clicked the button {click_count} time(s)!")


# The main window must exist before any widget or variable is created.
window = tk.Tk()
window.title("My first window")
window.geometry("320x140")

message = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
message.pack(pady=15)

# command= takes the function name WITHOUT parentheses.
tk.Button(window, text="Click me", command=change_text).pack()

# mainloop() keeps the window open and waits for clicks.
window.mainloop()

# This line runs only after the window has been closed.
print("The window was closed after", click_count, "click(s).")
