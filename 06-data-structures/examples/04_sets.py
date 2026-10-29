"""
Sets: removing duplicates, membership tests, add/remove/discard and the
set operations (union, intersection, difference, symmetric difference)
as both methods and operators.

Run: python 04_sets.py
"""

# A set keeps only one copy of each item.
votes = ["tea", "coffee", "tea", "juice", "coffee", "tea"]
unique_drinks = set(votes)
print("votes:", votes)
print("unique drinks:", sorted(unique_drinks))
print("how many different drinks:", len(unique_drinks))

# add, remove, discard
unique_drinks.add("water")
unique_drinks.add("tea")            # already present: no change
unique_drinks.discard("milk")       # not present: no error
unique_drinks.remove("juice")       # present, so no error
print("after changes:", sorted(unique_drinks))
print("is 'tea' there?", "tea" in unique_drinks)
print("is 'juice' there?", "juice" in unique_drinks)

# Set operations on two classes of students.
maths_club = {"Sita", "Aarav", "Bikash", "Priya"}
science_club = {"Bikash", "Priya", "Kiran", "Maya"}

print("in either club:", sorted(maths_club | science_club))
print("in both clubs:", sorted(maths_club & science_club))
print("only maths:", sorted(maths_club - science_club))
print("only science:", sorted(science_club - maths_club))
print("in exactly one club:", sorted(maths_club ^ science_club))

# The methods do the same as the operators.
print("union matches:", maths_club.union(science_club) == maths_club | science_club)
print("intersection matches:", maths_club.intersection(science_club) == maths_club & science_club)

# Subset and superset.
committee = {"Sita", "Priya"}
print("committee all in maths club?", committee.issubset(maths_club))
print("maths club contains committee?", maths_club.issuperset(committee))
print("committee all in science club?", committee <= science_club)

# frozenset: a set that cannot change, so it can be a dict key or a set member.
weekend = frozenset(["Sat", "Sun"])
print("weekend:", sorted(weekend), "| type:", type(weekend).__name__)
