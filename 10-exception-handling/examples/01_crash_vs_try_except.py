"""
Demonstrates what happens when an error is not handled (the program stops)
and how try/except keeps the program running, using a safe division
function as the example.
Run: python 01_crash_vs_try_except.py
"""


def divide_without_protection(a, b):
    return a / b


def divide_safely(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  Cannot divide {a} by zero")
        return None
    return result


print("Working division:", divide_without_protection(10, 2))

# Calling divide_without_protection(10, 0) on its own would raise
# ZeroDivisionError and stop the whole program with a traceback.
# Here the call is wrapped in try/except so that the script can continue.
try:
    divide_without_protection(10, 0)
except ZeroDivisionError as error:
    print("Unprotected call raised:", error)

print("Safe division examples:")
pairs = [(10, 2), (7, 0), (9, 3)]
for a, b in pairs:
    print(f"  {a} / {b} =", divide_safely(a, b))

print("The program reached the end")
