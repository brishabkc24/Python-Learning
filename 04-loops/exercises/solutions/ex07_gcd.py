"""Find the greatest common divisor of two numbers with a while loop."""

first = 48
second = 18

a = first
b = second
# Euclid's method: the GCD of (a, b) equals the GCD of (b, a % b).
while b != 0:
    a, b = b, a % b

print(f"GCD of {first} and {second} is {a}")
