"""
Demonstrates a generator pipeline over datasets/numbers.txt: read lines,
convert to int, keep the even numbers, square them. Each stage pulls one
item at a time from the stage before it.
Run: python 07_pipeline_numbers.py
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"


def read_lines(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def to_integers(lines):
    for line in lines:
        yield int(line)


def keep_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square(numbers):
    for number in numbers:
        yield number * number


# Connect the stages. Nothing is read from the file until next() is called.
lines = read_lines(DATA_DIR / "numbers.txt")
numbers = to_integers(lines)
evens = keep_even(numbers)
squares = square(evens)

print("First result     :", next(squares))
print("Remaining results:", list(squares))

# The same pipeline written with generator expressions.
with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    values = (int(line) for line in file)
    even_squares = (n * n for n in values if n % 2 == 0)
    print("Sum of even squares:", sum(even_squares))
