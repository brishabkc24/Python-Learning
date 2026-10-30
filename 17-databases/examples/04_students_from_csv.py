"""Load datasets/students.csv into a SQLite table and answer questions with SQL.

Run: python 04_students_from_csv.py   (works from any folder)
Creates the file 04_students.db next to this script. The file is removed at
the start of every run, so running it again gives the same output.
"""

import csv
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
DB_FILE = Path(__file__).with_name("04_students.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT,
        marks INTEGER
    )
""")

# Read the CSV file and insert every row with executemany().
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    rows = [(int(row["id"]), row["name"], int(row["age"]), row["city"], int(row["marks"]))
            for row in csv.DictReader(file)]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", rows)
connection.commit()
print(f"Loaded {len(rows)} students into {DB_FILE.name}")

cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1")
name, marks = cursor.fetchone()
print(f"Highest marks: {name} with {marks}")

print("Students per city:")
cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city ORDER BY COUNT(*) DESC, city")
for city, count in cursor.fetchall():
    print(f"  {city:<11} {count}")

cursor.execute("SELECT AVG(marks) FROM students")
print(f"Average marks: {cursor.fetchone()[0]:.1f}")

cursor.execute("SELECT name, city FROM students WHERE marks < ? ORDER BY name", (50,))
print("Below 50:", ", ".join(f"{name} ({city})" for name, city in cursor.fetchall()))

connection.close()
