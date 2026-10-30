# GUI with Tkinter

A GUI (graphical user interface) is a program you control with windows, buttons and text boxes instead of typed commands. Tkinter is the GUI toolkit that comes with Python, so you can build desktop windows without installing anything extra.

## What you will learn

- What a GUI is and how it differs from a text menu
- How to create a window with `Tk()` and keep it open with `mainloop()`
- The most common widgets and what each one is for
- How to arrange widgets with `pack`, `grid` and `place`
- How to react to button clicks, key presses and mouse clicks
- How to read what the user typed with control variables and `Entry` methods
- How to show pop-up dialogs with `messagebox`
- How to build small complete programs: a login form, a calculator and a to-do list

## 1. What a GUI is and why we use one

Every program you have written so far talks to the user through the terminal. It prints text and waits for `input()`. That is a text interface. A GUI shows a window with buttons, boxes and lists, and the user works with the mouse and the keyboard. A text menu is like reading a list of options out loud; a GUI is like a vending machine where you simply press the button you want.

Here is a text menu. The user has to read the options and type a number.

```python
print("1. Add a task")
print("2. Show tasks")
print("3. Quit")
choice = input("Choose an option: ")
print("You chose option", choice)
```

Output (the user typed `2`):

```
1. Add a task
2. Show tasks
3. Quit
Choose an option: 2
You chose option 2
```

Here is the same menu as a GUI. Each option becomes a button.

```python
import tkinter as tk

window = tk.Tk()
window.title("Task menu")

tk.Button(window, text="Add a task").pack(fill="x", padx=20, pady=5)
tk.Button(window, text="Show tasks").pack(fill="x", padx=20, pady=5)
tk.Button(window, text="Quit", command=window.destroy).pack(fill="x", padx=20, pady=5)

window.mainloop()
```

On screen: a small window titled "Task menu" with three buttons stacked from top to bottom. The first two buttons do nothing yet. Clicking "Quit" closes the window.

| Text menu | GUI |
|---|---|
| The user types a number | The user clicks a button |
| Runs top to bottom, one line at a time | Waits for events (clicks, key presses) and reacts to them |
| Works in any terminal, even over a network | Needs a screen |
| Easy to test by typing or piping input | Tested by using the window |
| Confusing for people who are not programmers | Familiar to everyone |

## 2. Tk() and mainloop()

`tk.Tk()` creates the main window. `mainloop()` starts the event loop. The event loop is a loop that waits for the user to do something (click, type, resize) and keeps the window open while it waits. Without `mainloop()` the program reaches its last line, ends, and the window disappears before you can see it.

```python
import tkinter as tk

window = tk.Tk()   # create the main window
window.mainloop()  # keep it open and wait for events
print("The window was closed.")
```

On screen: an empty grey window with the default title "tk". The `print` line runs only after you close the window with the X button.

Output (after closing the window):

```
The window was closed.
```

We write `import tkinter as tk` so that every widget name starts with `tk.`. That makes it clear which names come from Tkinter.

## 3. Window title and geometry

`title()` sets the text in the title bar. `geometry()` sets the size and, if you want, the position of the window. The string has the form `"WIDTHxHEIGHT+X+Y"` with all numbers in pixels.

```python
import tkinter as tk

window = tk.Tk()
window.title("My first app")
window.geometry("400x250+100+80")
window.resizable(False, False)
window.mainloop()
```

| Part of `"400x250+100+80"` | Meaning |
|---|---|
| `400` | the window is 400 pixels wide |
| `x250` | and 250 pixels tall |
| `+100` | its left edge is 100 pixels from the left edge of the screen |
| `+80` | its top edge is 80 pixels from the top of the screen |

On screen: a window titled "My first app", 400 by 250 pixels, near the top left of the screen. `resizable(False, False)` means the user cannot drag its corners to change the width or the height.

## 4. The common widgets

A widget is a building block of a window: a label, a button, a text box. Everything you see inside a window is a widget. Each widget is created with the window (or another container) as its first argument, which is called its parent.

| Widget | Purpose |
|---|---|
| `tk.Label` | shows a line of text or an image |
| `tk.Button` | a clickable button that runs a function |
| `tk.Entry` | a single-line text box for typing |
| `tk.Text` | a multi-line text box |
| `tk.Checkbutton` | a box that is ticked or not ticked (on or off) |
| `tk.Radiobutton` | a round button; exactly one of a group is selected |
| `tk.Listbox` | a list of lines; the user can select one |
| `ttk.Combobox` | a drop-down list of choices |
| `tk.Scale` | a slider for picking a number in a range |
| `messagebox` | pop-up dialogs such as "OK" messages and "Yes/No" questions |

`ttk` is a second module inside Tkinter with widgets that look more modern. We import it with `from tkinter import ttk`. This program shows one of each widget.

```python
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Widget gallery")

tk.Label(window, text="Label: shows text").pack(anchor="w", padx=10, pady=2)
tk.Button(window, text="Button: click me").pack(anchor="w", padx=10, pady=2)
tk.Entry(window, width=30).pack(anchor="w", padx=10, pady=2)
tk.Text(window, width=30, height=3).pack(anchor="w", padx=10, pady=2)
tk.Checkbutton(window, text="Checkbutton: on or off").pack(anchor="w", padx=10, pady=2)
tk.Radiobutton(window, text="Radiobutton: one of a group", value=1).pack(anchor="w", padx=10, pady=2)

listbox = tk.Listbox(window, height=3)
listbox.insert("end", "Listbox item 1", "Listbox item 2")
listbox.pack(anchor="w", padx=10, pady=2)

ttk.Combobox(window, values=["Combobox: choose one", "Other"]).pack(anchor="w", padx=10, pady=2)
tk.Scale(window, from_=0, to=100, orient="horizontal", label="Scale").pack(anchor="w", padx=10, pady=2)

window.mainloop()
```

On screen: a tall window with the widgets listed one under the other, all pushed to the left (`anchor="w"` means west). You can type in the Entry and the Text box, tick the Checkbutton, open the Combobox and drag the Scale.

## 5. Geometry managers: pack, grid and place

Creating a widget does not show it. You must also place it with a geometry manager. A geometry manager is the part of Tkinter that decides where each widget goes. There are three.

| Manager | How it arranges widgets | Use it when |
|---|---|---|
| `pack()` | stacks widgets top to bottom, or left to right with `side="left"` | you have a simple column or row of widgets |
| `grid()` | puts widgets in rows and columns, like a table | you build a form, a calculator, or anything table-shaped |
| `place()` | puts a widget at exact x and y pixel coordinates | rarely; fixed layouts such as a game board |

`pack` is the simplest. Each call adds the widget below the previous one.

```python
import tkinter as tk

window = tk.Tk()
window.title("pack")

tk.Label(window, text="Top", bg="lightblue").pack(fill="x")
tk.Label(window, text="Middle", bg="lightgreen").pack(fill="x")
tk.Button(window, text="Left", width=10).pack(side="left", padx=5, pady=5)
tk.Button(window, text="Right", width=10).pack(side="left", padx=5, pady=5)

window.mainloop()
```

On screen: two coloured bars across the full width of the window, then two buttons side by side under them.

`grid` is the right choice for forms. Row 0 is the top row and column 0 is the left column.

```python
import tkinter as tk

window = tk.Tk()
window.title("grid")

tk.Label(window, text="First name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Entry(window).grid(row=0, column=1, padx=5, pady=5)
tk.Label(window, text="Last name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Entry(window).grid(row=1, column=1, padx=5, pady=5)
tk.Button(window, text="Save").grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
```

On screen: a neat two-column form. The labels are in the left column, lined up on their right side (`sticky="e"` means stick to the east), and the Save button is centred under both columns because `columnspan=2` lets it span two columns.

`place` uses pixel positions. Resizing the window does not move anything.

```python
import tkinter as tk

window = tk.Tk()
window.title("place")
window.geometry("300x200")

tk.Label(window, text="At (20, 20)", bg="yellow").place(x=20, y=20)
tk.Label(window, text="At (150, 100)", bg="orange").place(x=150, y=100)
tk.Button(window, text="Bottom right").place(x=200, y=160)

window.mainloop()
```

On screen: three widgets at the exact pixel positions given, with empty space around them.

The most useful options are these.

| Option | Works with | Meaning |
|---|---|---|
| `padx`, `pady` | pack, grid | empty space, in pixels, to the left/right and above/below the widget |
| `fill="x"` | pack | stretch the widget to the full width |
| `side="left"` | pack | put widgets next to each other instead of one under the other |
| `anchor="w"` | pack | push the widget to the left (west) edge |
| `sticky="e"` | grid | stick the widget to the east side of its cell (`n`, `s`, `e`, `w` or a mix such as `"we"`) |
| `columnspan=2` | grid | let the widget span two columns |

One rule to remember: a container must use only one geometry manager. If you need both `pack` and `grid`, put the grid widgets inside a `tk.Frame` (an invisible box), pack the frame, and use grid inside it.

## 6. Events: command= and bind()

An event is something that happens: a click, a key press, the mouse moving. There are two ways to react to events.

- `command=` is an option on `Button`, `Checkbutton`, `Radiobutton` and `Scale`. You give it a function name without parentheses. Tkinter calls the function when the widget is used.
- `bind(event_name, function)` works on any widget and on the window. The function receives an event object with details such as the key that was pressed or where the mouse was.

| Event name | Fires when |
|---|---|
| `"<Button-1>"` | the left mouse button is clicked (`<Button-3>` is the right button) |
| `"<Double-Button-1>"` | the left button is double-clicked |
| `"<Key>"` | any key is pressed |
| `"<Return>"` | the Enter key is pressed |
| `"<Motion>"` | the mouse moves over the widget |
| `"<Enter>"`, `"<Leave>"` | the mouse pointer enters or leaves the widget |

```python
import tkinter as tk

def on_button():
    print("Button clicked")

def on_key(event):
    print("Key pressed:", event.keysym)

def on_click(event):
    print(f"Mouse clicked at x={event.x} y={event.y}")

window = tk.Tk()
window.title("Events")

tk.Button(window, text="Click me", command=on_button).pack(pady=10)

area = tk.Label(window, text="Click inside this box or press a key", bg="lightyellow", width=40, height=5)
area.pack(padx=10, pady=10)
area.bind("<Button-1>", on_click)
window.bind("<Key>", on_key)

window.mainloop()
```

Output (the user clicked the button, pressed the `a` key, then clicked inside the yellow box; the numbers depend on where the click lands):

```
Button clicked
Key pressed: a
Mouse clicked at x=132 y=41
```

Notice `command=on_button` has no parentheses. `command=on_button()` would run the function immediately, once, while the window is being built, and the button would do nothing afterwards.

## 7. Control variables: StringVar, IntVar, BooleanVar

A control variable is a special Tkinter variable that is linked to a widget. When the variable changes, the widget updates on screen. When the user changes the widget, the variable changes too. You read one with `.get()` and change it with `.set()`. Create control variables only after `tk.Tk()`, because they belong to the window.

| Class | Holds | Typical widget |
|---|---|---|
| `tk.StringVar` | text | Label, Entry, Radiobutton, Combobox |
| `tk.IntVar` | a whole number | Checkbutton, Scale, Radiobutton |
| `tk.BooleanVar` | `True` or `False` | Checkbutton |
| `tk.DoubleVar` | a decimal number | Scale |

```python
import tkinter as tk

def add_one():
    count.set(count.get() + 1)

window = tk.Tk()
window.title("Counter")

count = tk.IntVar(value=0)
tk.Label(window, textvariable=count, font=("Arial", 24)).pack(pady=10)
tk.Button(window, text="Add one", command=add_one).pack(pady=10)

window.mainloop()
```

On screen: a large "0" above a button. Every click on "Add one" increases the number by one. The label is never updated by hand; it follows the `count` variable.

## 8. Entry methods: get, insert, delete

`Entry` is the single-line text box. Three methods do almost everything.

| Method | What it does |
|---|---|
| `entry.get()` | returns the text in the box as a string |
| `entry.insert(0, "text")` | inserts text at position 0 (the start) |
| `entry.delete(0, "end")` | deletes everything from the start to the end |

```python
import tkinter as tk

def show_and_clear():
    typed = name_entry.get()
    print("You typed:", typed)
    name_entry.delete(0, "end")

window = tk.Tk()
window.title("Entry methods")

name_entry = tk.Entry(window, width=30)
name_entry.insert(0, "Type your name here")
name_entry.pack(padx=10, pady=10)

tk.Button(window, text="Show and clear", command=show_and_clear).pack(pady=5)

window.mainloop()
```

Output (the user replaced the starting text with `Asha` and clicked the button):

```
You typed: Asha
```

`get()` always returns a string. If you need a number, convert it with `int()` or `float()` inside a `try` block, because the user may type letters.

## 9. The Text widget: get("1.0", "end")

`Text` is the multi-line box. Positions inside it are written as `"LINE.COLUMN"`. Lines start at 1 and columns start at 0, so `"1.0"` is the very first character. `"end"` is the position after the last character.

| Index | Meaning |
|---|---|
| `"1.0"` | line 1, column 0: the start of the text |
| `"end"` | just after the last character (includes a final newline that Tkinter adds) |
| `"end-1c"` | one character before `"end"`: the text without that final newline |
| `"insert"` | where the typing cursor is |

```python
import tkinter as tk

def count_words():
    content = notes.get("1.0", "end")
    words = content.split()
    result.config(text=f"Words: {len(words)}")

window = tk.Tk()
window.title("Text widget")

notes = tk.Text(window, width=40, height=6)
notes.insert("1.0", "Python is easy to learn.\nTkinter makes windows.")
notes.pack(padx=10, pady=10)

tk.Button(window, text="Count words", command=count_words).pack()
result = tk.Label(window, text="Words: ?")
result.pack(pady=5)

window.mainloop()
```

On screen: a text box with two lines already in it, a button, and a label. Clicking the button changes the label to "Words: 8". Edit the text and click again to see the count change.

## 10. Reading Checkbutton and Radiobutton values

A `Checkbutton` is linked to a `BooleanVar` (or an `IntVar`). Ticked means `True`. A group of `Radiobutton` widgets shares one variable; each button has its own `value=`, and the variable holds the value of the selected button.

```python
import tkinter as tk

def show_choices():
    print("Newsletter:", subscribe.get())
    print("Size:", size.get())

window = tk.Tk()
window.title("Choices")

subscribe = tk.BooleanVar(value=False)
tk.Checkbutton(window, text="Subscribe to the newsletter", variable=subscribe).pack(anchor="w", padx=10, pady=5)

size = tk.StringVar(value="medium")
for option in ("small", "medium", "large"):
    tk.Radiobutton(window, text=option, variable=size, value=option).pack(anchor="w", padx=10)

tk.Button(window, text="Show choices", command=show_choices).pack(pady=10)

window.mainloop()
```

Output (the user ticked the box, chose "large" and clicked the button):

```
Newsletter: True
Size: large
```

## 11. messagebox dialogs

A dialog is a small pop-up window that shows a message or asks a question. The `messagebox` module has ready-made dialogs. Each takes a title and a message. The `ask...` functions return the user's answer.

| Function | Shows | Returns |
|---|---|---|
| `messagebox.showinfo(title, message)` | a message with an OK button | `"ok"` |
| `messagebox.showwarning(title, message)` | a warning with an OK button | `"ok"` |
| `messagebox.showerror(title, message)` | an error with an OK button | `"ok"` |
| `messagebox.askyesno(title, message)` | Yes and No buttons | `True` for Yes, `False` for No |
| `messagebox.askokcancel(title, message)` | OK and Cancel buttons | `True` for OK, `False` for Cancel |

```python
import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Hello", "Welcome to Tkinter!")

def close_window():
    if messagebox.askyesno("Quit", "Do you really want to quit?"):
        window.destroy()

window = tk.Tk()
window.title("Dialogs")
window.geometry("250x120")

tk.Button(window, text="Say hello", command=say_hello).pack(pady=10)
tk.Button(window, text="Quit", command=close_window).pack(pady=10)

window.mainloop()
```

On screen: two buttons. "Say hello" opens a small box with the message and an OK button. "Quit" opens a Yes/No question; the window closes only if the user clicks Yes.

## 12. Worked program: a label and a button that changes it

The smallest useful program. The function changes the label with `config()`, which updates any option of a widget after it was created.

```python
import tkinter as tk

def change_text():
    message.config(text="You clicked the button!")

window = tk.Tk()
window.title("Label and button")
window.geometry("300x120")

message = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
message.pack(pady=15)

tk.Button(window, text="Click me", command=change_text).pack()

window.mainloop()
```

On screen: the text "Hello, Tkinter!" above a button. After one click the text becomes "You clicked the button!".

## 13. Worked program: a greeting app with Entry

The user types a name, clicks "Greet" (or presses Enter), and a label shows a greeting. The Enter key is bound with a `lambda` because `bind` passes an event argument that `greet()` does not need.

```python
import tkinter as tk

def greet():
    name = name_entry.get().strip()
    if name == "":
        greeting.config(text="Please type your name.", fg="red")
    else:
        greeting.config(text=f"Hello, {name}! Welcome.", fg="blue")

window = tk.Tk()
window.title("Greeting app")

tk.Label(window, text="Your name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.focus()

tk.Button(window, text="Greet", command=greet).grid(row=1, column=0, columnspan=2, pady=5)
greeting = tk.Label(window, text="")
greeting.grid(row=2, column=0, columnspan=2, pady=5)

window.bind("<Return>", lambda event: greet())
window.mainloop()
```

On screen: a label, a text box with the cursor already in it, and a button. Typing "Asha" and pressing Enter shows "Hello, Asha! Welcome." in blue. Clicking with an empty box shows "Please type your name." in red.

## 14. Worked program: a login form

A real program would check a database. Here the correct values are placeholders in two constants. `show="*"` hides the password while it is typed. The result label is green on success and red on failure.

```python
import tkinter as tk

USERNAME = "admin"
PASSWORD = "password123"

def check_login():
    username = username_entry.get().strip()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        result.config(text="Login successful", fg="green")
    else:
        result.config(text="Wrong username or password", fg="red")
        password_entry.delete(0, "end")

window = tk.Tk()
window.title("Login")

tk.Label(window, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(window, width=25)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(window, width=25, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Login", command=check_login).grid(row=2, column=0, columnspan=2, pady=5)
result = tk.Label(window, text="")
result.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
```

On screen: two labelled boxes and a Login button. With `admin` and `password123` the label says "Login successful" in green. With anything else it says "Wrong username or password" in red and the password box is cleared.

## 15. Worked program: a registration form

This form uses several widgets together: two `Entry` boxes, a `Combobox`, three `Radiobutton` widgets inside a `Frame`, a `Checkbutton`, and a read-only `Text` widget for the summary. A `Text` widget with `state="disabled"` cannot be typed into, so the program switches it to `"normal"` just long enough to write the summary.

```python
import tkinter as tk
from tkinter import ttk, messagebox

def register():
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
        f"Newsletter: {'yes' if newsletter.get() else 'no'}",
    ]
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
level_frame = tk.Frame(window)
level_frame.grid(row=3, column=1, sticky="w")
for option in ("Beginner", "Intermediate", "Advanced"):
    tk.Radiobutton(level_frame, text=option, variable=level, value=option).pack(anchor="w")

newsletter = tk.BooleanVar(value=True)
tk.Checkbutton(window, text="Send me the newsletter", variable=newsletter).grid(row=4, column=1, sticky="w", padx=5)

tk.Button(window, text="Register", command=register).grid(row=5, column=0, columnspan=2, pady=8)

summary = tk.Text(window, width=40, height=6, state="disabled")
summary.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
```

On screen: a form with Name and Email boxes, a Course drop-down, three Level radio buttons, a newsletter tick box and a Register button. After filling it in and clicking Register, the grey box at the bottom shows five lines, one per field. Leaving the name empty opens an error dialog instead.

## 16. Worked program: a simple calculator with a grid of buttons

The display is an `Entry` linked to a `StringVar`. The number and operator buttons add their text to the display. The `=` button splits the expression at the operator and computes the answer. This simple calculator handles one operation at a time, such as `12+3` or `7/2`, and the `operator` module gives us the four arithmetic functions.

The buttons are created in a loop. The `lambda k=key: press(k)` trick saves the current `key` for each button; without `k=key`, every button would send the last key of the loop.

```python
import operator
import tkinter as tk
from tkinter import messagebox

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def press(key):
    display.set(display.get() + key)

def clear():
    display.set("")

def calculate():
    expression = display.get()
    try:
        for symbol, operation in OPERATIONS.items():
            if symbol in expression:
                left, right = expression.split(symbol)
                answer = operation(float(left), float(right))
                break
        else:
            answer = float(expression)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear()
        return
    except ValueError:
        messagebox.showerror("Error", "Enter a sum like 12+3.")
        clear()
        return
    if answer == int(answer):
        display.set(str(int(answer)))
    else:
        display.set(str(round(answer, 6)))

window = tk.Tk()
window.title("Calculator")

display = tk.StringVar()
tk.Entry(window, textvariable=display, justify="right", font=("Arial", 16),
         width=16).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

keys = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]
for row_index, row in enumerate(keys, start=1):
    for column_index, key in enumerate(row):
        if key == "=":
            action = calculate
        else:
            action = lambda k=key: press(k)
        tk.Button(window, text=key, width=5, height=2, command=action).grid(
            row=row_index, column=column_index, padx=2, pady=2)

tk.Button(window, text="C", width=24, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

window.mainloop()
```

On screen: a display across the top, a four-by-four grid of keys and a wide "C" (clear) key. Pressing `7`, `/`, `2`, `=` shows `3.5`. Pressing `5`, `/`, `0`, `=` opens an error dialog saying "Cannot divide by zero." and clears the display.

## 17. Worked program: a to-do list with Listbox

The `Listbox` holds the tasks. `insert("end", task)` adds a line at the bottom. `curselection()` returns a tuple with the index of the selected line (empty if nothing is selected), and `delete(index)` removes that line.

```python
import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Empty task", "Type a task first.")
        return
    tasks.insert("end", task)
    task_entry.delete(0, "end")

def remove_task():
    selected = tasks.curselection()
    if not selected:
        messagebox.showwarning("Nothing selected", "Click a task to remove it.")
        return
    tasks.delete(selected[0])

window = tk.Tk()
window.title("To-do list")

task_entry = tk.Entry(window, width=30)
task_entry.grid(row=0, column=0, padx=5, pady=5)
task_entry.bind("<Return>", add_task)
tk.Button(window, text="Add", width=10, command=add_task).grid(row=0, column=1, padx=5)

tasks = tk.Listbox(window, width=40, height=8)
tasks.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

tk.Button(window, text="Remove selected", command=remove_task).grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
```

On screen: a text box with an Add button beside it, a list area, and a Remove button. Typing "Buy milk" and pressing Enter adds the line to the list and clears the box. Clicking a line and then "Remove selected" deletes it. `add_task` has the parameter `event=None` so it works both from the button (no argument) and from the Enter key (one argument).

## Common mistakes

- Forgetting `window.mainloop()` -> the program ends at once and no window appears, or it flashes and disappears. Add `window.mainloop()` as the last line.
- Mixing `pack` and `grid` inside the same container -> the program stops with `cannot use geometry manager grid inside . which already has slaves managed by pack`. Use one manager per container; put a group of widgets in a `tk.Frame` if you need the other manager.
- Reading an `Entry` before the user typed, for example calling `name_entry.get()` right after creating the box -> you get an empty string. Call `get()` inside the function that runs when the button is clicked.
- Writing `command=greet()` with parentheses -> the function runs once while the window is built and the button does nothing. Write `command=greet`.
- Creating a widget but never calling `pack`, `grid` or `place` -> the widget exists but is invisible. Every widget needs a geometry manager call.
- Creating a `StringVar` or `IntVar` before `tk.Tk()` -> `RuntimeError: Too early to create variable: no default root window`. Create the window first.

## Summary

- A GUI reacts to events (clicks, key presses) instead of reading typed commands one after another.
- `window = tk.Tk()` creates the window and `window.mainloop()` keeps it open; it must be the last line.
- `title()`, `geometry("WIDTHxHEIGHT+X+Y")` and `resizable()` control the window itself.
- Widgets are the parts of a window: Label, Button, Entry, Text, Checkbutton, Radiobutton, Listbox, Combobox, Scale.
- Every widget must be placed with `pack`, `grid` or `place`; never mix two managers in one container.
- `command=function` handles button clicks; `bind("<Event>", function)` handles keys and the mouse.
- `StringVar`, `IntVar` and `BooleanVar` link a value to a widget; use `.get()` and `.set()`.
- `entry.get()`, `entry.insert()`, `entry.delete()` and `text.get("1.0", "end")` read and change what the user typed.
- `messagebox.showinfo` shows a message; `messagebox.askyesno` asks a question and returns `True` or `False`.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Databases](../17-databases/README.md) | [Next: Projects](../19-projects/README.md) | [Home](../README.md)
