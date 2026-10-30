"""SQLite step by step: connect, create a table, insert rows, read them back.

Run: python 01_sqlite_basics.py
Creates the file 01_sqlite_basics.db next to this script. The file is
removed at the start of every run, so running it again gives the same output.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("01_sqlite_basics.db")
DB_FILE.unlink(missing_ok=True)         # start fresh every run

# 1. connect() opens the database file (and creates it if it is missing).
connection = sqlite3.connect(DB_FILE)

# 2. A cursor is the object that runs SQL statements.
cursor = connection.cursor()

# 3. Create the table. IF NOT EXISTS avoids an error if it already exists.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT,
        marks INTEGER
    )
""")

# 4. Insert rows. The ? placeholders are filled in safely by sqlite3.
cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Aarav Sharma", "Kathmandu", 85))
cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Sita Rai", "Pokhara", 92))
cursor.execute("INSERT INTO students (name, city, marks) VALUES (?, ?, ?)",
               ("Bikash Thapa", "Lalitpur", 67))

# 5. commit() saves the changes to the file. Without it they are lost.
connection.commit()
print("Three rows inserted and saved.")

# 6. SELECT and fetch the results.
cursor.execute("SELECT * FROM students")
first_row = cursor.fetchone()           # one row as a tuple
print("First row:", first_row)

cursor.execute("SELECT name, marks FROM students WHERE marks > ?", (70,))
good_students = cursor.fetchall()       # all remaining rows as a list
print("Marks above 70:")
for name, marks in good_students:
    print(f"  {name}: {marks}")

# 7. Always close the connection when you are done.
connection.close()
print("Database saved in", DB_FILE.name)
