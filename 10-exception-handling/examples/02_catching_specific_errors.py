"""
Demonstrates catching specific exceptions: several except blocks, a tuple
of exceptions in one except, and "as error" to read the error message.
Run: python 02_catching_specific_errors.py
"""


def describe(value, index):
    """Convert value to int, divide 100 by it, then pick a colour by index."""
    colours = ["red", "green", "blue"]
    try:
        number = int(value)
        share = 100 / number
        colour = colours[index]
        print(f"  share = {share}, colour = {colour}")
    except ValueError:
        print(f"  {value!r} cannot be converted to a whole number")
    except ZeroDivisionError:
        print("  the number is zero, so 100 cannot be divided by it")
    except IndexError as error:
        print("  bad index:", error)


print("Several except blocks, one for each kind of problem:")
describe("4", 1)
describe("four", 1)
describe("0", 1)
describe("4", 7)


def to_number(value):
    """Turn value into a float, or return 0.0 if that is impossible."""
    try:
        return float(value)
    except (ValueError, TypeError) as error:
        print(f"  Could not convert {value!r}: {error}")
        return 0.0


print("One except block for a tuple of exceptions:")
for value in ["3.5", "abc", None]:
    print("  result:", to_number(value))
