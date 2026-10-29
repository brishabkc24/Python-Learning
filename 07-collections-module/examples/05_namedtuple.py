"""
namedtuple: define a record type, create values, read fields by name or
index, convert with _asdict, make changed copies with _replace, and sort
a list of records by a field.

Run: python 05_namedtuple.py
"""

from collections import namedtuple

# Field names can be given as a list or as one space-separated string.
Point = namedtuple("Point", "x y")
Student = namedtuple("Student", ["name", "age", "city", "marks"])

origin = Point(0, 0)
corner = Point(x=3, y=4)
print("points:", origin, corner)
print("distance:", (corner.x ** 2 + corner.y ** 2) ** 0.5)

sita = Student("Sita", 21, "Pokhara", 92)
print("record:", sita)
print("by name:", sita.name, sita.marks)
print("by index:", sita[0], sita[3])
print("as dict:", sita._asdict())
print("fields:", Student._fields)

# A namedtuple cannot be changed; _replace gives a changed copy.
promoted = sita._replace(age=22, marks=95)
print("replaced:", promoted)
print("original:", sita)

# _make builds a record from any sequence, handy for rows read from a file.
row = ["Aarav", 20, "Kathmandu", 85]
aarav = Student._make(row)
print("from a list:", aarav)

# Records in a list can be sorted by any field.
students = [sita, aarav, Student("Bikash", 19, "Lalitpur", 67)]
by_marks = sorted(students, key=lambda student: student.marks, reverse=True)
for student in by_marks:
    print(" ", student.name.ljust(8), student.marks)

# Unpacking works exactly like a normal tuple.
name, age, city, marks = aarav
print(name, "from", city, "is", age, "and scored", marks)
