"""Exercise 2: pick parts of a list of 1 to 10 using slices only."""

numbers = list(range(1, 11))

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Every second:", numbers[::2])
print("Reversed:", numbers[::-1])
