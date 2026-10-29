"""Use for loops with range(), strings and lists, plus enumerate() and zip().

Run: python 01_for_and_range.py
"""

# range(stop) counts from 0 up to, but not including, stop.
print("range(5):")
for number in range(5):
    print(number, end=" ")
print()

# range(start, stop) begins at start.
print("range(1, 6):")
for number in range(1, 6):
    print(number, end=" ")
print()

# range(start, stop, step) jumps by step. A negative step counts down.
print("range(0, 20, 5):")
for number in range(0, 20, 5):
    print(number, end=" ")
print()
print("range(10, 0, -2):")
for number in range(10, 0, -2):
    print(number, end=" ")
print()

print()

# A for loop over a string visits each character.
for letter in "abc":
    print("Letter:", letter)

# A for loop over a list visits each item in order.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

print()

# enumerate() gives the position together with the item, so there is no
# need for a separate counter variable. Positions start at 0 by default.
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

print()

# zip() walks through two sequences side by side.
names = ["Asha", "Ravi", "Meera"]
marks = [88, 72, 95]
for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")

# The loop variable keeps its last value after the loop ends.
print()
print("Last value of number:", number)
