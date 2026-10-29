"""Demonstrate the arithmetic, comparison, logical, assignment, membership
and identity operators.

Run: python 03_operators.py
"""

a = 17
b = 5

print("Arithmetic")
print(f"  {a} + {b} = {a + b}")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} / {b} = {a / b}")      # / always gives a float
print(f"  {a} // {b} = {a // b}")    # // drops the remainder
print(f"  {a} % {b} = {a % b}")      # % is the remainder
print(f"  {a} ** {b} = {a ** b}")    # ** is the power

print("Comparison (the answer is always True or False)")
print(f"  {a} == {b} is {a == b}")
print(f"  {a} != {b} is {a != b}")
print(f"  {a} > {b} is {a > b}")
print(f"  {a} <= {b} is {a <= b}")

print("Logical")
is_adult = True
has_ticket = False
print(f"  is_adult and has_ticket -> {is_adult and has_ticket}")
print(f"  is_adult or has_ticket -> {is_adult or has_ticket}")
print(f"  not has_ticket -> {not has_ticket}")

print("Assignment shortcuts")
balance = 100
balance += 50     # same as balance = balance + 50
print(f"  after += 50: {balance}")
balance -= 30
print(f"  after -= 30: {balance}")
balance *= 2
print(f"  after *= 2: {balance}")
balance /= 4
print(f"  after /= 4: {balance}")   # / makes it a float

print("Membership")
word = "python"
print(f"  'y' in 'python' -> {'y' in word}")
print(f"  'z' not in 'python' -> {'z' not in word}")

print("Identity")
nothing = None
print(f"  nothing is None -> {nothing is None}")
# Use == to compare values. Two equal lists are not the same object.
first_list = [1, 2, 3]
second_list = [1, 2, 3]
print(f"  first_list == second_list -> {first_list == second_list}")
print(f"  first_list is second_list -> {first_list is second_list}")
