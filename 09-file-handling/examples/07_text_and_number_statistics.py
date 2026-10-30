"""
Practical file programs: copy a file, count lines, words, characters and
vowels in datasets/sample_text.txt, add up datasets/numbers.txt, and work
out the average marks of each student in datasets/marks.txt.
Run: python 07_text_and_number_statistics.py
Creates output_copy.txt next to this script.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

# Part 1: copy a file by reading it and writing the content elsewhere.
with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as source:
    text = source.read()
with open(HERE / "output_copy.txt", "w", encoding="utf-8") as target:
    target.write(text)
print("Copied sample_text.txt to output_copy.txt")

# Part 2: statistics about the text we just read.
line_count = len(text.splitlines())
word_count = len(text.split())
char_count = len(text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

print("sample_text.txt")
print("  lines     :", line_count)
print("  words     :", word_count)
print("  characters:", char_count)
print("  vowels    :", vowel_count)

# Part 3: add up numbers stored one per line.
total = 0
count = 0
with open(DATA_DIR / "numbers.txt", encoding="utf-8") as file:
    for line in file:
        total += int(line)      # int() ignores the surrounding whitespace
        count += 1
print("numbers.txt")
print("  count:", count)
print("  sum  :", total)
print("  mean :", total / count)

# Part 4: average marks per student. Each line is "name m1 m2 m3".
print("marks.txt")
with open(DATA_DIR / "marks.txt", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        name = parts[0]
        marks = [int(value) for value in parts[1:]]
        average = sum(marks) / len(marks)
        print(f"  {name:<8} average {average:.2f}")
