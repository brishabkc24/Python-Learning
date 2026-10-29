"""Add up the digits of a whole number using % and // in a while loop."""

number = 4521

remaining = number
digit_sum = 0
while remaining > 0:
    digit_sum += remaining % 10     # the last digit
    remaining //= 10                # drop the last digit

print(f"Sum of the digits of {number} is {digit_sum}")
