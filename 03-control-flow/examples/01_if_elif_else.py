"""Use if, if-else and if-elif-else to make decisions about numbers.

Run: python 01_if_elif_else.py
"""

# A plain if: the indented block runs only when the condition is True.
temperature = 31
if temperature > 30:
    print("It is hot today.")
print("This line always runs.")

print()

# if-else: exactly one of the two blocks runs.
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print()

# if-elif-else: Python tests the conditions from the top and runs the
# first block whose condition is True, then skips the rest.
marks = 67
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

print()

# The order of the conditions matters. Try the same marks with the tests
# written the other way round and the first True branch is the wrong one.
if marks >= 40:
    print("Wrong order: Grade C")      # 67 >= 40 is True, so this runs
elif marks >= 60:
    print("Wrong order: Grade B")      # never reached for 67

print()

# A sign check with three branches.
value = 0
if value > 0:
    print("positive")
elif value < 0:
    print("negative")
else:
    print("zero")
