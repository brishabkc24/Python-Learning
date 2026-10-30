"""Exercise 7: Uppercase, Lowercase and Clear buttons for a Text widget, with a character count."""

import tkinter as tk


def current_text():
    # "end-1c" leaves out the newline that Tkinter adds after the last line.
    return text_box.get("1.0", "end-1c")


def replace_text(new_text):
    text_box.delete("1.0", "end")
    text_box.insert("1.0", new_text)
    update_count()


def update_count():
    count_label.config(text=f"Characters: {len(current_text())}")


def make_upper():
    replace_text(current_text().upper())


def make_lower():
    replace_text(current_text().lower())


def clear_text():
    replace_text("")


window = tk.Tk()
window.title("Text tools")

text_box = tk.Text(window, width=40, height=8)
text_box.insert("1.0", "Hello World")
text_box.pack(padx=10, pady=10)

buttons = tk.Frame(window)
buttons.pack()
tk.Button(buttons, text="Uppercase", width=10, command=make_upper).pack(side="left", padx=5)
tk.Button(buttons, text="Lowercase", width=10, command=make_lower).pack(side="left", padx=5)
tk.Button(buttons, text="Clear", width=10, command=clear_text).pack(side="left", padx=5)

count_label = tk.Label(window, text="")
count_label.pack(pady=10)
update_count()

window.mainloop()
