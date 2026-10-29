"""Print each number from 1 to 10 with its square in two aligned columns."""

for number in range(1, 11):
    # :2 and :4 are widths, so the digits line up on the right.
    print(f"{number:2} {number * number:4}")
