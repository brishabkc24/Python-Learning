"""
Demonstrates infinite generators: a generator can run forever, so the
caller must stop with break or take only a fixed number of values.
Run: python 05_infinite_generators.py
"""


def natural_numbers():
    number = 1
    while True:                 # never ends on its own
        yield number
        number += 1


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("First number whose square is above 50:")
for n in natural_numbers():
    if n * n > 50:
        print("  ", n, "squared is", n * n)
        break               # without break this loop would never end

print("Fibonacci numbers below 100:")
small = []
for value in fibonacci():
    if value >= 100:
        break
    small.append(value)
print("  ", small)

# Taking exactly five values by hand.
gen = natural_numbers()
first_five = [next(gen) for _ in range(5)]
print("First five natural numbers:", first_five)
print("The generator continues from where it stopped:", next(gen))
