"""Load datasets/books.csv into SQLite and find the most expensive book, the number of books per genre and the average price. Creates ex04_books.db next to this file."""

import csv
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
DB_FILE = Path(__file__).with_name("ex04_books.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        title TEXT, author TEXT, year INTEGER, price REAL, genre TEXT
    )
""")

with open(DATA_DIR / "books.csv", newline="", encoding="utf-8") as file:
    rows = [(row["title"], row["author"], int(row["year"]), float(row["price"]), row["genre"])
            for row in csv.DictReader(file)]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?)", rows)
connection.commit()
print(f"Loaded {len(rows)} books")

cursor.execute("SELECT title, price FROM books ORDER BY price DESC LIMIT 1")
title, price = cursor.fetchone()
print(f"Most expensive: {title} ({price:.2f})")

print("Books per genre:")
cursor.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre ORDER BY COUNT(*) DESC, genre")
for genre, count in cursor.fetchall():
    print(f"  {genre:<12} {count}")

cursor.execute("SELECT AVG(price) FROM books")
print(f"Average price: {cursor.fetchone()[0]:.2f}")

connection.close()
