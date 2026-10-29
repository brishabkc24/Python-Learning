"""Classic counting loops: print 1 to 20, even numbers, the sum of the
first n natural numbers, the sum of odd numbers up to 30 and a
multiplication table.

Run: python 04_sums_and_tables.py
"""

# Print 1 to 20 on one line. end=" " keeps them on the same line.
print("1 to 20:")
for number in range(1, 21):
    print(number, end=" ")
print()

# Even numbers: step by 2 starting from 2.
print("Even numbers up to 20:")
for number in range(2, 21, 2):
    print(number, end=" ")
print()

print()

# Sum of the first n natural numbers: keep a running total. The variable
# total starts at 0 and grows by each number in turn. This "accumulator"
# pattern appears in almost every program.
n = 10
total = 0
for number in range(1, n + 1):
    total += number
print(f"Sum of 1 to {n}: {total}")
print(f"Check with the formula n * (n + 1) / 2: {n * (n + 1) // 2}")

# Sum of odd numbers up to 30: use the step of range() to pick odd numbers.
odd_total = 0
for number in range(1, 31, 2):
    odd_total += number
print(f"Sum of odd numbers up to 30: {odd_total}")

# The same sum with a while loop and a test for oddness.
odd_total = 0
number = 1
while number <= 30:
    if number % 2 == 1:
        odd_total += number
    number += 1
print(f"Same sum using while: {odd_total}")

print()

# Multiplication table. The width spec :2 lines up the numbers.
table_of = 7
print(f"Multiplication table of {table_of}")
for multiplier in range(1, 11):
    print(f"{table_of} x {multiplier:2} = {table_of * multiplier:2}")
