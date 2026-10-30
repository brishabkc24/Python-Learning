"""Exercise 1: a label 'Clicks: 0' and a button that increases the count on every click."""

import tkinter as tk

clicks = 0


def count_click():
    global clicks
    clicks += 1
    counter_label.config(text=f"Clicks: {clicks}")


window = tk.Tk()
window.title("Click counter")
window.geometry("250x120")

counter_label = tk.Label(window, text="Clicks: 0", font=("Arial", 14))
counter_label.pack(pady=15)

tk.Button(window, text="Click", width=10, command=count_click).pack()

window.mainloop()
