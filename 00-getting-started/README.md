# Getting Started

Python is a programming language whose code reads almost like plain English. This topic shows you how to install Python, how to run your first program and how to use this repository.

## What you will learn

- What Python is and where it is used
- How to install Python on Windows, macOS and Linux
- Three ways to run Python code
- How to write and run your first program
- How to install packages with pip inside a virtual environment
- How this repository is organised and how to study it
- How to read an error message

## 1. What is Python?

Python is a general-purpose programming language. General-purpose means it is not tied to one kind of job. You write instructions in a text file, and a program called the Python interpreter reads that file and carries out the instructions one line at a time.

Python is used in many areas:

| Area | Examples |
|---|---|
| Web development | websites and web services built with Django and Flask |
| Data analysis | tables, charts and reports with pandas and matplotlib |
| Automation | renaming files, sending emails, filling in forms |
| Artificial intelligence | machine learning with scikit-learn, PyTorch and TensorFlow |
| Games | small 2D games with pygame |

Here is a complete Python program. It is one line long.

```python
print("Python is easy to read.")
```

Output:

```
Python is easy to read.
```

## 2. Installing Python

You need Python 3.10 or newer. This repository was tested with Python 3.13.

**Windows**

1. Open https://www.python.org/downloads/ and click the download button.
2. Run the installer.
3. Tick the box **Add python.exe to PATH** before you click **Install Now**. This lets you type `python` in any terminal.

**macOS**

1. Open https://www.python.org/downloads/ and download the macOS installer.
2. Run the installer and accept the defaults.

macOS may also contain an older Python. Use the command `python3` to be sure you run the one you installed.

**Linux**

Most distributions already include Python 3. If yours does not, install it with the package manager. On Ubuntu and Debian:

```
sudo apt install python3 python3-pip python3-venv
```

On Fedora use `sudo dnf install python3`.

**Check the installation**

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS and Linux) and type:

```
python --version
```

Output:

```
Python 3.13.14
```

On macOS and Linux type `python3 --version` instead. Your version number may differ; anything from 3.10 upwards is fine. If you see "command not found" or "python is not recognized", the installer did not add Python to PATH. Run the Windows installer again and tick the PATH box.

## 3. Three ways to run Python code

**The interactive shell (REPL)**

Type `python` (or `python3`) in a terminal and press Enter. You get a prompt that looks like `>>>`. Type one line of Python, press Enter, and Python answers at once. REPL stands for Read, Evaluate, Print, Loop: it reads your line, evaluates it, prints the result and waits for the next line. It is the quickest way to try something out. Type `exit()` to leave.

```
>>> 2 + 3
5
>>> print("hello")
hello
>>> exit()
```

**A .py file from the terminal**

Save your code in a file whose name ends with `.py`, for example `hello.py`. Then run it from the terminal:

```
python hello.py
```

This is how you run every example in this repository.

**VS Code with the Python extension**

Visual Studio Code is a free code editor. Install it from https://code.visualstudio.com/, open the Extensions panel and install the extension named **Python** (published by Microsoft). Open a folder, create a file with a `.py` name, and click the **Run** (play) button in the top-right corner. The output appears in the terminal panel at the bottom of the window.

## 4. Your first program

`print()` writes text to the screen. The text goes inside the brackets, wrapped in quotes. A line that starts with `#` is a comment. Python ignores comments; they are notes for people who read the code.

```python
# My first program
print("Hello, World!")
print("I am learning Python.")
```

Output:

```
Hello, World!
I am learning Python.
```

Save this as `hello.py` and run `python hello.py`. Note that the quotes are not printed; they only tell Python where the text starts and ends.

## 5. pip and virtual environments

`pip` is the tool that installs extra packages. A package is a library of code written by other people, such as `requests` for downloading web pages. A virtual environment is a private folder that holds the packages for one project, so two projects never interfere with each other. Create one inside your project folder:

```
python -m venv .venv
```

Then activate it. You only need the line for your system:

| System | Command |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Command Prompt) | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

The prompt now starts with `(.venv)`. Install a package:

```
pip install requests
```

A file named `requirements.txt` lists the packages a project needs, one per line. Save the current list, or install from it on another computer, with:

```
pip freeze > requirements.txt
pip install -r requirements.txt
```

Type `deactivate` to leave the virtual environment. Everything in this repository uses only the standard library (the modules that come with Python), so you do not need to install any package to follow along.

## 6. How this repository is organised

Each topic has its own numbered folder. Inside every folder you find the same layout:

```
04-loops/
  README.md               the lesson
  examples/               small runnable scripts, numbered in teaching order
  exercises/README.md     practice tasks, easy to hard
  exercises/solutions/    one solution file per exercise
```

Study each topic in this order:

1. Read `README.md` from top to bottom. Type the code blocks yourself instead of copying them.
2. Run every script in `examples/` and read the output.
3. Do the exercises in `exercises/README.md` without looking at the solutions.
4. Compare your code with `exercises/solutions/`. Different code that gives the same result is fine.

Run an example from the repository root like this:

```
python 00-getting-started/examples/01_hello_world.py
```

Output:

```
Hello, World!
I am learning Python.
Single quotes work too.

42
```

## 7. Reading an error message

When something goes wrong, Python stops and prints a traceback. Read it from the bottom up. The last line names the kind of error and explains it. The lines above show the file, the line number and the code that failed. Suppose the file `greet.py`, saved in the folder `C:\code`, contains:

```python
message = "Welcome"
print(mesage)
```

Output:

```
Traceback (most recent call last):
  File "C:\code\greet.py", line 2, in <module>
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

The last line says a `NameError` happened: Python does not know the name `mesage`. The line above points at line 2 of the file (the path is wherever you saved it), and the `^^^^^^` marks the exact spot. Line 2 spelled the variable wrongly. Fix the spelling and run again.

```python
message = "Welcome"
print(message)
```

Output:

```
Welcome
```

## Common mistakes

- Typing `python` and seeing "not recognized" or "command not found" -> install again with the PATH box ticked, or use `python3` on macOS and Linux.
- Writing `print(Hello)` without quotes -> Python looks for a variable named `Hello` and raises a `NameError`. Write `print("Hello")`.
- Saving the file as `hello.py.txt` -> make sure the name ends with `.py` only. In the save dialog choose "All files" as the type.
- Typing `python hello.py` inside the `>>>` prompt -> that prompt expects Python code, not terminal commands. Type `exit()` first, then run the command in the terminal.
- Installing packages without a virtual environment -> create and activate `.venv` first so each project keeps its own packages.

## Summary

- Python is a general-purpose language used for the web, data, automation, AI and games.
- Install it from python.org and check it with `python --version` (or `python3 --version`).
- You can run code in the REPL, from a `.py` file, or from VS Code.
- `print()` writes text to the screen; a line starting with `#` is a comment.
- `pip` installs packages; a virtual environment keeps each project's packages separate.
- Study each topic by reading the lesson, running the examples and doing the exercises.
- Read a traceback from the bottom up: the last line tells you what went wrong.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Next: Python Basics](../01-python-basics/README.md) | [Home](../README.md)
