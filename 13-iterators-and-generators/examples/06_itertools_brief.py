"""
Demonstrates four helpers from the itertools module: count, cycle, chain
and islice, each with a tiny example.
Run: python 06_itertools_brief.py
"""

from itertools import chain, count, cycle, islice

# count(start, step) is an infinite counter.
print("count(10, 5), first four :", list(islice(count(10, 5), 4)))

# cycle() repeats a sequence forever; islice() takes just a slice of it.
print("cycle('AB'), first five  :", list(islice(cycle("AB"), 5)))

# chain() joins several iterables into one stream.
print("chain of list, tuple, str:", list(chain([1, 2], (3, 4), "56")))

# islice(iterable, start, stop, step) slices any iterable, even an infinite one.
print("islice(count(), 2, 10, 3):", list(islice(count(), 2, 10, 3)))

# A practical use of count: number the students without an index variable.
students = ["Aarav", "Sita", "Bikash"]
for seat, name in zip(count(1), students):
    print(f"  Seat {seat}: {name}")

# A practical use of cycle: two players taking turns.
turns = cycle(["Player A", "Player B"])
for move in range(1, 5):
    print(f"  Move {move}: {next(turns)}")
