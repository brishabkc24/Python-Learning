"""Reverse the digits of a whole number with arithmetic in a while loop,
and count and sum its digits the same way.

Run: python 06_reverse_digits.py
"""

number = 12345
print("Number:", number)

# number % 10 gives the last digit; number // 10 drops it.
# Each round moves one digit from the end of number to the end of reversed.
remaining = number
reversed_number = 0
while remaining > 0:
    last_digit = remaining % 10
    reversed_number = reversed_number * 10 + last_digit
    remaining = remaining // 10
    print(f"  took {last_digit}, reversed so far {reversed_number}, remaining {remaining}")
print("Reversed:", reversed_number)

print()

# The same loop shape counts and sums the digits.
remaining = number
digit_count = 0
digit_sum = 0
while remaining > 0:
    digit_sum += remaining % 10
    digit_count += 1
    remaining //= 10
print("Digits:", digit_count)
print("Sum of digits:", digit_sum)

print()

# Reversing is also how you test whether a number is a palindrome.
number = 12321
remaining = number
reversed_number = 0
while remaining > 0:
    reversed_number = reversed_number * 10 + remaining % 10
    remaining //= 10
print(f"{number} reversed is {reversed_number}; palindrome: {number == reversed_number}")

# Trailing zeros disappear, because 0 cannot lead a number.
number = 1200
remaining = number
reversed_number = 0
while remaining > 0:
    reversed_number = reversed_number * 10 + remaining % 10
    remaining //= 10
print(f"{number} reversed is {reversed_number}")
