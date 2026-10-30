"""
Demonstrates the difference between an iterable and an iterator, the
iter() and next() functions, StopIteration, and what a for loop really
does behind the scenes.
Run: python 01_iter_and_next.py
"""

colours = ["red", "green", "blue"]

# A list is iterable: you can loop over it, but it has no __next__ method.
print("Does a list have __next__?", hasattr(colours, "__next__"))

# iter() creates an iterator from any iterable.
iterator = iter(colours)
print("Does iter(list) have __next__?", hasattr(iterator, "__next__"))

# next() asks the iterator for one item at a time.
print("next ->", next(iterator))
print("next ->", next(iterator))
print("next ->", next(iterator))

# When the items are used up, next() raises StopIteration.
try:
    next(iterator)
except StopIteration:
    print("StopIteration: nothing left")

# This is what a for loop does for you: iter() once, next() until StopIteration.
print("Manual for loop:")
iterator = iter(colours)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print("  item:", item)

# next() can take a default value instead of raising.
empty = iter([])
print("Default value:", next(empty, "no more items"))

# Strings, tuples, dictionaries and files are iterable too.
letters = iter("hi")
print("From a string:", next(letters), next(letters))
