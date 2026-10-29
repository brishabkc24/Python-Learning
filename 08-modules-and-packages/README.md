# Modules and Packages

A module is a file of Python code that you can load into another program with `import`. Modules let you split a big program into small files, reuse your own code, and use the huge library of ready-made code that comes with Python.

## What you will learn

- What a module is and the four ways to import one
- How to write your own module and import it from another script
- What `if __name__ == "__main__":` does and why nearly every script has it
- How to group modules into a package with `__init__.py`
- Where Python looks for modules (`sys.path`)
- A quick tour of useful standard library modules
- How to explore a module with `dir()` and `help()`
- Installing third-party packages with `pip`, and why virtual environments matter

## 1. What is a module

Every `.py` file is a module. When you write `import math`, Python finds the file for the `math` module, runs it once, and gives you a module object whose functions and variables you reach with a dot. The standard library is the collection of modules that ships with Python, such as `math`, `random` and `datetime`. Think of a module as a toolbox: `import` brings the toolbox in, and the dot picks a tool out of it.

```python
import math

print(math.sqrt(16))
print(math.pi)
print(type(math))
```

Output:

```
4.0
3.141592653589793
<class 'module'>
```

## 2. Import styles

There are four ways to import. The first two keep the module name as a prefix, which makes it clear where each function comes from. The third brings chosen names in directly, which is shorter. The fourth, `from module import *`, brings in every name and is best avoided.

| Style | How you call it | When to use it |
|---|---|---|
| `import math` | `math.sqrt(25)` | the normal choice; clear and safe |
| `import math as m` | `m.sqrt(25)` | a long module name used many times |
| `from math import sqrt, pi` | `sqrt(25)` | a few names used very often |
| `from math import *` | `sqrt(25)` | avoid: hides where names come from |

```python
import math
print(math.sqrt(25))

import math as m
print(m.sqrt(25))

from math import sqrt, pi
print(sqrt(25), pi)

from math import factorial as fact
print(fact(5))
```

Output:

```
5.0
5.0
5.0 3.141592653589793
120
```

`from math import *` silently replaces any name you already have with the module's version. Here the built-in `pow` is replaced by `math.pow`, which returns a float instead of an integer, and nothing in the code shows that it happened.

```python
print(pow(2, 3))

from math import *

print(pow(2, 3))
```

Output:

```
8
8.0
```

## 3. Creating your own module

Any file you write is a module too. Save the code below as `greetings.py`. It defines a constant and two functions, and the last block is explained in the next section. The file is in this lesson's `examples` folder.

```python
"""
A tiny module with two greeting functions, used by 02_use_greetings.py
and 03_name_main_demo.py to show how importing your own file works.

Run directly to see its self-test: python greetings.py
"""

DEFAULT_NAME = "friend"


def hello(name=DEFAULT_NAME):
    """Return a greeting for the given name."""
    return "Hello, " + name + "!"


def goodbye(name=DEFAULT_NAME):
    """Return a farewell for the given name."""
    return "Goodbye, " + name + "."


if __name__ == "__main__":
    print(hello("tester"))
    print(goodbye("tester"))
```

Now a second file in the same folder can import it. The module name is the file name without `.py`. Run this script from inside the `examples` folder (it is `02_use_greetings.py`).

```python
import greetings

print(greetings.hello("Sita"))
print(greetings.goodbye())
print("default name:", greetings.DEFAULT_NAME)

from greetings import hello
print(hello("Aarav"))
```

Output:

```
Hello, Sita!
Goodbye, friend.
default name: friend
Hello, Aarav!
```

## 4. if __name__ == "__main__"

Every module has a variable called `__name__`. When you run a file directly, Python sets its `__name__` to the string `"__main__"`. When the file is imported, `__name__` is the module's name instead. So the test `if __name__ == "__main__":` means "only when this file is run directly". Code inside it runs for `python greetings.py` but not for `import greetings`. That lets a module carry its own demo or tests without running them every time it is imported.

```python
import greetings

print("In this script, __name__ is", __name__)
print("In the imported module, __name__ is", greetings.__name__)
print("Imported, so the test block in greetings.py did not print anything above.")
```

Output:

```
In this script, __name__ is __main__
In the imported module, __name__ is greetings
Imported, so the test block in greetings.py did not print anything above.
```

Running the module itself does trigger the block:

```
python greetings.py
Hello, tester!
Goodbye, tester.
```

## 5. Packages

A package is a folder of modules. The folder must contain a file named `__init__.py`, which can be empty; its presence tells Python that the folder is a package. You import a module from a package with a dot between the package name and the module name. The `examples/shapes` folder of this lesson is a package with three files.

`shapes/__init__.py` runs when the package is imported. Here it pulls the two area functions up to package level, so `shapes.circle_area` works as well as `shapes.circle.circle_area`.

```python
"""
The shapes package: area and perimeter helpers for circles and rectangles.
Importing the package makes circle_area and rectangle_area available
directly as shapes.circle_area and shapes.rectangle_area.
"""

from shapes.circle import circle_area
from shapes.rectangle import rectangle_area

__all__ = ["circle_area", "rectangle_area"]
```

`shapes/circle.py`:

```python
"""Circle helpers for the shapes package."""

import math


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


def circle_perimeter(radius):
    """Return the perimeter (circumference) of a circle."""
    return 2 * math.pi * radius
```

`shapes/rectangle.py` has `rectangle_area(width, height)` and `rectangle_perimeter(width, height)` in the same style. A script in the `examples` folder can now use the package in several ways (this is `04_use_shapes_package.py`).

```python
import shapes
from shapes import circle
from shapes.rectangle import rectangle_perimeter

print("circle area:", round(shapes.circle_area(2), 2))
print("circle perimeter:", round(circle.circle_perimeter(2), 2))
print("rectangle area:", shapes.rectangle_area(3, 4))
print("rectangle perimeter:", rectangle_perimeter(3, 4))
```

Output:

```
circle area: 12.57
circle perimeter: 12.57
rectangle area: 12
rectangle perimeter: 14
```

## 6. Where Python looks for modules

When you import, Python searches a list of folders in order and uses the first match. The list is `sys.path`. Its first entry is the folder of the script you ran, which is why `import greetings` works from the `examples` folder. After that come any folders in the `PYTHONPATH` environment variable, the standard library, and the `site-packages` folder where `pip` installs packages. You can add a folder yourself with `sys.path.append("folder")`, but keeping related files together is simpler.

```python
import sys

print("first entry (the script's folder):", sys.path[0])
print("number of entries:", len(sys.path))
```

Output (yours will differ):

```
first entry (the script's folder): D:\Python-Learning\08-modules-and-packages\examples
number of entries: 5
```

If a module cannot be found in any of these folders, you get `ModuleNotFoundError: No module named 'name'`.

## 7. Standard library tour

Python ships with hundreds of modules. These are the ones you will meet first. `random.seed()` fixes the sequence of random numbers, so the output below is the same on every run.

```python
import math
import random
import statistics

print("math:", math.sqrt(2), math.floor(3.7), math.ceil(3.2), math.gcd(12, 18))

random.seed(42)                      # same "random" numbers every run
print("random:", random.randint(1, 6), random.choice(["red", "green", "blue"]))
print("random:", random.sample(range(1, 50), 3))

marks = [67, 92, 45, 85, 92]
print("statistics:", statistics.mean(marks), statistics.median(marks), statistics.mode(marks))
```

Output:

```
math: 1.4142135623730951 3 4 6
random: 6 red
random: [2, 48, 18]
statistics: 76.2 85 92
```

`datetime` works with dates and times; `time` measures time and pauses the program.

```python
import datetime
import time

exam_day = datetime.date(2026, 3, 15)
print("exam day:", exam_day)
print("formatted:", exam_day.strftime("%d %B %Y, %A"))
print("results day:", exam_day + datetime.timedelta(days=30))
print("days between:", (datetime.date(2026, 12, 25) - exam_day).days)

start = time.perf_counter()
time.sleep(0.2)
print("slept for about", round(time.perf_counter() - start, 1), "seconds")
```

Output:

```
exam day: 2026-03-15
formatted: 15 March 2026, Sunday
results day: 2026-04-14
days between: 285
slept for about 0.2 seconds
```

The current date and time change every run, so this block's output will not match yours.

```python
import datetime
import os
import sys

print("today:", datetime.date.today())
print("now:", datetime.datetime.now().strftime("%H:%M"))
print("current folder:", os.getcwd())
print("python version:", sys.version_info.major, ".", sys.version_info.minor)
print("operating system:", os.name)
```

Output (yours will differ):

```
today: 2026-10-29
now: 09:45
current folder: D:\Python-Learning\08-modules-and-packages\examples
python version: 3 . 13
operating system: nt
```

`json` converts between Python data and JSON text, the format most web services use. `json.dumps` makes text from data and `json.loads` makes data from text. Reading and writing JSON files is covered in File Handling.

```python
import json

student = {"name": "Sita", "marks": [92, 85], "passed": True}
text = json.dumps(student)
print(text, type(text))
print(json.loads(text)["marks"])
```

Output:

```
{"name": "Sita", "marks": [92, 85], "passed": true} <class 'str'>
[92, 85]
```

## 8. dir() and help()

`dir(module)` lists every name inside a module. Names that start and end with two underscores are internal, so they are usually filtered out. `help(thing)` prints the documentation of a module, function or class, taken from its docstrings. Both work on your own modules as well as the standard library, which is a good reason to write docstrings.

```python
import greetings

names = [name for name in dir(greetings) if not name.startswith("__")]
print("names in greetings:", names)
help(greetings.hello)
```

Output:

```
names in greetings: ['DEFAULT_NAME', 'goodbye', 'hello']
Help on function hello in module greetings:

hello(name='friend')
    Return a greeting for the given name.

```

Try `help(math)` or `help(str.split)` in the Python shell to see the same idea on built-in code.

## 9. pip, requirements.txt and virtual environments

Packages that are not in the standard library are published on the Python Package Index (PyPI) and installed with `pip`, the package installer that comes with Python. These commands are typed in a terminal, not in Python.

```
pip install requests
pip install requests==2.32.3
pip list
pip uninstall requests
```

A `requirements.txt` file lists the packages a project needs, one per line, so anyone can install them all with one command.

```
requests==2.32.3
rich==13.7.1
```

```
pip install -r requirements.txt
```

A virtual environment is a private copy of Python for one project, so projects with different package versions do not disturb each other. Create one in the project folder, activate it, and then `pip install` puts packages inside it only.

```
python -m venv .venv
.venv\Scripts\activate        (Windows)
source .venv/bin/activate     (macOS and Linux)
pip install -r requirements.txt
deactivate
```

Everything in this repository uses only the standard library, so no installs are needed.

## Common mistakes

- Naming your file `random.py` or `math.py` -> your file shadows the real module and `import random` loads yours; pick a different name.
- Writing `import greetings` and then calling `hello()` -> `NameError`; call `greetings.hello()` or import the name with `from greetings import hello`.
- Running a script from a different folder and getting `ModuleNotFoundError` -> Python looks in the script's own folder first; keep the module next to the script or add its folder to `sys.path`.
- Forgetting `__init__.py` in a package folder -> older Python versions cannot import it; always add the file.
- Putting test prints at the top level of a module -> they run on every import; move them under `if __name__ == "__main__":`.
- Using `from module import *` -> names collide silently; import the names you need.

## Summary

- A module is a `.py` file; `import name` loads it and `name.thing` uses what is inside.
- Prefer `import module` or `from module import a, b`; avoid `from module import *`.
- Your own files are modules too, as long as they are on `sys.path` (the script's folder is).
- `if __name__ == "__main__":` guards code that should run only when the file is run directly.
- A package is a folder with `__init__.py`; import its modules with `package.module`.
- `math`, `random`, `datetime`, `time`, `os`, `sys`, `statistics` and `json` cover many everyday jobs.
- `dir()` lists what a module contains and `help()` shows its documentation.
- `pip install` adds third-party packages; a virtual environment keeps each project's packages separate.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: The collections Module](../07-collections-module/README.md) | [Next: File Handling](../09-file-handling/README.md) | [Home](../README.md)
