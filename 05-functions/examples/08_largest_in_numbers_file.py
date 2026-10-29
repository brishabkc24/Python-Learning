"""
Find the largest, smallest and average of the numbers in
datasets/numbers.txt using small functions. The file is located relative
to this script, so the script works from any working directory.

Run: python 08_largest_in_numbers_file.py
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"


def read_numbers(file_path):
    """Return the integers in a file that has one number per line."""
    numbers = []
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


def find_largest(values):
    """Return the largest value without using max()."""
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


def find_smallest(values):
    """Return the smallest value without using min()."""
    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
    return smallest


def average(values):
    """Return the mean of the values, rounded to 2 decimals."""
    return round(sum(values) / len(values), 2)


numbers = read_numbers(DATA_DIR / "numbers.txt")

print("Numbers read:", len(numbers))
print("Largest:", find_largest(numbers))
print("Smallest:", find_smallest(numbers))
print("Average:", average(numbers))

# The built-in functions give the same answers in one call each.
print("Check with built-ins:", max(numbers), min(numbers))
