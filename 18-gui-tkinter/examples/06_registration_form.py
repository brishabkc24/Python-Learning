"""
Demonstrates a registration form built from several widgets: Entry,
ttk.Combobox, Radiobutton, Checkbutton, Scale and a read-only Text
widget that shows a summary after the Register button is clicked.
Run: python 06_registration_form.py
Fill in the form and click Register. Leaving the name empty or typing an
email without @ opens an error dialog instead of a summary.
"""

import tkinter as tk
from tkinter import ttk, messagebox


def register():
    """Validate the form, then write a summary into the Text widget."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    if name == "" or "@" not in email:
        messagebox.showerror("Missing data", "Please enter a name and a valid email.")
        return

    lines = [
        f"Name: {name}",
        f"Email: {email}",
        f"Course: {course.get()}",
        f"Level: {level.get()}",
        f"Hours per week: {hours.get()}",
        f"Newsletter: {'yes' if newsletter.get() else 'no'}",
    ]
    # A disabled Text widget cannot be edited, so enable it just long
    # enough to replace its contents.
    summary.config(state="normal")
    summary.delete("1.0", "end")
    summary.insert("1.0", "\n".join(lines))
    summary.config(state="disabled")


window = tk.Tk()
window.title("Registration")

tk.Label(window, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
name_entry = tk.Entry(window, width=28)
name_entry.grid(row=0, column=1, padx=5, pady=3)

tk.Label(window, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
email_entry = tk.Entry(window, width=28)
email_entry.grid(row=1, column=1, padx=5, pady=3)

tk.Label(window, text="Course:").grid(row=2, column=0, sticky="e", padx=5, pady=3)
course = tk.StringVar(value="Python")
ttk.Combobox(window, textvariable=course, values=["Python", "Java", "C"],
             state="readonly", width=25).grid(row=2, column=1, padx=5, pady=3)

tk.Label(window, text="Level:").grid(row=3, column=0, sticky="ne", padx=5, pady=3)
level = tk.StringVar(value="Beginner")
level_frame = tk.Frame(window)           # the radio buttons use pack inside this frame
level_frame.grid(row=3, column=1, sticky="w")
for option in ("Beginner", "Intermediate", "Advanced"):
    tk.Radiobutton(level_frame, text=option, variable=level, value=option).pack(anchor="w")

tk.Label(window, text="Hours per week:").grid(row=4, column=0, sticky="e", padx=5, pady=3)
hours = tk.IntVar(value=5)
tk.Scale(window, from_=1, to=20, orient="horizontal", variable=hours).grid(row=4, column=1, sticky="we", padx=5)

newsletter = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Send me the newsletter", variable=newsletter).grid(row=5, column=1, sticky="w", padx=5)

tk.Button(window, text="Register", width=12, command=register).grid(row=6, column=0, columnspan=2, pady=8)

summary = tk.Text(window, width=40, height=7, state="disabled")
summary.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
