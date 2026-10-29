"""Create variables of each basic type and inspect them with type().

Run: python 01_variables_and_types.py
"""

# One variable of each basic type. The name describes what the box holds.
student_name = "Asha"        # str: text inside quotes
student_age = 21             # int: a whole number
student_height = 1.62        # float: a number with a decimal point
is_enrolled = True           # bool: True or False
middle_name = None           # None: no value yet

print("Name:", student_name, "->", type(student_name))
print("Age:", student_age, "->", type(student_age))
print("Height:", student_height, "->", type(student_height))
print("Enrolled:", is_enrolled, "->", type(is_enrolled))
print("Middle name:", middle_name, "->", type(middle_name))

print()

# The same name can be reassigned, even to a value of a different type.
# This works, but it makes code hard to follow, so avoid it in real programs.
score = 90
print("score is", score, "->", type(score))
score = "ninety"
print("score is now", score, "->", type(score))

print()

# Python is case sensitive: these are three different variables.
total = 1
Total = 2
TOTAL = 3
print("total, Total, TOTAL =", total, Total, TOTAL)

# Digits in quotes are text, not a number. 7 + "7" would be an error.
digits = "7"
print("digits + digits =", digits + digits)
print("7 + 7 =", 7 + 7)
