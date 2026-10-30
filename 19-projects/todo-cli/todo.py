"""
To-Do List (command line)
=========================
A menu-driven task list. Tasks are kept as a list of dictionaries and
saved to todo.json next to this script, so they survive between runs.

Run: python todo.py

Sample session:
    1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
    Choose (1-5): 1
    Task title: Buy milk
    Added task 1: Buy milk
    Choose (1-5): 2
    [ ] 1. Buy milk  (added 2025-01-15)
"""

import json
from datetime import date
from pathlib import Path

# The file lives next to this script no matter where you run it from.
TODO_FILE = Path(__file__).resolve().parent / "todo.json"

MENU = "\n1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit"


def load_tasks():
    """Read the saved list, or start with an empty list if there is none."""
    try:
        with open(TODO_FILE, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {TODO_FILE.name} is damaged. Starting with an empty list.")
        return []


def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if title == "":
        print("The title cannot be empty.")
        return
    task = {"title": title, "done": False, "added": date.today().isoformat()}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {len(tasks)}: {title}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {number}. {task['title']}  (added {task['added']})")
    done_count = sum(1 for task in tasks if task["done"])
    print(f"{done_count} of {len(tasks)} done.")


def choose_task_number(tasks, action):
    """Ask for a task number and return its list index, or None if invalid."""
    if not tasks:
        print("There are no tasks to", action + ".")
        return None
    answer = input(f"Task number to {action}: ").strip()
    try:
        number = int(answer)
    except ValueError:
        print("Please type a number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"There is no task {number}. Choose 1 to {len(tasks)}.")
        return None
    return number - 1


def complete_task(tasks):
    index = choose_task_number(tasks, "complete")
    if index is None:
        return
    if tasks[index]["done"]:
        print("That task is already done.")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[index]['title']}")


def delete_task(tasks):
    index = choose_task_number(tasks, "delete")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    print(f"To-Do List ({len(tasks)} task(s) loaded from {TODO_FILE.name})")

    while True:
        print(MENU)
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
