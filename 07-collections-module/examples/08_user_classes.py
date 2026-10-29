"""
UserDict, UserList and UserString: containers with one rule changed.
A dictionary with upper-case keys, a list that validates what is added,
and a string that always strips surrounding spaces. The class keyword is
explained in OOP Basics; here each class changes only one or two methods.

Run: python 08_user_classes.py
"""

from collections import UserDict, UserList, UserString


class UpperKeyDict(UserDict):
    """A dictionary whose keys are always stored in upper case."""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.upper())

    def __contains__(self, key):
        return super().__contains__(key.upper())


class PositiveList(UserList):
    """A list that accepts only positive numbers."""

    def append(self, item):
        if not isinstance(item, (int, float)) or item <= 0:
            print("  rejected:", repr(item))
            return
        super().append(item)

    def extend(self, items):
        for item in items:
            self.append(item)       # reuse the check above


class CleanString(UserString):
    """A string with the spaces around it removed."""

    def __init__(self, text):
        super().__init__(str(text).strip())


config = UpperKeyDict()
config["theme"] = "dark"
config["Font_Size"] = 14
print("config:", config)
print("lookup in any case:", config["THEME"], config["theme"], config["Theme"])
print("'font_size' in config:", "font_size" in config)

print()
prices = PositiveList()
prices.append(120)
prices.append(-5)
prices.append("free")
prices.extend([45.5, 0, 80])
print("prices:", prices, "| total:", sum(prices))

print()
city = CleanString("   Pokhara   ")
print("repr:", repr(city), "| length:", len(city))
print("methods still work:", city.upper(), city.startswith("Pok"))
print("joined:", city + " Valley")
