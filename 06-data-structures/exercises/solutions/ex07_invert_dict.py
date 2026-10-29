"""Exercise 7: swap the keys and values of a dictionary with a comprehension and with zip."""

marks = {"Sita": 92, "Aarav": 85, "Bikash": 67}

by_comprehension = {mark: name for name, mark in marks.items()}
print("Comprehension:", by_comprehension)

by_zip = dict(zip(marks.values(), marks.keys()))
print("zip:", by_zip)

print("Equal:", by_comprehension == by_zip)
