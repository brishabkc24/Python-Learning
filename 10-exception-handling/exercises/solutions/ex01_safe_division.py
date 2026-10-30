"""Write safe_divide(a, b) that returns None and prints a message when b is zero."""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None


for a, b in [(10, 2), (5, 0), (9, 3)]:
    print(f"{a} / {b} =", safe_divide(a, b))
