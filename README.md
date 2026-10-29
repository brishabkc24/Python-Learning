# Python Learning

A complete, beginner-friendly path through Python: from installing it to building small projects.
Every topic has a written lesson, runnable example scripts, and exercises with solutions.
No prior programming experience is needed.

## Who this is for

- Students learning Python as a first language
- Anyone who wants a structured path instead of scattered tutorials
- Learners who prefer short explanations followed by code they can run and change

## How to use this repository

1. Start at `00-getting-started` and follow the topics in order. Each one builds on the previous.
2. In every topic folder:
   - read `README.md` (the lesson),
   - run the scripts in `examples/` and change them,
   - solve the tasks in `exercises/README.md`,
   - compare your answer with `exercises/solutions/`.
3. Finish with `19-projects`, which combines the topics into small real programs.

Run any script from the repository root or from its own folder:

```bash
python 04-loops/examples/01_for_loop.py
```

## Learning path

| # | Topic | What you will learn |
|---|---|---|
| 00 | [Getting Started](00-getting-started/README.md) | Install Python, run your first program, pip and virtual environments, reading error messages |
| 01 | [Python Basics](01-python-basics/README.md) | Variables, data types, input and output, type casting, operators, f-strings |
| 02 | [Strings](02-strings/README.md) | Indexing, slicing, string methods, common string programs |
| 03 | [Control Flow](03-control-flow/README.md) | if, elif, else, nested conditions, match-case |
| 04 | [Loops](04-loops/README.md) | for, while, range, break, continue, nested loops, patterns |
| 05 | [Functions](05-functions/README.md) | Parameters, return values, scope, lambda, map and filter, recursion |
| 06 | [Data Structures](06-data-structures/README.md) | Lists, tuples, sets, dictionaries, comprehensions, zip and enumerate |
| 07 | [The collections Module](07-collections-module/README.md) | Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap |
| 08 | [Modules and Packages](08-modules-and-packages/README.md) | Importing, writing your own modules and packages, the standard library, pip |
| 09 | [File Handling](09-file-handling/README.md) | Reading and writing files, file modes, pathlib, CSV and JSON |
| 10 | [Exception Handling](10-exception-handling/README.md) | try, except, else, finally, raise, custom exceptions |
| 11 | [OOP Basics](11-oop-basics/README.md) | Classes, objects, `__init__`, `self`, attributes, methods, `__str__` |
| 12 | [OOP Advanced](12-oop-advanced/README.md) | Inheritance, polymorphism, encapsulation, abstraction, composition |
| 13 | [Iterators and Generators](13-iterators-and-generators/README.md) | iter and next, custom iterators, yield, generator expressions |
| 14 | [Regular Expressions](14-regular-expressions/README.md) | The re module, patterns, groups, validating phone numbers, emails and dates |
| 15 | [Multithreading](15-multithreading/README.md) | Threads, start and join, locks, race conditions, the thread life cycle |
| 16 | [Network Programming](16-network-programming/README.md) | Sockets, client and server programs, chat between programs |
| 17 | [Databases](17-databases/README.md) | SQL basics, sqlite3, CRUD operations, an optional MySQL section |
| 18 | [GUI with Tkinter](18-gui-tkinter/README.md) | Windows, widgets, layouts, events, a login form and a calculator |
| 19 | [Projects](19-projects/README.md) | Seven small projects that combine everything above |

## Repository structure

```
Python-Learning/
├── 00-getting-started/
│   ├── README.md              # the lesson
│   ├── examples/              # runnable scripts, numbered in teaching order
│   └── exercises/
│       ├── README.md          # exercise list, easy to hard
│       └── solutions/         # one solution file per exercise
├── 01-python-basics/
│   └── ... (same layout)
├── ...
├── 19-projects/               # one folder per project
├── datasets/                  # sample CSV, JSON and text files used by the lessons
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer (`python --version` to check)
- Everything uses the standard library. Tkinter ships with Python on Windows and macOS; on some Linux distributions install it with `sudo apt install python3-tk`.
- Optional: `pip install -r requirements.txt` installs `mysql-connector-python`, needed only for the MySQL section of the Databases topic. Every other database example uses the built-in `sqlite3` module.

## Datasets

The `datasets/` folder holds small fictional data files (students, books, employees, text, numbers) that the file handling, collections, database and project lessons work on. See [datasets/README.md](datasets/README.md) for the columns in each file.

## Projects

| Project | Concepts |
|---|---|
| Number guessing game | loops, random, functions, input validation |
| To-do CLI | lists and dictionaries, JSON files, menus |
| Contact book | CSV files, searching, exception handling |
| Student management | classes, sqlite3, CRUD |
| Quiz app | JSON, random, scoring |
| Calculator GUI | Tkinter, grid layout, events |
| Chat app | sockets, threading, client and server |

## Found a mistake?

Open an issue or a pull request. Fixes to explanations, outputs and exercises are welcome.

## License

Released under the [MIT License](LICENSE).
