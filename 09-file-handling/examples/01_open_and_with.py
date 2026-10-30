"""
Demonstrates the two ways to open a file: open() followed by close(), and
the with statement, which closes the file for you.
Run: python 01_open_and_with.py
Creates output_notes.txt next to this script.
"""

from pathlib import Path

# Build the path next to this script so it works from any folder.
NOTES_FILE = Path(__file__).resolve().parent / "output_notes.txt"

# Way 1: open(), then remember to close() by hand.
file = open(NOTES_FILE, "w", encoding="utf-8")
file.write("First line, written with open() and close().\n")
file.close()
print("Closed by hand?", file.closed)

# Way 2: the with statement closes the file automatically,
# even if an error happens inside the block.
with open(NOTES_FILE, "a", encoding="utf-8") as file:
    file.write("Second line, written inside a with block.\n")
print("Closed by with?", file.closed)

# Read everything back to prove both lines are there.
with open(NOTES_FILE, encoding="utf-8") as file:
    content = file.read()

print("File name:", NOTES_FILE.name)
print("File content:")
print(content, end="")
