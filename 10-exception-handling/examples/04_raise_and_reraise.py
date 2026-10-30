"""
Demonstrates raising exceptions on purpose with raise, re-raising an
exception after logging it, and why a bare except hides real bugs.
Run: python 04_raise_and_reraise.py
"""


def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be a whole number")
    if age < 0 or age > 150:
        raise ValueError(f"age {age} is out of range")
    print("  Age set to", age)


print("Raising our own errors:")
for value in [25, -3, "ten"]:
    try:
        set_age(value)
    except (TypeError, ValueError) as error:
        print("  Rejected:", error)


def load_setting(settings, key):
    try:
        return settings[key]
    except KeyError:
        print(f"  (log) setting {key!r} is missing")
        raise                      # the same KeyError continues upward


print("Re-raising after logging:")
settings = {"theme": "dark"}
try:
    load_setting(settings, "font")
except KeyError as error:
    print("  Caller handled the re-raised error:", error)


def average_bad(values):
    try:
        return sum(values) / len(vlaues)     # deliberate typo: vlaues
    except:                                  # bare except swallows the NameError
        return 0


def average_good(values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:                # only the error we expect
        return 0


print("Why a bare except is bad:")
print("  bare except hid the typo and returned", average_bad([1, 2, 3]))
print("  specific except gives the right answer:", average_good([1, 2, 3]))
print("  specific except on an empty list:", average_good([]))
