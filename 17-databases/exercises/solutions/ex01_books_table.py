"""Create a books table, insert three books with ? placeholders, commit, and print every row. Creates ex01_books.db next to this file."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("ex01_books.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        price REAL
    )
""")

books = [
    ("The Hobbit", "J. R. R. Tolkien", 1937, 15.00),
    ("1984", "George Orwell", 1949, 10.99),
    ("Clean Code", "Robert C. Martin", 2008, 35.50),
]
for book in books:
    cursor.execute("INSERT INTO books (title, author, year, price) VALUES (?, ?, ?, ?)", book)
connection.commit()

cursor.execute("SELECT id, title, author, year, price FROM books")
for book_id, title, author, year, price in cursor.fetchall():
    print(f"{book_id}. {title} by {author} ({year}) - {price:.2f}")

connection.close()
