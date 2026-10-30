"""Keep students with 80 or more marks, sort them, and save them to output_top_students.csv."""

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

top_students = []
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if int(row["marks"]) >= 80:
            top_students.append({"name": row["name"], "city": row["city"], "marks": int(row["marks"])})

top_students.sort(key=lambda student: student["marks"], reverse=True)

with open(HERE / "output_top_students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city", "marks"])
    writer.writeheader()
    writer.writerows(top_students)

for student in top_students:
    print(f"{student['name']},{student['city']},{student['marks']}")
print("Saved", len(top_students), "students to output_top_students.csv")
