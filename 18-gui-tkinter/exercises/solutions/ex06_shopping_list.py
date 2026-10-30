"""Exercise 6: a shopping list with add, remove selected, and a live item count."""

import tkinter as tk
from tkinter import messagebox


def update_count():
    count_label.config(text=f"{items.size()} item(s)")


def add_item(event=None):
    item = item_entry.get().strip()
    if item == "":
        return
    items.insert("end", item)
    item_entry.delete(0, "end")
    update_count()


def remove_item():
    selected = items.curselection()
    if not selected:
        messagebox.showwarning("Nothing selected", "Click an item first.")
        return
    items.delete(selected[0])
    update_count()


window = tk.Tk()
window.title("Shopping list")

item_entry = tk.Entry(window, width=28)
item_entry.grid(row=0, column=0, padx=5, pady=5)
item_entry.bind("<Return>", add_item)
item_entry.focus()
tk.Button(window, text="Add", width=14, command=add_item).grid(row=0, column=1, padx=5)

items = tk.Listbox(window, width=40, height=8)
items.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

tk.Button(window, text="Remove selected", command=remove_item).grid(row=2, column=0, columnspan=2, pady=5)

count_label = tk.Label(window, text="")
count_label.grid(row=3, column=0, columnspan=2, pady=(0, 5))
update_count()

window.mainloop()
