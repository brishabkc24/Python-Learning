"""Exercise 2: group words by their first letter with a defaultdict of lists."""

from collections import defaultdict

words = ["apple", "avocado", "banana", "blueberry", "cherry"]

groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)

for letter, grouped_words in groups.items():
    print(letter, "->", grouped_words)
