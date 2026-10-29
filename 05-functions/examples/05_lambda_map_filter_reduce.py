"""
Lambda functions used with map, filter, sorted (with a key) and
functools.reduce, applied to a small list of students.

Run: python 05_lambda_map_filter_reduce.py
"""

from functools import reduce

students = [
    ("Aarav", 85),
    ("Sita", 92),
    ("Bikash", 67),
    ("Priya", 78),
    ("Rohan", 45),
]

# A lambda is a one-line function without a name.
get_marks = lambda student: student[1]
print("Marks of the first student:", get_marks(students[0]))

# map applies a function to every item.
names = list(map(lambda student: student[0], students))
print("Names:", names)

# filter keeps only the items for which the function returns True.
passed = list(filter(lambda student: student[1] >= 50, students))
print("Passed:", passed)

# sorted with key sorts by whatever the key function returns.
by_marks = sorted(students, key=lambda student: student[1], reverse=True)
print("Top student:", by_marks[0])
print("By marks:", by_marks)

# key can be any function, not only a lambda.
print("By name length:", sorted(names, key=len))

# reduce combines all items into a single value, two at a time.
all_marks = list(map(get_marks, students))
total_marks = reduce(lambda a, b: a + b, all_marks)
highest = reduce(lambda a, b: a if a > b else b, all_marks)
print("Total marks:", total_marks)
print("Highest marks:", highest)
