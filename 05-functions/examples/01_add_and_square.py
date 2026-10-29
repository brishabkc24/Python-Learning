"""
Define and call two simple functions: add two numbers and square a number.
Shows the difference between a parameter and an argument, and between
returning a value and printing it.

Run: python 01_add_and_square.py
"""


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


def square(number):
    """Return a number multiplied by itself."""
    return number * number


def show_sum(first, second):
    """Print the sum instead of returning it (less reusable)."""
    print(first, "+", second, "=", first + second)


# Calling the functions: 3 and 4 are the arguments.
total = add(3, 4)
print("add(3, 4) returned:", total)

# A returned value can be used in further calculations.
print("add(3, 4) * 10 =", add(3, 4) * 10)
print("square(6) =", square(6))
print("square(add(1, 2)) =", square(add(1, 2)))

# A function that only prints gives back None.
result = show_sum(5, 6)
print("show_sum gave back:", result)

# The same function works for floats and even for strings.
print("add(2.5, 0.5) =", add(2.5, 0.5))
print("add('Py', 'thon') =", add("Py", "thon"))
