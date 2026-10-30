"""Exercise 4: show the last key pressed and where the mouse was clicked inside a box."""

import tkinter as tk


def on_key(event):
    key_label.config(text=f"Last key: {event.keysym}")


def on_click(event):
    click_label.config(text=f"Clicked at: {event.x}, {event.y}")


window = tk.Tk()
window.title("Key and mouse watcher")

box = tk.Label(window, text="Click here or press a key", bg="lightblue", width=40, height=6)
box.pack(padx=10, pady=10)
box.bind("<Button-1>", on_click)

# Key presses go to the window, so bind them there.
window.bind("<Key>", on_key)

key_label = tk.Label(window, text="Last key: (none yet)")
key_label.pack(anchor="w", padx=10)
click_label = tk.Label(window, text="Clicked at: (nowhere yet)")
click_label.pack(anchor="w", padx=10, pady=(0, 10))

window.mainloop()
