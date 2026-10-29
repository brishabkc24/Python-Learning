"""Exercise 4: compare two sets of friends with intersection, difference and union."""

sita_friends = {"Aarav", "Bikash", "Priya", "Kiran"}
maya_friends = {"Bikash", "Kiran", "Nabin"}

print("Shared:", sorted(sita_friends & maya_friends))
print("Only Sita:", sorted(sita_friends - maya_friends))
print("Everyone:", sorted(sita_friends | maya_friends))
