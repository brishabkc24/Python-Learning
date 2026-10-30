"""
Demonstrates a to-do list built on a Listbox: add a task from an Entry,
remove the selected task, clear the list, and keep a live count.
Run: python 08_todo_list.py
Type a task and press Enter or click Add. Click a task and then
"Remove selected" to delete it. The label at the bottom shows the count.
"""

import tkinter as tk
from tkinter import messagebox


def update_count():
    count_label.config(text=f"{tasks.size()} task(s)")


def add_task(event=None):
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Empty task", "Type a task first.")
        return
    tasks.insert("end", task)         # "end" means after the last line
    task_entry.delete(0, "end")
    update_count()


def remove_task():
    selected = tasks.curselection()   # a tuple of selected indexes
    if not selected:
        messagebox.showwarning("Nothing selected", "Click a task to remove it.")
        return
    tasks.delete(selected[0])
    update_count()


def clear_tasks():
    if tasks.size() == 0:
        return
    if messagebox.askyesno("Clear all", "Remove every task?"):
        tasks.delete(0, "end")
        update_count()


window = tk.Tk()
window.title("To-do list")

task_entry = tk.Entry(window, width=30)
task_entry.grid(row=0, column=0, padx=5, pady=5)
task_entry.bind("<Return>", add_task)
task_entry.focus()
tk.Button(window, text="Add", width=12, command=add_task).grid(row=0, column=1, padx=5)

tasks = tk.Listbox(window, width=40, height=8)
tasks.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# A few starting tasks so the list is not empty.
for starting_task in ("Read the Tkinter lesson", "Run the examples", "Do the exercises"):
    tasks.insert("end", starting_task)

tk.Button(window, text="Remove selected", command=remove_task).grid(row=2, column=0, pady=5)
tk.Button(window, text="Clear all", command=clear_tasks).grid(row=2, column=1, pady=5)

count_label = tk.Label(window, text="")
count_label.grid(row=3, column=0, columnspan=2, pady=5)
update_count()

window.mainloop()
