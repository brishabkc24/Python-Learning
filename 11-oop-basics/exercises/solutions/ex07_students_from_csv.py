"""Read datasets/students.csv into Student objects and report top 3, average and low marks."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"


class Student:
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    @classmethod
    def from_row(cls, row):
        return cls(row["name"], int(row["age"]), row["city"], int(row["marks"]))


students = []
with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        students.append(Student.from_row(row))

print("Students loaded:", len(students))

ranked = sorted(students, key=lambda student: student.marks, reverse=True)
print("Top 3:")
for student in ranked[:3]:
    print(f"  {student.name} ({student.marks})")

average = sum(student.marks for student in students) / len(students)
print(f"Average marks: {average:.2f}")

weak = [student.name for student in students if student.marks < 40]
print("Below 40:", ", ".join(weak))
