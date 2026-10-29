"""Print the first 10 Fibonacci numbers on one line."""

previous = 0
current = 1

for count in range(10):
    print(previous, end=" ")
    # Move both values one step along the sequence.
    previous, current = current, previous + current
print()
