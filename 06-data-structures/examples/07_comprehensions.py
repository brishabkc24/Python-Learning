"""
List, dictionary and set comprehensions: the plain form, with a filter,
with if-else, nested, and some practical clean-up jobs. Each one is
shown next to the loop it replaces.

Run: python 07_comprehensions.py
"""

numbers = [3, 8, 1, 6, 4, 9]

# The loop way and the comprehension way give the same list.
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)
doubled = [n * 2 for n in numbers]
print("doubled (loop):", doubled_loop)
print("doubled (comprehension):", doubled)

# A condition at the end keeps only some items.
evens = [n for n in numbers if n % 2 == 0]
print("evens:", evens)

# if-else at the front chooses a value for every item.
sizes = ["big" if n >= 5 else "small" for n in numbers]
print("sizes:", sizes)

# Nested: two for parts give every combination.
shirts = [(size, colour) for size in ["S", "M"] for colour in ["red", "blue"]]
print("shirts:", shirts)

# A comprehension inside a comprehension builds a grid.
multiplication = [[row * col for col in range(1, 4)] for row in range(1, 4)]
for row in multiplication:
    print(" ", row)

# Dictionary comprehension: key: value.
words = ["python", "list", "comprehension"]
lengths = {word: len(word) for word in words}
print("lengths:", lengths)

# Set comprehension: unique results only.
remainders = {n % 3 for n in numbers}
print("remainders when divided by 3:", sorted(remainders))

# Practical: remove None values from survey answers.
answers = ["yes", None, "no", None, "yes"]
valid = [answer for answer in answers if answer is not None]
print("valid answers:", valid)

# Practical: label pass or fail.
marks = {"Sita": 92, "Rohan": 45, "Maya": 38, "Nabin": 59}
results = {name: "pass" if mark >= 40 else "fail" for name, mark in marks.items()}
print("results:", results)

# Practical: clean up strings.
raw_cities = ["  pokhara", "KATHMANDU ", " Butwal"]
clean_cities = [city.strip().title() for city in raw_cities]
print("clean cities:", clean_cities)
