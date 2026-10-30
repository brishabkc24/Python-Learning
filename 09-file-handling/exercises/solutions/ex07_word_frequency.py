"""Print the five most common words in datasets/sample_text.txt, ignoring case and punctuation."""

from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    text = file.read().lower()

# Remove punctuation so "language." and "language" count as the same word.
for mark in ".,":
    text = text.replace(mark, "")

counter = Counter(text.split())
for word, count in counter.most_common(5):
    print(f"{word}: {count}")
