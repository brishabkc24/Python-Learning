"""Load datasets/students.csv into SQLite and print, per city, the number of students, their average marks and the best marks. Creates ex05_students.db next to this file."""

import csv
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
DB_FILE = Path(__file__).with_name("ex05_students.db")
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

print(f"{'City':<11} {'Count':>5} {'Average':>8} {'Best':>5}")
cursor.execute("""
    SELECT city, COUNT(*), AVG(marks), MAX(marks)
    FROM students
    GROUP BY city
    ORDER BY AVG(marks) DESC
""")
for city, count, average, best in cursor.fetchall():
    print(f"{city:<11} {count:>5} {average:>8.1f} {best:>5}")

connection.close()
