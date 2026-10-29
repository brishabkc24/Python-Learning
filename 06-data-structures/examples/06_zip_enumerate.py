"""
zip and enumerate: walking two lists together, unzipping with zip(*),
and numbering items without range(len(...)).

Run: python 06_zip_enumerate.py
"""

names = ["Sita", "Aarav", "Bikash", "Priya"]
marks = [92, 85, 67, 78]
cities = ["Pokhara", "Kathmandu", "Lalitpur", "Butwal"]

# zip pairs items by position.
print("name and marks:")
for name, mark in zip(names, marks):
    print(" ", name, mark)

# zip accepts any number of lists.
print("three lists at once:")
for name, mark, city in zip(names, marks, cities):
    print(" ", name, "from", city, "scored", mark)

# zip stops at the shortest list.
short = ["first", "second"]
print("zip with a shorter list:", list(zip(names, short)))

# A list of pairs can be split back into separate tuples with zip(*).
pairs = list(zip(names, marks))
print("pairs:", pairs)
names_again, marks_again = zip(*pairs)
print("names again:", names_again)
print("marks again:", marks_again)

# enumerate gives the index with each item; start chooses the first number.
print("numbered list:")
for position, name in enumerate(names, start=1):
    print(" ", position, name)

# A typical use: find the index of the highest mark.
best_index = 0
for index, mark in enumerate(marks):
    if mark > marks[best_index]:
        best_index = index
print("top student:", names[best_index], "at index", best_index)

# zip and enumerate together.
for row_number, (name, city) in enumerate(zip(names, cities), start=1):
    print(row_number, name, city)
