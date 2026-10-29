"""Exercise 8: read students.csv, group marks by city and print each city's average."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

marks_by_city = {}
with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split(",")
        city = parts[3]
        marks = int(parts[4])
        if city not in marks_by_city:
            marks_by_city[city] = []
        marks_by_city[city].append(marks)

averages = {city: round(sum(marks) / len(marks), 2) for city, marks in marks_by_city.items()}

for city in sorted(averages):
    print(city + ":", averages[city])

print("Highest average:", max(averages, key=averages.get))
