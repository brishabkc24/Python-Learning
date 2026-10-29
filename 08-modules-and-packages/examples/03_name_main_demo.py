"""
Show what __name__ holds in a script that is run directly and in a
module that is imported, and why the test block in greetings.py stays
silent on import.

Run from this folder: python 03_name_main_demo.py
Then compare with: python greetings.py
"""

print("Before the import.")

import greetings

print("After the import: nothing was printed by greetings.py,")
print("because its __name__ was", repr(greetings.__name__), "not '__main__'.")
print()
print("This script's __name__ is", repr(__name__))


def main():
    """The script's own work, kept in a function so it can be reused."""
    print("Running the main part of", __name__)
    print(greetings.hello("Sita"))


if __name__ == "__main__":
    main()
