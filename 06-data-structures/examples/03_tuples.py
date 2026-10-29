"""
Tuples: immutable sequences, one-element tuples, packing and unpacking,
count and index, converting to and from lists, and returning several
values from a function.

Run: python 03_tuples.py
"""

# A tuple holds related values that belong together and should not change.
point = (3, 4)
print("point:", point, "| x:", point[0], "| y:", point[1])

# The comma makes the tuple, not the parentheses.
single = (7,)
just_a_number = (7)
print("(7,) is a", type(single).__name__, "| (7) is an", type(just_a_number).__name__)

# Packing several values into one tuple, then unpacking them into names.
record = "Sita", 21, "Pokhara"
name, age, city = record
print(name, "is", age, "and lives in", city)

# Swapping two variables is just packing and unpacking.
first, second = "A", "B"
first, second = second, first
print("after swap:", first, second)

# A star collects the remaining items when unpacking.
top, *rest = (92, 85, 78, 67)
print("top:", top, "| rest:", rest)

# Tuples have only two methods because they never change.
colours = ("red", "green", "red", "blue")
print("count('red'):", colours.count("red"))
print("index('blue'):", colours.index("blue"))

# To change a tuple, convert to a list, edit it, and convert back.
scores = (67, 92, 45)
score_list = list(scores)
score_list.append(85)
score_list.sort()
scores = tuple(score_list)
print("sorted and extended:", scores)


def min_max(values):
    """Return the smallest and largest value as one tuple."""
    return min(values), max(values)


lowest, highest = min_max(scores)
print("lowest:", lowest, "| highest:", highest)

# Tuples can be dictionary keys; lists cannot.
distances = {("Kathmandu", "Pokhara"): 200, ("Kathmandu", "Butwal"): 270}
print("Kathmandu to Pokhara:", distances[("Kathmandu", "Pokhara")], "km")
