"""
Read datasets/students.csv into a list of dictionaries, then use the
structures from this lesson to find the top student, the marks per city
and the pass list. Only three lines touch the file; File Handling covers
files properly later.

Run: python 08_students_highest_marks.py
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

students = []
with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    header = file.readline()                   # skip: id,name,age,city,marks
    for line in file:
        parts = line.strip().split(",")
        students.append({
            "id": int(parts[0]),
            "name": parts[1],
            "age": int(parts[2]),
            "city": parts[3],
            "marks": int(parts[4]),
        })

print("students read:", len(students))
print("first record:", students[0])

# Highest marks with a loop, then the same with max() and a key.
top = students[0]
for student in students:
    if student["marks"] > top["marks"]:
        top = student
print("highest marks (loop):", top["name"], top["marks"])
best = max(students, key=lambda student: student["marks"])
print("highest marks (max):", best["name"], best["marks"])

# A set of cities and a dictionary of marks per city.
cities = {student["city"] for student in students}
print("cities:", sorted(cities))

marks_by_city = {}
for student in students:
    city = student["city"]
    if city not in marks_by_city:
        marks_by_city[city] = []          # first student from this city
    marks_by_city[city].append(student["marks"])
for city in sorted(marks_by_city):
    print(" ", city, "->", marks_by_city[city])

# Pass list with a comprehension, sorted by marks.
passed = [student["name"] for student in students if student["marks"] >= 40]
print("passed:", len(passed), "of", len(students))
ranked = sorted(students, key=lambda student: student["marks"], reverse=True)
print("top three:", [(student["name"], student["marks"]) for student in ranked[:3]])
