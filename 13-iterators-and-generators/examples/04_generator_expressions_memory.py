"""
Demonstrates generator expressions compared with list comprehensions, and
the memory difference measured with sys.getsizeof. The exact byte counts
can differ a little between computers.
Run: python 04_generator_expressions_memory.py
"""

import sys

squares_list = [n * n for n in range(1000)]      # builds every value now
squares_gen = (n * n for n in range(1000))       # builds values on demand

print("List comprehension type :", type(squares_list).__name__)
print("Generator expression type:", type(squares_gen).__name__)

print("Size of the list     :", sys.getsizeof(squares_list), "bytes")
print("Size of the generator:", sys.getsizeof(squares_gen), "bytes")

# The generator still produces the same values, one at a time.
print("Sum of squares from list     :", sum(squares_list))
print("Sum of squares from generator:", sum(squares_gen))

# A generator can be used only once. After that it is empty.
print("Sum again from the same generator:", sum(squares_gen))

# A much larger range: the list grows, the generator does not.
big_list = [n for n in range(1_000_000)]
big_gen = (n for n in range(1_000_000))
print("One million items as a list     :", sys.getsizeof(big_list), "bytes")
print("One million items as a generator:", sys.getsizeof(big_gen), "bytes")

# A generator expression can be passed straight into a function.
total_even = sum(n for n in range(1, 11) if n % 2 == 0)
print("Sum of even numbers 1 to 10:", total_even)
