"""Store a few values in variables and print them with labels.

Run: python 02_print_variables.py
"""

# A variable is a name that refers to a value, like a label on a box.
# The value goes on the right of the = sign, the name on the left.
language = "Python"
version = 3.13
year_created = 1991
is_beginner_friendly = True

# A label before each value makes the output explain itself.
print("Language:", language)
print("Version:", version)
print("Created in:", year_created)
print("Beginner friendly:", is_beginner_friendly)

# A variable can be given a new value at any time.
language = "Python 3"
print("Updated language:", language)

# Variables can be used in calculations before printing.
minutes_per_hour = 60
hours_per_day = 24
minutes_per_day = minutes_per_hour * hours_per_day
print("Minutes in a day:", minutes_per_day)
