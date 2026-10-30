"""Exercise 5: a feedback form whose Submit button shows the answers in a dialog."""

import tkinter as tk
from tkinter import messagebox


def submit():
    name = name_entry.get().strip()
    if name == "":
        messagebox.showerror("Missing name", "Please enter your name.")
        return
    summary = (
        f"Name: {name}\n"
        f"Rating: {rating.get()} out of 5\n"
        f"Recommend: {recommend.get()}\n"
        f"Contact me: {'yes' if contact.get() else 'no'}"
    )
    messagebox.showinfo("Thank you", summary)


window = tk.Tk()
window.title("Feedback form")

tk.Label(window, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.focus()

tk.Label(window, text="Rating:").grid(row=1, column=0, sticky="e", padx=5)
rating = tk.IntVar(value=3)
tk.Scale(window, from_=1, to=5, orient="horizontal", variable=rating).grid(row=1, column=1, sticky="we", padx=5)

tk.Label(window, text="Would you recommend us?").grid(row=2, column=0, columnspan=2, pady=(10, 0))
recommend = tk.StringVar(value="Yes")
choices = tk.Frame(window)
choices.grid(row=3, column=0, columnspan=2)
for answer in ("Yes", "No"):
    tk.Radiobutton(choices, text=answer, variable=recommend, value=answer).pack(side="left", padx=10)

contact = tk.BooleanVar(value=False)
tk.Checkbutton(window, text="Contact me", variable=contact).grid(row=4, column=0, columnspan=2, pady=5)

tk.Button(window, text="Submit", width=12, command=submit).grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
