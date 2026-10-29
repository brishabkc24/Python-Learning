"""Print the number of lines, words and characters in sample_text.txt and its longest word."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

text = (DATA_DIR / "sample_text.txt").read_text(encoding="utf-8")

lines = text.strip().split("\n")
words = text.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(text))

longest = ""
for word in words:
    word = word.strip(".,")      # "language." should not count the full stop
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
