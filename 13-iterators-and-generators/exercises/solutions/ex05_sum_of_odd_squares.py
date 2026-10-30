"""Sum the squares of the odd numbers in numbers.txt with a generator expression and compare sizes."""

import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    numbers = [int(line) for line in file]

total = sum(n * n for n in numbers if n % 2 == 1)
print("Sum of odd squares:", total)

odd_squares_list = [n * n for n in numbers if n % 2 == 1]
odd_squares_gen = (n * n for n in numbers if n % 2 == 1)
print("List size:", sys.getsizeof(odd_squares_list), "bytes")
print("Generator size:", sys.getsizeof(odd_squares_gen), "bytes")
