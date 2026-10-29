"""A simple menu calculator that uses match-case to pick the operation.

Run: python 06_menu_calculator.py

Sample session:
    First number: 10
    Second number: 4
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    Choose an option (1-4): 4
    10.0 / 4.0 = 2.5
"""

first = float(input("First number: "))
second = float(input("Second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Choose an option (1-4): ")

# match compares the value against each case in order and runs the first
# one that fits. case _ is the catch-all for anything else. The choice is
# compared as text because input() returns a string.
match choice:
    case "1":
        print(f"{first} + {second} = {first + second}")
    case "2":
        print(f"{first} - {second} = {first - second}")
    case "3":
        print(f"{first} * {second} = {first * second}")
    case "4":
        # Dividing by zero would crash, so guard it with an if.
        if second == 0:
            print("Cannot divide by zero.")
        else:
            print(f"{first} / {second} = {first / second}")
    case _:
        print("Unknown option:", choice)
