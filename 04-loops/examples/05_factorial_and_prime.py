"""Calculate a factorial with a loop and check whether a number is prime
using a loop with break and else.

Run: python 05_factorial_and_prime.py
"""

# Factorial: n! = 1 * 2 * 3 * ... * n. Start the product at 1, not 0,
# because multiplying by 0 would wipe everything out.
n = 6
factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(f"{n}! = {factorial}")

# 0! is defined as 1. The loop body never runs, so the answer is the
# starting value, which is exactly why we started at 1.
n = 0
factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(f"{n}! = {factorial}")

print()

# Prime check: a prime has no divisors other than 1 and itself.
# Try every candidate from 2 up to the number - 1. The first one that
# divides exactly proves the number is not prime, so break out.
# If the loop finishes without a break, the else block runs: it is prime.
candidate = 29
if candidate < 2:
    print(candidate, "is not prime")
else:
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            print(f"{candidate} is not prime ({divisor} x {candidate // divisor})")
            break
    else:
        print(candidate, "is prime")

candidate = 91
if candidate < 2:
    print(candidate, "is not prime")
else:
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            print(f"{candidate} is not prime ({divisor} x {candidate // divisor})")
            break
    else:
        print(candidate, "is prime")

print()

# All primes up to 30, using the same idea inside an outer loop.
print("Primes up to 30:", end=" ")
for candidate in range(2, 31):
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            break
    else:
        print(candidate, end=" ")
print()
