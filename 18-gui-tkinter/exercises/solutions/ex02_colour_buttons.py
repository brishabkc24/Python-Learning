"""Exercise 2: three buttons that change the background colour of a label."""

import tkinter as tk


def set_colour(colour):
    colour_label.config(bg=colour, text=f"You picked {colour}")


window = tk.Tk()
window.title("Colour buttons")

colour_label = tk.Label(window, text="Pick a colour", width=30, height=4, bg="white")
colour_label.pack(padx=10, pady=10)

button_row = tk.Frame(window)
button_row.pack(pady=5)
for colour in ("red", "green", "blue"):
    # c=colour stores this loop's colour inside the lambda.
    tk.Button(button_row, text=colour.capitalize(), width=8,
              command=lambda c=colour: set_colour(c)).pack(side="left", padx=5)

window.mainloop()
