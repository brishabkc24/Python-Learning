"""
Count how often each word appears in datasets/words.txt with Counter and
show the result as a small text bar chart.

Run: python 02_count_words_in_file.py
"""

from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

words = []
with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip().lower()
        if word:                      # skip any blank line
            words.append(word)

word_counts = Counter(words)

print("words in the file:", len(words))
print("different words:", len(word_counts))
print("top three:", word_counts.most_common(3))
print()

# most_common() with no argument lists every word, highest count first.
for word, count in word_counts.most_common():
    print(word.ljust(12), "#" * count, count)
print()

once = [word for word, count in word_counts.items() if count == 1]
print("words that appear only once:", sorted(once))
print("share of 'python':", round(word_counts["python"] / len(words) * 100), "%")
