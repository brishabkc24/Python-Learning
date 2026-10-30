"""
Demonstrates the csv module: reader, DictReader, writer and DictWriter,
using datasets/students.csv and datasets/books.csv.
Run: python 05_csv_files.py
Creates output_toppers.csv and output_cheap_books.csv next to this script.
"""

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

# csv.reader gives each row as a list of strings.
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    rows = list(csv.reader(file))
print("Header       :", rows[0])
print("First student:", rows[1])
print("Student count:", len(rows) - 1)

# csv.DictReader gives each row as a dictionary keyed by the header.
toppers = []
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if int(row["marks"]) >= 85:
            toppers.append(row)
print("Students with 85 or more:")
for student in toppers:
    print(f"  {student['name']} ({student['city']}): {student['marks']}")

# csv.DictWriter writes dictionaries; fieldnames fixes the column order.
with open(HERE / "output_toppers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city", "marks"])
    writer.writeheader()
    for student in toppers:
        writer.writerow(
            {"name": student["name"], "city": student["city"], "marks": student["marks"]}
        )
print("Wrote", len(toppers), "rows to output_toppers.csv")

# csv.writer writes lists; here we keep only the books under 15.00.
cheap_books = []
with open(DATA_DIR / "books.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if float(row["price"]) < 15.00:
            cheap_books.append([row["title"], row["author"], row["price"]])

with open(HERE / "output_cheap_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "author", "price"])
    writer.writerows(cheap_books)
print("Wrote", len(cheap_books), "rows to output_cheap_books.csv")

# Read the new file back to prove it worked.
print("Content of output_cheap_books.csv:")
with open(HERE / "output_cheap_books.csv", newline="", encoding="utf-8") as file:
    for line in file:
        print("  " + line.strip())
