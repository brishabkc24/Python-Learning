"""
sorted() versus .sort(), and copying a list versus sharing it (aliasing).
Shows the classic bug where two names point at the same list, and how
copy.deepcopy handles nested lists.

Run: python 02_sort_and_copy.py
"""

import copy

marks = [67, 92, 45, 85]

# sorted() returns a NEW list and leaves the original alone.
ordered = sorted(marks)
print("sorted(marks):", ordered)
print("marks after sorted():", marks)

# .sort() changes the list in place and returns None.
returned = marks.sort()
print("marks.sort() returned:", returned)
print("marks after .sort():", marks)

print("descending:", sorted(marks, reverse=True))
words = ["banana", "Fig", "apple"]
print("by length:", sorted(words, key=len))
print("ignoring case:", sorted(words, key=str.lower))

# Aliasing: assignment does not copy a list.
team_a = ["Sita", "Aarav"]
team_b = team_a
team_b.append("Kiran")
print("team_a:", team_a, "| team_b:", team_b)
print("same list object?", team_a is team_b)

# A real copy is independent.
team_c = team_a.copy()
team_c.append("Maya")
print("team_a:", team_a, "| team_c:", team_c)
print("same list object?", team_a is team_c)

# .copy() is shallow: inner lists are still shared.
groups = [["Sita"], ["Aarav"]]
shallow = groups.copy()
shallow[0].append("Kiran")
print("groups after changing shallow[0]:", groups)

# deepcopy copies the inner lists as well.
deep = copy.deepcopy(groups)
deep[1].append("Maya")
print("groups after changing deep[1]:", groups)
print("deep:", deep)
