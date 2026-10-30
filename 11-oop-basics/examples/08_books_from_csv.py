"""Build Book objects from datasets/books.csv and search the list.

The dataset folder is found relative to this file, so the script
works from any working directory. Run: python 08_books_from_csv.py
"""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"


class Book:
    def __init__(self, title, author, year, price, genre):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.price:.2f}"


def load_books(path):
    books = []
    with open(path, encoding="utf-8") as file:
        for row in csv.DictReader(file):
            # The CSV gives text, so convert the numbers before storing them.
            books.append(Book(row["title"], row["author"], int(row["year"]),
                              float(row["price"]), row["genre"]))
    return books


books = load_books(DATA_DIR / "books.csv")
print("Books loaded:", len(books))

print("\nLatest book   :", max(books, key=lambda book: book.year))
print("Oldest book   :", min(books, key=lambda book: book.year))
print("Most expensive:", max(books, key=lambda book: book.price))

print("\nProgramming books:")
for book in books:
    if book.genre == "Programming":
        print(" -", book)

total_price = sum(book.price for book in books)
print(f"\nTotal price of all books: {total_price:.2f}")
