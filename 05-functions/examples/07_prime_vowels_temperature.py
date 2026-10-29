"""
Three small reusable functions with docstrings and type hints:
check whether a number is prime, count the vowels in a text, and convert
Celsius to Fahrenheit. Each is tested with a few values.

Run: python 07_prime_vowels_temperature.py
"""


def is_prime(number: int) -> bool:
    """Return True if number is a prime (divisible only by 1 and itself)."""
    if number < 2:
        return False
    # Checking up to the square root is enough to find any divisor.
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def count_vowels(text: str) -> int:
    """Return how many vowels (a, e, i, o, u) appear in text."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count = count + 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


print("Primes between 1 and 30:")
for candidate in range(1, 31):
    if is_prime(candidate):
        print(candidate, end=" ")
print()

print()
for phrase in ["Programming", "Python is fun", "rhythm"]:
    print("Vowels in", repr(phrase) + ":", count_vowels(phrase))

print()
for celsius in [0, 25, 37, 100]:
    print(celsius, "C =", celsius_to_fahrenheit(celsius), "F")

print()
print("help() shows the docstring of our own function:")
help(count_vowels)
