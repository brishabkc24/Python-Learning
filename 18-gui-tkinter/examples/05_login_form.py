"""
Demonstrates a login form: two Entry boxes (the password one hidden with
show="*"), a check against placeholder values, and a result label that
turns green on success and red on failure.
Run: python 05_login_form.py
The accepted username is admin and the password is password123.
"""

import tkinter as tk
from tkinter import messagebox

# Placeholder values. A real program would look these up in a database.
USERNAME = "admin"
PASSWORD = "password123"
MAX_ATTEMPTS = 3

failed_attempts = 0


def check_login(event=None):
    """Compare the typed values with the placeholders and colour the result."""
    global failed_attempts
    username = username_entry.get().strip()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        result.config(text="Login successful", fg="green")
        return

    failed_attempts += 1
    result.config(text="Wrong username or password", fg="red")
    password_entry.delete(0, "end")      # make the user retype the password
    if failed_attempts >= MAX_ATTEMPTS:
        messagebox.showerror("Locked", "Too many failed attempts.")
        window.destroy()


window = tk.Tk()
window.title("Login")

tk.Label(window, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(window, width=25)
username_entry.grid(row=0, column=1, padx=5, pady=5)
username_entry.focus()

tk.Label(window, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(window, width=25, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)
password_entry.bind("<Return>", check_login)

tk.Button(window, text="Login", width=10, command=check_login).grid(row=2, column=0, columnspan=2, pady=5)

result = tk.Label(window, text="")
result.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
