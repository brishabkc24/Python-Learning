"""Draw star patterns with nested loops: a right triangle, an inverted
triangle and a pyramid.

Run: python 03_star_patterns.py
"""

rows = 5

# Right triangle: row 1 has one star, row 2 has two, and so on.
# The outer loop picks the row; the inner loop prints that many stars.
print("Right triangle")
for row in range(1, rows + 1):
    for star in range(row):
        print("*", end="")
    print()          # move to the next line after each row

print()

# The same triangle without an inner loop: "*" * row repeats the star.
print("Right triangle with string repetition")
for row in range(1, rows + 1):
    print("*" * row)

print()

# Inverted triangle: start with all the stars and lose one per row.
print("Inverted triangle")
for row in range(rows, 0, -1):
    print("*" * row)

print()

# Pyramid: each row needs some spaces first, then an odd number of stars.
# Row 1 of 5 has 4 spaces and 1 star; row 5 has 0 spaces and 9 stars.
print("Pyramid")
for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)

print()

# Number triangle: a nested loop can print values, not only stars.
print("Number triangle")
for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()
