# Datasets

Small sample data files used by the examples, exercises and projects. All names and numbers are fictional.

| File | Format | Columns / content | Used in |
|---|---|---|---|
| `students.csv` | CSV with header | `id, name, age, city, marks` (10 students, marks out of 100) | File Handling, Data Structures, Databases, Projects |
| `books.csv` | CSV with header | `title, author, year, price, genre` (10 books) | OOP, File Handling, Databases |
| `employees.json` | JSON list of objects | `id, name, department, salary, joined (YYYY-MM-DD), city` (8 employees) | File Handling, Collections, Projects |
| `sample_text.txt` | plain text | five sentences about Python | File Handling, Strings, Regular Expressions |
| `numbers.txt` | plain text | one integer per line (20 numbers) | Loops, File Handling, Functions |
| `words.txt` | plain text | one word per line, with repeats (20 words) | Collections (Counter), File Handling |
| `marks.txt` | plain text | `name maths science english`, space separated (6 students) | File Handling, Exception Handling |

## Reading a dataset from a script

Scripts in this repository locate the folder relative to their own file, so they work from any working directory:

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```
