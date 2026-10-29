"""
defaultdict with int and list defaults: group the students in
datasets/students.csv by city and total their marks, without ever
checking whether a key exists.

Run: python 03_defaultdict_grouping.py
"""

from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

students_by_city = defaultdict(list)    # missing key -> []
marks_total = defaultdict(int)          # missing key -> 0
count_by_city = defaultdict(int)

with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    header = file.readline()            # skip: id,name,age,city,marks
    for line in file:
        parts = line.strip().split(",")
        name, city, marks = parts[1], parts[3], int(parts[4])
        students_by_city[city].append(name)
        marks_total[city] += marks
        count_by_city[city] += 1

print("Students grouped by city:")
for city in sorted(students_by_city):
    average = marks_total[city] / count_by_city[city]
    print(" ", city, "->", students_by_city[city], "| average:", round(average, 1))

print()
print("cities with more than one student:",
      [city for city, names in students_by_city.items() if len(names) > 1])

# Reading a missing key creates it, which is sometimes a surprise.
print("students in Dharan:", students_by_city["Dharan"])
print("students in Hetauda:", students_by_city["Hetauda"])
print("'Hetauda' is now a key:", "Hetauda" in students_by_city)

# The plain-dictionary version of the grouping, for comparison.
plain = {}
for city, names in students_by_city.items():
    if city not in plain:
        plain[city] = []
    plain[city].extend(names)
print("same grouping with a plain dict:", plain == dict(students_by_city))
