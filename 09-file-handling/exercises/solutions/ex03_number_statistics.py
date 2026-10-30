"""Read datasets/numbers.txt and print count, sum, average, smallest and largest."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

numbers = []
with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line))

print("Count   :", len(numbers))
print("Sum     :", sum(numbers))
print("Average :", round(sum(numbers) / len(numbers), 2))
print("Smallest:", min(numbers))
print("Largest :", max(numbers))
