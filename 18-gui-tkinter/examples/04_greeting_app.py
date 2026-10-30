"""
Demonstrates reading an Entry with get(), clearing it with delete(), and
reading a multi-line Text widget with get("1.0", "end").
Run: python 04_greeting_app.py
A window opens. Type a name and press Enter or click Greet to see a
greeting. Type a note in the big box and click Count words.
"""

import tkinter as tk


def greet(event=None):
    """Read the name box and show a greeting. event is unused but bind() passes it."""
    name = name_entry.get().strip()
    if name == "":
        greeting.config(text="Please type your name.", fg="red")
    else:
        greeting.config(text=f"Hello, {name}! Welcome.", fg="blue")


def clear_name():
    name_entry.delete(0, "end")
    greeting.config(text="")
    name_entry.focus()


def count_words():
    # "1.0" is line 1, column 0; "end" is just after the last character.
    content = notes.get("1.0", "end")
    word_count = len(content.split())
    notes_result.config(text=f"Words: {word_count}")


window = tk.Tk()
window.title("Greeting app")

tk.Label(window, text="Your name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.focus()                       # put the cursor in the box
name_entry.bind("<Return>", greet)       # Enter works like the button

tk.Button(window, text="Greet", width=8, command=greet).grid(row=1, column=0, pady=5)
tk.Button(window, text="Clear", width=8, command=clear_name).grid(row=1, column=1, pady=5, sticky="w")

greeting = tk.Label(window, text="")
greeting.grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(window, text="Notes:").grid(row=3, column=0, padx=5, sticky="ne")
notes = tk.Text(window, width=30, height=5)
notes.insert("1.0", "Python is easy to learn.\nTkinter makes windows.")
notes.grid(row=3, column=1, padx=5, pady=5)

tk.Button(window, text="Count words", command=count_words).grid(row=4, column=1, sticky="w", padx=5)
notes_result = tk.Label(window, text="Words: ?")
notes_result.grid(row=5, column=1, sticky="w", padx=5, pady=5)

window.mainloop()
