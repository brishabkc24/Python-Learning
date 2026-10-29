"""
List basics: creating a list, indexing, slicing, nested lists and the
most common list methods, each shown with a labelled result.

Run: python 01_list_basics.py
"""

marks = [85, 92, 67, 78, 45]
print("marks:", marks)
print("first:", marks[0], "| last:", marks[-1], "| count:", len(marks))
print("first three:", marks[:3])
print("last two:", marks[-2:])
print("reversed copy:", marks[::-1])

# Changing an item in place: lists are mutable.
marks[2] = 70
print("after marks[2] = 70:", marks)

# Adding items: append puts one item at the end, extend adds many.
marks.append(88)
marks.extend([59, 73])
print("after append and extend:", marks)

# insert puts an item at a chosen index; later items shift right.
marks.insert(0, 100)
print("after insert(0, 100):", marks)

# Removing items: by value with remove, by index with pop.
marks.remove(45)
highest = marks.pop(0)
print("after remove(45) and pop(0):", marks, "| popped:", highest)

# Searching and counting.
print("index of 88:", marks.index(88))
print("how many 70s:", marks.count(70))
print("is 92 in marks?", 92 in marks)

# A nested list stores a table: one inner list per row.
timetable = [
    ["Mon", "Maths", "Science"],
    ["Tue", "English", "Maths"],
    ["Wed", "Science", "English"],
]
print("Tuesday:", timetable[1])
print("Tuesday, second period:", timetable[1][2])
for day_row in timetable:
    print(day_row[0], "->", day_row[1:])
