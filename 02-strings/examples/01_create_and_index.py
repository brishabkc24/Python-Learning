"""Create strings with the three kinds of quotes and pick out single
characters with positive and negative indexes.

Run: python 01_create_and_index.py
"""

# Single and double quotes give the same result. Pick the one that lets you
# avoid escaping: a string containing an apostrophe is easier in double quotes.
city = 'Kathmandu'
sentence = "It's a sunny day."
print(city)
print(sentence)

# Triple quotes keep line breaks, so they suit text that spans several lines.
address = """Flat 3
Lake Road
Pokhara"""
print(address)

print()

# Each character has a position called its index. Counting starts at 0.
language = "Python"
print("Word:", language)
print("Index 0:", language[0])
print("Index 1:", language[1])
print("Index 5:", language[5])

# Negative indexes count from the end: -1 is the last character.
print("Index -1:", language[-1])
print("Index -2:", language[-2])

# len() gives the number of characters, so the last index is len - 1.
print("Length:", len(language))
print("Last character using len():", language[len(language) - 1])

# A string of digits is still text. Indexing gives a one-character string.
pin = "4729"
print("First digit of the pin:", pin[0], type(pin[0]))
