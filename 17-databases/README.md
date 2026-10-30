# Databases

A database stores data in an organised way so that programs can save it, search it and change it safely. This topic uses SQLite, which is built into Python, and shows the basics of SQL, the language used to talk to databases.

## What you will learn

- What a database is and why programs use one instead of plain files
- Tables, rows, columns and primary keys
- The most common SQL statements
- Using the `sqlite3` module: connect, create tables, insert, select, update, delete
- Why you must use `?` placeholders instead of building SQL with f-strings
- Transactions: `commit()`, `rollback()` and the connection as a context manager
- Loading a CSV file into a table and asking questions with SQL
- Wrapping database code in a small class
- (Optional) the same ideas with a MySQL server

## 1. What is a database?

**Data** is raw facts: the number 92, the word "Pokhara", the name "Sita Rai". **Information** is data arranged so it means something: "Sita Rai from Pokhara scored 92". A **database** is an organised collection of data, stored so that it is easy to find, update and protect. A **database management system** (DBMS) is the program that manages it: SQLite, MySQL, PostgreSQL and others. Your program sends it commands written in **SQL** (Structured Query Language).

An everyday analogy: a database is a well-organised filing cabinet, and SQL is the set of instructions you give the clerk who looks after it.

```python
import sqlite3

# ":memory:" is a database that lives in memory and vanishes when the
# program ends. It is handy for trying things out.
connection = sqlite3.connect(":memory:")
print("SQLite version:", sqlite3.sqlite_version)
print("Connected:", connection)
connection.close()
```

Output (the version and the address depend on your computer):

```
SQLite version: 3.50.4
Connected: <sqlite3.Connection object at 0x0000021E15909A80>
```

## 2. Why use a database instead of files?

You already know how to save data in text and CSV files. Files are fine for small, simple data. Databases solve the problems that appear when data grows or several programs share it.

| Problem with plain files | How a database helps |
|---|---|
| Redundancy: the same fact is copied into several files and the copies drift apart | Each fact is stored once, in one table |
| Loss: a crash while writing can corrupt the whole file | Changes are saved in transactions: all or nothing |
| Security: anyone who can open the file can read everything | Users and permissions control who may read or change what |
| Many users: two programs writing one file at the same time break it | The DBMS coordinates many users at once |
| Searching: you must read the whole file and filter it yourself | One SQL query finds exactly the rows you want, fast |

SQLite keeps the whole database in a single file and needs no server, which makes it perfect for learning and for small programs. MySQL and PostgreSQL run as separate server programs and are used for websites and large systems.

## 3. Tables, rows, columns and primary keys

A database holds **tables**. A table looks like a spreadsheet: every **column** has a name and a type (text, integer, real number), and every **row** is one record. A **primary key** is a column whose value is different in every row, so each row can be found without confusion. In SQLite an `INTEGER PRIMARY KEY` column fills itself in: the first row gets 1, the next gets 2, and so on.

| id | name | city | marks |
|---|---|---|---|
| 1 | Aarav Sharma | Kathmandu | 85 |
| 2 | Sita Rai | Pokhara | 92 |
| 3 | Bikash Thapa | Lalitpur | 67 |

Here `id` is the primary key, `name`, `city` and `marks` are the other columns, and each line is a row.

## 4. SQL crash course

SQL statements read almost like English. Table and column names are written as they are; text values go in single quotes. SQL keywords are usually written in capitals, but SQLite does not care about the case.

| Statement | What it does | Example |
|---|---|---|
| `CREATE TABLE` | Makes a new table with named, typed columns | `CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)` |
| `INSERT` | Adds a row | `INSERT INTO students (name, marks) VALUES ('Sita Rai', 92)` |
| `SELECT` | Reads rows | `SELECT name, marks FROM students` |
| `WHERE` | Keeps only matching rows | `SELECT name FROM students WHERE marks > 80` |
| `ORDER BY` | Sorts the result | `SELECT name FROM students ORDER BY marks DESC` |
| `LIMIT` | Returns at most that many rows | `SELECT name FROM students ORDER BY marks DESC LIMIT 3` |
| `UPDATE` | Changes rows | `UPDATE students SET marks = 95 WHERE name = 'Sita Rai'` |
| `DELETE` | Removes rows | `DELETE FROM students WHERE marks < 40` |
| `COUNT` | Counts rows | `SELECT COUNT(*) FROM students` |
| `AVG` | Averages a column | `SELECT AVG(marks) FROM students` |

`DESC` means descending (largest first); the default is ascending. Be careful with `UPDATE` and `DELETE`: without a `WHERE` clause they change or remove every row in the table.

## 5. sqlite3 step by step

The `sqlite3` module comes with Python. The steps are always the same: **connect** to the database file, get a **cursor** (the object that runs SQL), **execute** statements, **commit** to save changes, **fetch** the results of a `SELECT`, and **close** the connection. `CREATE TABLE IF NOT EXISTS` avoids an error when the table already exists, so the script can run again.

The `?` in an `INSERT` is a **placeholder**. You pass the values separately as a tuple, and sqlite3 puts them in safely. `fetchone()` returns the next row as a tuple, or `None` when there are no more rows. `fetchall()` returns every remaining row as a list of tuples.

```python
import sqlite3
from pathlib import Path

Path("school.db").unlink(missing_ok=True)      # start fresh each run

connection = sqlite3.connect("school.db")      # creates the file if needed
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT,
        marks INTEGER
    )
""")

cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Aarav Sharma", "Kathmandu", 85))
cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Sita Rai", "Pokhara", 92))
cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Bikash Thapa", "Lalitpur", 67))
connection.commit()                            # save the changes

cursor.execute("SELECT * FROM students")
print("First row:", cursor.fetchone())

cursor.execute("SELECT name, marks FROM students WHERE marks > ?", (70,))
print("Marks above 70:", cursor.fetchall())

connection.close()
```

Output:

```
First row: (1, 'Aarav Sharma', 'Kathmandu', 85)
Marks above 70: [('Aarav Sharma', 85), ('Sita Rai', 92)]
```

Without `commit()` the inserted rows are not written to the file, and they are lost when the connection closes. The remaining sections use `:memory:` to keep the code short; everything works the same with a file name.

## 6. Why never build SQL with f-strings

It is tempting to write `f"SELECT ... WHERE name = '{name}'"`. Do not. If the text comes from a user, a crafted value can change the meaning of the query. This is called **SQL injection**, and it is one of the most common security holes in real software. A simple apostrophe in a name such as `O'Brien` also breaks the query. Placeholders solve both problems: the value is always treated as data, never as SQL.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (name TEXT, marks INTEGER)")
cursor.executemany("INSERT INTO students VALUES (?, ?)",
                   [("Aarav Sharma", 85), ("Sita Rai", 92), ("Bikash Thapa", 67)])

user_input = "nobody' OR '1'='1"

# Dangerous: the input becomes part of the SQL and the WHERE is bypassed.
cursor.execute(f"SELECT name FROM students WHERE name = '{user_input}'")
print("f-string result:   ", cursor.fetchall())

# Safe: the input is compared as plain text, so nothing matches.
cursor.execute("SELECT name FROM students WHERE name = ?", (user_input,))
print("placeholder result:", cursor.fetchall())

connection.close()
```

Output:

```
f-string result:    [('Aarav Sharma',), ('Sita Rai',), ('Bikash Thapa',)]
placeholder result: []
```

## 7. executemany, UPDATE, DELETE, COUNT and AVG

`executemany()` runs one statement once for every tuple in a list, which is the easy way to insert many rows. After an `UPDATE` or `DELETE`, `cursor.rowcount` tells how many rows were affected. `COUNT(*)` and `AVG(column)` are **aggregate functions**: they return one value computed from many rows.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)")

products = [("Notebook", 120.0, 50), ("Pen", 25.5, 200),
            ("Backpack", 1500.0, 8), ("Calculator", 850.0, 15)]
cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products)
connection.commit()

cursor.execute("UPDATE products SET price = ? WHERE name = ?", (30.0, "Pen"))
print("Rows updated:", cursor.rowcount)

cursor.execute("DELETE FROM products WHERE stock < ?", (10,))
print("Rows deleted:", cursor.rowcount)
connection.commit()

cursor.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 2")
print("Two most expensive:", cursor.fetchall())

cursor.execute("SELECT COUNT(*), AVG(price) FROM products")
count, average = cursor.fetchone()
print(f"{count} products, average price {average:.2f}")

connection.close()
```

Output:

```
Rows updated: 1
Rows deleted: 1
Two most expensive: [('Calculator', 850.0), ('Notebook', 120.0)]
3 products, average price 333.33
```

## 8. Transactions: rollback and the connection as a context manager

A **transaction** is a group of changes that are saved together or not at all. `commit()` saves them; `rollback()` throws away every change made since the last commit. Using the connection in a `with` statement does this for you: if the block finishes normally the changes are committed, and if an error is raised inside it they are rolled back. Note that `with connection:` does **not** close the connection; call `close()` yourself when you are done.

```python
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance INTEGER)")
cursor.executemany("INSERT INTO accounts VALUES (?, ?)", [("Aarav", 500), ("Sita", 300)])
connection.commit()


def balances():
    cursor.execute("SELECT name, balance FROM accounts ORDER BY name")
    return cursor.fetchall()


cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE name = 'Aarav'")
print("Before rollback:", balances())
connection.rollback()
print("After rollback: ", balances())


def transfer(sender, receiver, amount):
    with connection:            # commit on success, rollback on error
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
        cursor.execute("SELECT balance FROM accounts WHERE name = ?", (sender,))
        if cursor.fetchone()[0] < 0:
            raise ValueError(f"{sender} does not have {amount}")
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))


transfer("Aarav", "Sita", 200)
print("Good transfer:  ", balances())

try:
    transfer("Sita", "Aarav", 5000)
except ValueError as error:
    print("Failed:", error)
print("Failed transfer:", balances())

connection.close()
```

Output:

```
Before rollback: [('Aarav', -500), ('Sita', 300)]
After rollback:  [('Aarav', 500), ('Sita', 300)]
Good transfer:   [('Aarav', 300), ('Sita', 500)]
Failed: Sita does not have 5000
Failed transfer: [('Aarav', 300), ('Sita', 500)]
```

## 9. Loading a CSV file into a table

Real data often arrives as a CSV file. Read it with the `csv` module, insert the rows with `executemany()`, and then let SQL do the work: `ORDER BY ... LIMIT 1` finds the top student, `GROUP BY city` counts students per city, and `AVG(marks)` gives the average. Save this code as a script inside the `examples` folder so the dataset path resolves (`examples/04_students_from_csv.py` is this program).

```python
import csv
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
DB_FILE = Path(__file__).with_name("students_lesson.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT, marks INTEGER
    )
""")

with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    rows = [(int(row["id"]), row["name"], int(row["age"]), row["city"], int(row["marks"]))
            for row in csv.DictReader(file)]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", rows)
connection.commit()
print(f"Loaded {len(rows)} students")

cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1")
print("Highest marks:", cursor.fetchone())

cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city ORDER BY COUNT(*) DESC, city")
print("Students per city:", cursor.fetchall())

cursor.execute("SELECT AVG(marks) FROM students")
print(f"Average marks: {cursor.fetchone()[0]:.1f}")

connection.close()
DB_FILE.unlink()        # remove the database file again
```

Output:

```
Loaded 10 students
Highest marks: ('Kiran Adhikari', 95)
Students per city: [('Kathmandu', 3), ('Pokhara', 2), ('Bhaktapur', 1), ('Biratnagar', 1), ('Butwal', 1), ('Dharan', 1), ('Lalitpur', 1)]
Average marks: 72.0
```

## 10. A small StudentDB class

Spreading SQL all over a program makes it hard to read. A class can hide the SQL behind methods with clear names: `add`, `list_all`, `update_marks`, `delete`. The rest of the program then never sees a single SQL statement. `connection.execute()` is a shortcut that creates a cursor, runs the statement and returns that cursor. `cursor.lastrowid` is the primary key SQLite gave the row you just inserted.

```python
import sqlite3


class StudentDB:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")

    def add(self, name, marks):
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
        return cursor.lastrowid

    def list_all(self):
        return self.connection.execute("SELECT id, name, marks FROM students ORDER BY id").fetchall()

    def update_marks(self, student_id, marks):
        with self.connection:
            cursor = self.connection.execute(
                "UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
        return cursor.rowcount

    def delete(self, student_id):
        with self.connection:
            cursor = self.connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        return cursor.rowcount

    def close(self):
        self.connection.close()


db = StudentDB(":memory:")
db.add("Aarav Sharma", 85)
sita_id = db.add("Sita Rai", 92)
print("All:", db.list_all())
print("Updated:", db.update_marks(sita_id, 95))
print("Deleted:", db.delete(1))
print("All:", db.list_all())
db.close()
```

Output:

```
All: [(1, 'Aarav Sharma', 85), (2, 'Sita Rai', 92)]
Updated: 1
Deleted: 1
All: [(2, 'Sita Rai', 95)]
```

## 11. Optional: MySQL with mysql-connector-python

This section is optional. It needs a **running MySQL server** on your computer and an extra package, and the examples `06_mysql_basics_optional.py` and `07_mysql_crud_optional.py` only work when both are present. Everything else in this topic works without them.

```
pip install mysql-connector-python
```

The ideas are the same as with SQLite. The differences: you connect to a server with a host, a user name and a password instead of opening a file; you create or choose a database with `CREATE DATABASE IF NOT EXISTS` and `USE`; and the placeholder is `%s` instead of `?`. The scripts read the login from the environment variables `MYSQL_USER` and `MYSQL_PASSWORD`, and fall back to the placeholders `root` and `your_password`. Replace them with your own login; never write a real password into a script.

```python
import os

import mysql.connector

USER = os.environ.get("MYSQL_USER", "root")
PASSWORD = os.environ.get("MYSQL_PASSWORD", "your_password")

connection = mysql.connector.connect(host="localhost", user=USER, password=PASSWORD)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS learning_db")
cursor.execute("USE learning_db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        city VARCHAR(50),
        marks INT
    )
""")

cursor.execute("INSERT INTO students (name, city, marks) VALUES (%s, %s, %s)",
               ("Aarav Sharma", "Kathmandu", 85))
connection.commit()
print("Inserted rows:", cursor.rowcount)

cursor.execute("SELECT id, name, marks FROM students WHERE marks >= %s", (80,))
print("Marks 80 or more:", cursor.fetchall())

cursor.execute("UPDATE students SET marks = %s WHERE name = %s", (90, "Aarav Sharma"))
cursor.execute("DELETE FROM students WHERE marks < %s", (40,))
connection.commit()

cursor.close()
connection.close()
```

Output when a MySQL server is running and the login is correct:

```
Inserted rows: 1
Marks 80 or more: [(1, 'Aarav Sharma', 85)]
```

If the server is not running or the password is wrong, `mysql.connector.connect()` raises `mysql.connector.Error`; the example scripts catch it and print a short message.

## Common mistakes

- Rows disappear after the program ends -> you forgot `connection.commit()`. Commit after every change, or use `with connection:`.
- `sqlite3.OperationalError: table students already exists` -> use `CREATE TABLE IF NOT EXISTS`, or delete the old database file at the start.
- Building SQL with f-strings or `+` -> use `?` placeholders (`%s` in MySQL) and pass the values as a tuple.
- `ValueError: parameters are of unsupported type` or a `TypeError` with one value -> the parameters must be a tuple: write `(70,)` with the comma, not `(70)`.
- `UPDATE` or `DELETE` changed every row -> you left out the `WHERE` clause.
- `sqlite3.ProgrammingError: Cannot operate on a closed database` -> you called `close()` too early; close the connection last.

## Summary

- A database is organised data managed by a DBMS; SQL is the language for talking to it.
- Databases beat plain files on redundancy, safety, security, many users and searching.
- Tables have columns and rows; the primary key identifies each row.
- `CREATE TABLE`, `INSERT`, `SELECT ... WHERE ... ORDER BY ... LIMIT`, `UPDATE`, `DELETE`, `COUNT`, `AVG` cover most daily work.
- sqlite3 steps: `connect()`, `cursor()`, `execute()`, `commit()`, `fetchone()` / `fetchall()`, `close()`.
- Always use `?` placeholders; never put values into SQL with f-strings.
- `rollback()` undoes uncommitted changes; `with connection:` commits or rolls back for you but does not close.
- MySQL works the same way through `mysql-connector-python`, with `%s` placeholders and a server login.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Network Programming](../16-network-programming/README.md) | [Next: GUI with Tkinter](../18-gui-tkinter/README.md) | [Home](../README.md)
