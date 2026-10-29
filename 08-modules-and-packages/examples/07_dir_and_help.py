"""
Explore modules with dir() and help(): list the public names of our own
greetings module and of the statistics module, then show the help text
of a function from each.

Run from this folder: python 07_dir_and_help.py
"""

import statistics

import greetings


def public_names(module):
    """Return the names in a module that are not internal (no leading underscore)."""
    return [name for name in dir(module) if not name.startswith("_")]


print("public names in greetings:", public_names(greetings))

stats_names = public_names(statistics)
print("statistics has", len(stats_names), "public names; the first five:", stats_names[:5])

# dir() also works on any object, such as a string.
string_methods = [name for name in dir("") if not name.startswith("_")]
print("a string has", len(string_methods), "methods, for example:", string_methods[:4])

print()
print("help() on our own function:")
help(greetings.hello)

print("help() on a standard library function:")
help(statistics.mean)
