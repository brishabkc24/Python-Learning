# To-Do List (command line)

## What it does

A menu-driven to-do list. You can add tasks, list them, mark one as complete and delete one. The tasks are saved to `todo.json` in this folder after every change, so they are still there the next time you run the program.

## Concepts used

- A `while True` menu loop with `break` to quit
- Tasks stored as a list of dictionaries (`{"title": ..., "done": ..., "added": ...}`)
- Saving and loading with the `json` module
- `pathlib.Path(__file__)` to find the data file next to the script
- `try` / `except` for missing or damaged files and for bad input
- `enumerate()` to number the tasks when listing them
- `date.today().isoformat()` for the date a task was added

## Files

| File | Purpose |
|---|---|
| `todo.py` | the program |
| `todo.json` | created automatically on the first save; holds your tasks |

## How to run

```
cd 19-projects/todo-cli
python todo.py
```

Delete `todo.json` to start with an empty list again.

## Sample session

```
To-Do List (0 task(s) loaded from todo.json)

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 1
Task title: Buy milk
Added task 1: Buy milk

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 1
Task title: Finish the Python exercises
Added task 2: Finish the Python exercises

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 3
Task number to complete: 1
Completed: Buy milk

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 2
[x] 1. Buy milk  (added 2025-01-15)
[ ] 2. Finish the Python exercises  (added 2025-01-15)
1 of 2 done.

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 9
Please choose a number from 1 to 5.

1. Add a task  2. List tasks  3. Complete a task  4. Delete a task  5. Quit
Choose (1-5): 5
Goodbye!
```

## Ideas to extend it

- Add a due date to each task and sort the list by it.
- Add a "clear completed" option.
- Show only the open tasks, or only the completed ones.

---

[Back to the project index](../README.md)
