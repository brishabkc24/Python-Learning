"""
Keeps asking until the user types a valid whole number, by wrapping int()
in try/except inside a loop.
Run: python 07_valid_integer_input.py
Sample session:
    Enter your age: abc
    That is not a whole number, try again.
    Enter your age: 12
    You are 12 years old.
"""


def ask_for_integer(prompt):
    while True:
        answer = input(prompt)
        try:
            return int(answer)        # a valid number ends the loop
        except ValueError:
            print("That is not a whole number, try again.")


age = ask_for_integer("Enter your age: ")
print(f"You are {age} years old.")
