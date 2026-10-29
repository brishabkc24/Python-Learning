"""Count lines, words, characters and vowels in datasets/sample_text.txt.

Run: python 05_count_text_file.py
The dataset is found relative to this file, so any working directory works.
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

# read_text() returns the whole file as one string. File handling is
# explained fully in its own topic; here we only need the text.
text = (DATA_DIR / "sample_text.txt").read_text(encoding="utf-8")

print("First 40 characters:", text[:40])
print()

# Each line ends with a newline character, so splitting on it gives lines.
lines = text.strip().split("\n")
print("Lines:", len(lines))

# split() with no argument splits on any run of whitespace.
words = text.split()
print("Words:", len(words))
print("Characters (including spaces and newlines):", len(text))

# Walk through the text one character at a time and count what we meet.
letter_or_digit_count = 0
vowel_count = 0
for character in text:
    if character.isalnum():
        letter_or_digit_count += 1
    if character.lower() in "aeiou":
        vowel_count += 1
print("Characters (letters and digits only):", letter_or_digit_count)
print("Vowels:", vowel_count)

# How often does the word "Python" appear?
print("Mentions of 'Python':", text.count("Python"))

# The longest word, with punctuation stripped off the ends.
longest = ""
for word in words:
    word = word.strip(".,")
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest, "with", len(longest), "letters")
