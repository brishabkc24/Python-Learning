"""
Demonstrates the four ways to read a text file: read(), readline(),
readlines() and looping line by line, plus strip() to remove the newline.
Run: python 02_reading_methods.py
Reads datasets/sample_text.txt.
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
TEXT_FILE = DATA_DIR / "sample_text.txt"

# read() returns the whole file as one string.
with open(TEXT_FILE, encoding="utf-8") as file:
    whole_text = file.read()
print("read() gave", len(whole_text), "characters")

# readline() returns one line each time it is called.
with open(TEXT_FILE, encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
print("First line :", first_line.strip())
print("Second line:", second_line.strip())

# readlines() returns a list with one string per line.
with open(TEXT_FILE, encoding="utf-8") as file:
    all_lines = file.readlines()
print("readlines() gave", len(all_lines), "lines")
print("Last line, newline included:", repr(all_lines[-1]))

# Looping over the file is the simplest way to read line by line.
# Each line still ends with "\n", so strip() removes it before printing.
print("Lines with their numbers:")
with open(TEXT_FILE, encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")
