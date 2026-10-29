"""Ask for the user's name and print a personal greeting.

Run: python 03_greeting_input.py

Sample session:
    What is your name? Asha
    Hello, Asha! Welcome to Python.
    Your name has 4 letters.
"""

# input() shows the message, waits for the user to type and press Enter,
# then gives back what was typed as text.
name = input("What is your name? ")

# The + sign joins pieces of text together.
print("Hello, " + name + "! Welcome to Python.")

# len() counts the characters in a piece of text.
print("Your name has", len(name), "letters.")
