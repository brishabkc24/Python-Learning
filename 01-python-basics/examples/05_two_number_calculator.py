"""Read two numbers and print the result of every arithmetic operator.

Run: python 05_two_number_calculator.py

Sample session:
    Enter the first number: 9
    Enter the second number: 4
    9.0 + 4.0 = 13.0
    9.0 - 4.0 = 5.0
    9.0 * 4.0 = 36.0
    9.0 / 4.0 = 2.25
    9.0 // 4.0 = 2.0
    9.0 % 4.0 = 1.0
    9.0 ** 4.0 = 6561.0
"""

# float() accepts both "9" and "9.5", so it is the safer choice here.
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} * {second} = {first * second}")

# Dividing by zero is an error, so check before dividing.
if second == 0:
    print("Cannot divide by zero.")
else:
    print(f"{first} / {second} = {first / second}")
    print(f"{first} // {second} = {first // second}")
    print(f"{first} % {second} = {first % second}")

print(f"{first} ** {second} = {first ** second}")
