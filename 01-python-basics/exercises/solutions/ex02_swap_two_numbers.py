"""Swap the values of a and b without typing the numbers again."""

a = 5
b = 10
print(f"Before: a = {a}, b = {b}")

# Python can assign two names at once, so no temporary variable is needed.
a, b = b, a
print(f"After: a = {a}, b = {b}")
