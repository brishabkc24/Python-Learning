"""
Demonstrates extracting data from a text file with findall(): all the
numbers, words and sentences in datasets/sample_text.txt.
Run: python 06_extract_from_text.py
"""

import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
text = (DATA_DIR / "sample_text.txt").read_text(encoding="utf-8")

numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

words = re.findall(r"[A-Za-z]+", text)
print("Word count:", len(words))
print("First ten words:", words[:10])

capitalised = re.findall(r"\b[A-Z][a-z]+\b", text)
print("Capitalised words:", sorted(set(capitalised)))

long_words = re.findall(r"\b\w{10,}\b", text)
print("Words with 10 or more letters:", long_words)

# A sentence is a run of characters that is not a full stop, then a full stop.
sentences = re.findall(r"[^.]+\.", text)
print("Sentence count:", len(sentences))
for number, sentence in enumerate(sentences, start=1):
    print(f"  {number}. {sentence.strip()}")
