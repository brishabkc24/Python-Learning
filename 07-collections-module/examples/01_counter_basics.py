"""
Counter: count items in a list or letters in a string, read the count of
a missing item, find the most common items, and add or subtract counts.

Run: python 01_counter_basics.py
"""

from collections import Counter

votes = ["tea", "coffee", "tea", "juice", "tea", "coffee"]
vote_counts = Counter(votes)
print("votes:", vote_counts)
print("tea:", vote_counts["tea"])
print("water (never voted for):", vote_counts["water"])
print("winner:", vote_counts.most_common(1)[0][0])
print("ranked:", vote_counts.most_common())

# Counter also counts the characters of a string.
letters = Counter("mississippi")
print("letters:", letters)
print("total letters:", letters.total())
print("different letters:", len(letters))

# update adds more items; subtract takes them away.
vote_counts.update(["juice", "juice", "water"])
print("after more votes:", vote_counts)
vote_counts.subtract(["tea"])
print("after one tea vote is withdrawn:", vote_counts)

# Two counters can be added together.
morning = Counter(tea=3, coffee=1)
evening = Counter(tea=1, coffee=4)
print("whole day:", morning + evening)

# elements() repeats each item as many times as it was counted.
print("elements():", sorted(morning.elements()))

# The same count with a plain dictionary needs a loop.
manual_count = {}
for drink in votes:
    manual_count[drink] = manual_count.get(drink, 0) + 1
print("manual count:", manual_count)
