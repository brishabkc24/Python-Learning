"""
Recursion: factorial and Fibonacci written as functions that call
themselves, with the base case explained and the calls traced on screen.

Run: python 06_recursion.py
"""


def factorial(n, depth=0):
    """Return n! and print each call so the recursion is visible."""
    indent = "  " * depth
    print(indent + "factorial(" + str(n) + ") called")
    if n == 0:
        # Base case: the answer is known, so no further call is made.
        print(indent + "base case reached, returning 1")
        return 1
    # Recursive case: solve a smaller problem and build on its answer.
    result = n * factorial(n - 1, depth + 1)
    print(indent + "factorial(" + str(n) + ") returns " + str(result))
    return result


print("5! =", factorial(5))
print()


def fibonacci(n):
    """Return the n-th Fibonacci number: 0, 1, 1, 2, 3, 5, 8, ..."""
    if n <= 1:
        # Two base cases: fibonacci(0) is 0 and fibonacci(1) is 1.
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


sequence = []
for position in range(12):
    sequence.append(fibonacci(position))
print("First 12 Fibonacci numbers:", sequence)


def sum_digits(number):
    """Add up the digits of a positive integer, recursively."""
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


print("Sum of digits of 4729:", sum_digits(4729))
