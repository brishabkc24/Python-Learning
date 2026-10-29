"""Print a 5-row triangle where row n shows the numbers 1 to n."""

rows = 5

for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()
