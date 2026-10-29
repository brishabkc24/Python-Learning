"""
Import the greetings module that lives next to this file and use its
functions and constant in three different import styles.

Run from this folder: python 02_use_greetings.py
"""

# Style 1: the module name becomes a prefix.
import greetings

print(greetings.hello("Sita"))
print(greetings.goodbye())
print("default name:", greetings.DEFAULT_NAME)

# Style 2: an alias for the module.
import greetings as g

print(g.hello("Aarav"))

# Style 3: import a single name.
from greetings import goodbye

print(goodbye("Bikash"))

# The module was loaded once; every style refers to the same object.
print("same module object?", greetings is g)
print("module file:", greetings.__file__.split("\\")[-1].split("/")[-1])
