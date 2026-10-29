"""Exercise 8: count the students per city in students.csv with a Counter."""

from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

cities = []
with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split(",")
        cities.append(parts[3])

city_counts = Counter(cities)
print("Most common:", city_counts.most_common(2))
for city in sorted(city_counts):
    print(city + ":", city_counts[city])
