"""
Demonstrates events (command= and bind) together with the control
variables StringVar, IntVar and BooleanVar.
Run: python 03_events_and_variables.py
A window opens. Clicking, pressing keys, ticking the box, choosing a
colour or moving the slider prints a line in the terminal, for example:
    Key pressed: a
    Mouse clicked at x=57 y=22
    Checkbutton is now: True
"""

import tkinter as tk


def on_button():
    print("Button clicked")


def on_key(event):
    # event.keysym is the name of the key, such as "a", "Return" or "space".
    print("Key pressed:", event.keysym)


def on_click(event):
    # event.x and event.y are measured from the top-left corner of the widget.
    print(f"Mouse clicked at x={event.x} y={event.y}")


def on_check():
    print("Checkbutton is now:", agreed.get())


def on_colour():
    print("Colour chosen:", colour.get())


def on_slide(value):
    # Scale passes the new value as a string.
    print("Slider moved to:", value)


window = tk.Tk()
window.title("Events and variables")

tk.Button(window, text="Click me", command=on_button).pack(pady=5)

area = tk.Label(window, text="Click inside this box or press a key",
                bg="lightyellow", width=40, height=4)
area.pack(padx=10, pady=5)
area.bind("<Button-1>", on_click)
window.bind("<Key>", on_key)

# Control variables must be created after tk.Tk().
agreed = tk.BooleanVar(value=False)
tk.Checkbutton(window, text="I agree", variable=agreed, command=on_check).pack(anchor="w", padx=10)

colour = tk.StringVar(value="red")
for name in ("red", "green", "blue"):
    tk.Radiobutton(window, text=name, variable=colour, value=name,
                   command=on_colour).pack(anchor="w", padx=10)

volume = tk.IntVar(value=50)
tk.Scale(window, from_=0, to=100, orient="horizontal", variable=volume,
         label="Volume", command=on_slide).pack(fill="x", padx=10, pady=5)

window.mainloop()
