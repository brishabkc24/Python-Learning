"""Write three fruit names to output_fruits.txt, then read them back with line numbers."""

from pathlib import Path

FRUITS_FILE = Path(__file__).resolve().parent / "output_fruits.txt"
fruits = ["apple", "banana", "cherry"]

with open(FRUITS_FILE, "w", encoding="utf-8") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open(FRUITS_FILE, encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")
