# File Handling

File handling means reading data from files and writing data to files. A beginner needs it because everything a program keeps in variables disappears when the program ends; a file keeps the data on disk so it is still there tomorrow.

## What you will learn

- Why programs need files, and how `open()`, `close()` and the `with` statement work
- The file modes (`r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `b`) and what each does to an existing file
- Reading with `read()`, `readline()`, `readlines()` and a `for` loop
- Writing, appending, and moving inside a file with `seek()` and `tell()`
- Handling `FileNotFoundError`, `FileExistsError` and `PermissionError`
- Working with paths using `pathlib` and `os.path`
- Reading and writing CSV and JSON files
- Small practical programs: copying, counting, summing, filtering and word frequency

Some code blocks in this lesson read files from the `datasets` folder. They start with a `DATA_DIR` line that finds that folder relative to the script, so save them as `.py` files inside this topic's `examples` folder before running them. Files that the code creates appear in the folder you run Python from.

## 1. Why files

A variable lives in memory. Memory is cleared when the program stops, so a score, a note or a list of students is lost. A file lives on the disk. Writing to a file is like writing in a notebook: you can close the notebook, come back later and the words are still there.

```python
message = "Remember to water the plants"

with open("reminder.txt", "w", encoding="utf-8") as file:
    file.write(message)

print("Saved. Close Python, open reminder.txt, and the text is still there.")
```

Output:

```
Saved. Close Python, open reminder.txt, and the text is still there.
```

## 2. open() and close()

`open()` connects your program to a file and returns a file object. The first argument is the file name, the second is the mode (`"w"` to write, `"r"` to read). `encoding="utf-8"` tells Python how letters are stored; always pass it for text files so the code behaves the same on every computer. When you are done you must call `close()`, which saves everything and frees the file for other programs.

```python
file = open("notes.txt", "w", encoding="utf-8")
file.write("Python notes\n")
file.close()

file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print(content)
```

Output:

```
Python notes
```

## 3. The with statement

It is easy to forget `close()`, and if an error happens before it the file stays open. The `with` statement solves this: it opens the file, gives it a name after `as`, and closes it automatically when the indented block ends, even when an error occurs inside. This is the way to open files in Python. The mode `"r"` is the default, so you can leave it out when reading.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python notes\n")
    file.write("Files are easy\n")

print("Closed automatically?", file.closed)

with open("notes.txt", encoding="utf-8") as file:
    print(file.read(), end="")
```

Output:

```
Closed automatically? True
Python notes
Files are easy
```

## 4. File modes

The mode tells Python what you plan to do with the file. The table shows what happens when the file already exists and when it does not.

| Mode | Meaning | File exists | File does not exist |
|---|---|---|---|
| `r` | read (default) | reads from the start | `FileNotFoundError` |
| `w` | write | erases everything, then writes | creates it |
| `a` | append | keeps content, writes at the end | creates it |
| `x` | create | `FileExistsError` | creates it |
| `r+` | read and write | reads and writes from the start, nothing erased | `FileNotFoundError` |
| `w+` | write and read | erases everything, then allows reading too | creates it |
| `a+` | append and read | writes at the end, allows reading | creates it |
| `b` | binary, added to another mode (`rb`, `wb`) | works with bytes instead of text, for images and other non-text files | same as the mode it is added to |

```python
with open("modes.txt", "w", encoding="utf-8") as file:   # create or overwrite
    file.write("line 1\n")

with open("modes.txt", "a", encoding="utf-8") as file:   # add to the end
    file.write("line 2\n")

with open("modes.txt", "r", encoding="utf-8") as file:   # read it back
    print(file.read(), end="")
```

Output:

```
line 1
line 2
```

## 5. Reading a file

There are four common ways to read a text file. `read()` returns the whole file as one string.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    text = file.read()

print(type(text))
print(len(text), "characters")
print(text[:40])
```

Output:

```
<class 'str'>
408 characters
Python is a popular programming language
```

`readline()` returns one line each time you call it. The line keeps its newline character `\n` at the end, which is why the first `print` below shows `\n` inside the quotes. `strip()` removes it.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    first = file.readline()
    second = file.readline()

print(repr(first))
print(second.strip())
```

Output:

```
'Python is a popular programming language. It was created by Guido van Rossum and first released in 1991.\n'
Python is easy to read and easy to learn, which makes it a great first language.
```

`readlines()` returns a list with one string per line. Use it when you need to know how many lines there are or want to pick a line by number.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    lines = file.readlines()

print(len(lines), "lines")
print(repr(lines[3]))
```

Output:

```
5 lines
'Python runs on Windows, macOS and Linux.\n'
```

The simplest way to go through a file is a `for` loop directly over the file object. It reads one line at a time, so even a huge file does not fill the memory. Each line still ends with `\n`, so call `strip()` before printing or you will get a blank line after every line.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())
```

Output:

```
1 Python is a popular programming language. It was created by Guido van Rossum and first released in 1991.
2 Python is easy to read and easy to learn, which makes it a great first language.
3 It is used for web development, data analysis, automation, artificial intelligence and much more.
4 Python runs on Windows, macOS and Linux.
5 Many beginners start with Python because the code looks almost like plain English.
```

| Method | Returns | Best for |
|---|---|---|
| `read()` | the whole file as one string | small files, searching the text |
| `readline()` | the next line as a string | reading a header or a few lines |
| `readlines()` | a list of all lines | counting lines, picking a line by index |
| `for line in file` | one line at a time | large files, processing every line |

## 6. Writing to a file

`write()` takes one string and writes it. It does not add a newline, so you must put `\n` at the end of each line yourself. `writelines()` takes a list of strings and writes them one after another, again without adding newlines.

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")
    file.writelines(["bread\n", "rice\n"])

with open("shopping.txt", encoding="utf-8") as file:
    print(file.read(), end="")
```

Output:

```
milk
eggs
bread
rice
```

If you forget the `\n`, everything lands on one line.

```python
with open("joined.txt", "w", encoding="utf-8") as file:
    file.write("milk")
    file.write("eggs")

with open("joined.txt", encoding="utf-8") as file:
    print(file.read())
```

Output:

```
milkeggs
```

## 7. Appending

Mode `"w"` erases the file every time. When you want to keep the old content and add new lines at the end, open the file with mode `"a"` (append). This is how log files and diaries grow.

```python
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Day 1: learned about files\n")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Day 2: learned about append mode\n")

with open("diary.txt", encoding="utf-8") as file:
    print(file.read(), end="")
```

Output:

```
Day 1: learned about files
Day 2: learned about append mode
```

## 8. seek() and tell()

A file object remembers a position, like a finger pointing at the next character to read. `tell()` returns that position, counted in bytes from the start (for plain English text one character is one byte). `seek(n)` moves the finger to position `n`. For the text `Python is fun` the positions are:

| P | y | t | h | o | n | (space) | i | s | (space) | f | u | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

```python
with open("position.txt", "w", encoding="utf-8") as file:
    file.write("Python is fun")

with open("position.txt", encoding="utf-8") as file:
    print("Start:", file.tell())
    print("read(6):", file.read(6))
    print("Now at:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())
    print("read():", file.read())
    file.seek(10)
    print("After seek(10), read():", file.read())
```

Output:

```
Start: 0
read(6): Python
Now at: 6
After seek(0): 0
read(): Python is fun
After seek(10), read(): fun
```

After `read()` reaches the end, another `read()` returns an empty string. `seek(0)` takes you back to the start so you can read the file again without reopening it.

## 9. File exceptions

Three errors appear often when working with files. An exception is an error that happens while the program runs; you catch it with `try` and `except` so the program can carry on. The next topic covers exceptions in detail.

| Exception | When it happens |
|---|---|
| `FileNotFoundError` | reading a file (mode `r`) that does not exist |
| `FileExistsError` | creating a file with mode `x` when it already exists |
| `PermissionError` | the operating system does not allow the action, for example writing to a read-only file |

```python
try:
    with open("does_not_exist.txt", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("That file does not exist")
```

Output:

```
That file does not exist
```

Mode `"x"` is a safe way to create a file: it refuses to overwrite one that is already there.

```python
with open("once.txt", "w", encoding="utf-8") as file:
    file.write("first\n")

try:
    with open("once.txt", "x", encoding="utf-8") as file:
        file.write("second\n")
except FileExistsError:
    print("once.txt already exists, so mode x refused to overwrite it")
```

Output:

```
once.txt already exists, so mode x refused to overwrite it
```

To see `PermissionError`, make a file read-only with `os.chmod` and then try to write to it. The last line makes the file writable again.

```python
import os
import stat

with open("locked.txt", "w", encoding="utf-8") as file:
    file.write("read only\n")
os.chmod("locked.txt", stat.S_IREAD)        # make the file read-only

try:
    with open("locked.txt", "w", encoding="utf-8") as file:
        file.write("new text\n")
except PermissionError:
    print("No permission to write locked.txt")

os.chmod("locked.txt", stat.S_IREAD | stat.S_IWRITE)   # make it writable again
```

Output:

```
No permission to write locked.txt
```

## 10. Checking whether a file exists

Instead of waiting for an error, you can ask first. `pathlib` is the modern way: a `Path` object has an `exists()` method. The older `os.path.exists()` function does the same job and you will see it in a lot of existing code.

```python
import os
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

print((DATA_DIR / "numbers.txt").exists())
print((DATA_DIR / "missing.txt").exists())
print(os.path.exists(DATA_DIR / "numbers.txt"))
print(os.path.exists(DATA_DIR / "missing.txt"))
```

Output:

```
True
False
True
False
```

A typical use is to decide what to do before opening the file.

```python
from pathlib import Path

path = Path("maybe.txt")
if path.exists():
    print("Found it, reading now")
else:
    print("maybe.txt is missing, nothing to read")
```

Output:

```
maybe.txt is missing, nothing to read
```

## 11. pathlib basics

`Path` represents a file or folder location. The `/` operator joins parts of a path, which works on Windows, macOS and Linux without worrying about `\` or `/`. `read_text()` and `write_text()` read or write a whole file in one call, and `name`, `stem`, `suffix` and `parent` take the path apart.

```python
from pathlib import Path

folder = Path("reports")
folder.mkdir(exist_ok=True)              # create the folder if needed
report = folder / "summary.txt"          # the / operator joins paths

report.write_text("Total sales: 42\n", encoding="utf-8")
print("Exists:", report.exists())
print("Content:", report.read_text(encoding="utf-8").strip())
print("Name  :", report.name)
print("Stem  :", report.stem)
print("Suffix:", report.suffix)
print("Parent:", report.parent)
```

Output:

```
Exists: True
Content: Total sales: 42
Name  : summary.txt
Stem  : summary
Suffix: .txt
Parent: reports
```

| Path feature | Example | Result |
|---|---|---|
| join parts | `Path("reports") / "summary.txt"` | `reports/summary.txt` |
| `exists()` | `report.exists()` | `True` or `False` |
| `read_text()` | `report.read_text(encoding="utf-8")` | the whole file as a string |
| `write_text()` | `report.write_text("hi", encoding="utf-8")` | writes the string, replacing the file |
| `name` | `report.name` | `summary.txt` |
| `stem` | `report.stem` | `summary` |
| `suffix` | `report.suffix` | `.txt` |
| `parent` | `report.parent` | `reports` |

## 12. CSV files

CSV (comma-separated values) is a plain text table: one row per line, columns separated by commas. Spreadsheets export this format. The `csv` module reads and writes it correctly, including values that contain commas. Always open CSV files with `newline=""`, otherwise Windows adds blank lines between rows.

`csv.reader` returns each row as a list of strings. The first row is usually the header, so `next(reader)` reads it before the loop.

```python
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Columns:", header)
    for row in reader:
        if int(row[4]) >= 90:
            print(row[1], "scored", row[4])
```

Output:

```
Columns: ['id', 'name', 'age', 'city', 'marks']
Sita Rai scored 92
Kiran Adhikari scored 95
```

`csv.DictReader` uses the header row as keys, so each row is a dictionary and you can write `row["genre"]` instead of `row[4]`. This is easier to read and does not break when columns move.

```python
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "books.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row["genre"] == "Programming":
            print(f"{row['title']} by {row['author']} ({row['year']})")
```

Output:

```
Clean Code by Robert C. Martin (2008)
Automate the Boring Stuff with Python by Al Sweigart (2015)
```

`csv.writer` writes lists. `writerow()` writes one row and `writerows()` writes many.

```python
import csv

rows = [
    ["name", "city", "marks"],
    ["Aarav Sharma", "Kathmandu", 85],
    ["Sita Rai", "Pokhara", 92],
]

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("scores.csv", encoding="utf-8") as file:
    print(file.read(), end="")
```

Output:

```
name,city,marks
Aarav Sharma,Kathmandu,85
Sita Rai,Pokhara,92
```

`csv.DictWriter` writes dictionaries. `fieldnames` fixes the column order and `writeheader()` writes the header row.

```python
import csv

students = [
    {"name": "Bikash Thapa", "city": "Lalitpur", "marks": 67},
    {"name": "Priya Gurung", "city": "Butwal", "marks": 78},
]

with open("scores_dict.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city", "marks"])
    writer.writeheader()
    writer.writerows(students)

with open("scores_dict.csv", encoding="utf-8") as file:
    print(file.read(), end="")
```

Output:

```
name,city,marks
Bikash Thapa,Lalitpur,67
Priya Gurung,Butwal,78
```

| Tool | Reads or writes | Each row is |
|---|---|---|
| `csv.reader` | reads | a list of strings |
| `csv.DictReader` | reads | a dictionary keyed by the header |
| `csv.writer` | writes | a list |
| `csv.DictWriter` | writes | a dictionary |

## 13. JSON files

JSON (JavaScript Object Notation) is a text format for structured data: lists, dictionaries, strings, numbers, booleans and `null`. Web services and configuration files use it everywhere. The `json` module converts between JSON text and Python objects.

| JSON | Python |
|---|---|
| object `{...}` | `dict` |
| array `[...]` | `list` |
| string | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

`json.load(file)` reads a file and returns the Python objects.

```python
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "employees.json", encoding="utf-8") as file:
    employees = json.load(file)

print(type(employees).__name__, "of", len(employees), "items")
print(employees[0])
for person in employees:
    if person["city"] == "Kathmandu":
        print(person["name"], "-", person["department"])
```

Output:

```
list of 8 items
{'id': 101, 'name': 'Asha Koirala', 'department': 'Engineering', 'salary': 85000, 'joined': '2021-03-15', 'city': 'Kathmandu'}
Asha Koirala - Engineering
Kiran Basnet - Finance
Suman Adhikari - Finance
```

`json.dump(data, file)` writes Python objects to a file. `indent=2` adds line breaks and spaces so a person can read the file.

```python
import json

settings = {"theme": "dark", "font_size": 14, "languages": ["en", "ne"]}

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=2)

with open("settings.json", encoding="utf-8") as file:
    print(file.read())
```

Output:

```
{
  "theme": "dark",
  "font_size": 14,
  "languages": [
    "en",
    "ne"
  ]
}
```

`json.dumps()` and `json.loads()` do the same conversions with strings instead of files. The `s` stands for string. They are useful when the JSON comes from a network message rather than a file.

```python
import json

data = {"name": "Sita", "marks": [92, 88]}
text = json.dumps(data)
print(text)
print(type(text).__name__)

back = json.loads(text)
print(back["marks"][0])
print(type(back).__name__)
```

Output:

```
{"name": "Sita", "marks": [92, 88]}
str
92
dict
```

## 14. Practical programs

Copying a file is just reading the content and writing it somewhere else.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as source:
    content = source.read()

with open("sample_copy.txt", "w", encoding="utf-8") as target:
    target.write(content)

print("Copied", len(content), "characters to sample_copy.txt")
```

Output:

```
Copied 408 characters to sample_copy.txt
```

Counting lines, words, characters and vowels uses string methods on the text that `read()` returns. `splitlines()` cuts the text at every newline and `split()` cuts at every run of whitespace.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    text = file.read()

vowels = sum(1 for char in text.lower() if char in "aeiou")

print("Lines     :", len(text.splitlines()))
print("Words     :", len(text.split()))
print("Characters:", len(text))
print("Vowels    :", vowels)
```

Output:

```
Lines     : 5
Words     : 68
Characters: 408
Vowels    : 125
```

Adding up numbers stored one per line: `int()` ignores the newline around the digits, so each line converts directly.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

total = 0
with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    for line in file:
        total += int(line)

print("Sum:", total)
```

Output:

```
Sum: 759
```

Average marks per student: each line of `marks.txt` is a name followed by three marks, so `split()` gives a list where the first item is the name and the rest are marks.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "marks.txt", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        name = parts[0]
        marks = [int(value) for value in parts[1:]]
        average = sum(marks) / len(marks)
        print(f"{name:<8} {average:.2f}")
```

Output:

```
Aarav    84.33
Sita     91.67
Bikash   62.00
Priya    80.00
Rohan    52.33
Anjali   86.00
```

Saving records and reading them back: write one record per line with a separator, then split each line on that separator when reading.

```python
students = [
    ("Aarav Sharma", "Kathmandu"),
    ("Sita Rai", "Pokhara"),
    ("Maya Limbu", "Kathmandu"),
]

with open("students.txt", "w", encoding="utf-8") as file:
    for name, city in students:
        file.write(f"{name},{city}\n")

print("Students from Kathmandu:")
with open("students.txt", encoding="utf-8") as file:
    for line in file:
        name, city = line.strip().split(",")
        if city == "Kathmandu":
            print(" ", name)
```

Output:

```
Students from Kathmandu:
  Aarav Sharma
  Maya Limbu
```

Word frequency: a dictionary maps each word to a count. `get(word, 0)` returns the current count or 0 for a new word. `collections.Counter` does the same job in one line and `most_common()` ranks the results.

```python
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

counts = {}
with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        counts[word] = counts.get(word, 0) + 1
print("python appears", counts["python"], "times")

with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    counter = Counter(line.strip() for line in file)
print(counter.most_common(3))
```

Output:

```
python appears 6 times
[('python', 6), ('java', 4), ('go', 3)]
```

The scripts in [examples/](examples/) contain fuller versions of these programs.

## Common mistakes

- Opening a file with `"w"` to add a line erases everything that was there -> use `"a"` to append.
- Forgetting `"\n"` in `write()` so all the lines run together -> end every line with `"\n"`.
- Printing lines from a file and getting a blank line after each one -> call `line.strip()` or use `print(line, end="")`.
- Calling `read()` twice and getting an empty string the second time -> the position is at the end; call `seek(0)` or open the file again.
- Blank lines between rows when writing CSV on Windows -> open the file with `newline=""`.
- The program finds the file when run from one folder but not from another -> build the path from `Path(__file__)` instead of typing a relative path.

## Summary

- `open()` returns a file object; the `with` statement closes it for you, even when an error happens.
- Modes: `r` read, `w` write (erases), `a` append, `x` create only; add `b` for binary.
- `read()` gives one string, `readline()` one line, `readlines()` a list, and a `for` loop gives one line at a time.
- `write()` and `writelines()` do not add newlines; add `"\n"` yourself.
- `tell()` reports the position in the file and `seek()` moves it.
- Catch `FileNotFoundError`, `FileExistsError` and `PermissionError` with `try`/`except`.
- `pathlib.Path` joins paths with `/`, checks `exists()`, and has `read_text()`, `write_text()`, `name`, `stem` and `suffix`.
- `csv.reader`/`csv.DictReader` read tables and `csv.writer`/`csv.DictWriter` write them; `json.load`/`json.dump` work with files and `json.loads`/`json.dumps` with strings.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Modules and Packages](../08-modules-and-packages/README.md) | [Next: Exception Handling](../10-exception-handling/README.md) | [Home](../README.md)
