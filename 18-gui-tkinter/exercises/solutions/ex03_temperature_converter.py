"""Exercise 3: convert Celsius from an Entry to Fahrenheit, with an error message for bad input."""

import tkinter as tk


def convert(event=None):
    text = celsius_entry.get().strip()
    try:
        celsius = float(text)
    except ValueError:
        result.config(text="Please enter a number", fg="red")
        return
    fahrenheit = celsius * 9 / 5 + 32
    result.config(text=f"{fahrenheit:.1f} F", fg="black")


window = tk.Tk()
window.title("Temperature converter")

tk.Label(window, text="Celsius:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
celsius_entry = tk.Entry(window, width=15)
celsius_entry.grid(row=0, column=1, padx=5, pady=5)
celsius_entry.focus()
celsius_entry.bind("<Return>", convert)

tk.Button(window, text="Convert", command=convert).grid(row=1, column=0, columnspan=2, pady=5)

result = tk.Label(window, text="", font=("Arial", 12))
result.grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
