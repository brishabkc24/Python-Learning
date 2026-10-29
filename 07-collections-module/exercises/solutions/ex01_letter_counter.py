"""Exercise 1: count the letters in a word with Counter and show the three most common."""

from collections import Counter

letters = Counter("programming")
print(letters)
print("Top three:", letters.most_common(3))
