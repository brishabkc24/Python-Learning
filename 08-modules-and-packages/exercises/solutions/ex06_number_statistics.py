"""Exercise 6: read datasets/numbers.txt and describe the numbers with the statistics module."""

import statistics
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

numbers = []
with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))

print("Count:", len(numbers))
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Standard deviation:", round(statistics.stdev(numbers), 2))
print("Smallest and largest:", min(numbers), max(numbers))
