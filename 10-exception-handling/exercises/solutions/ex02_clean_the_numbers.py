"""Convert a list of strings to integers, adding up the valid ones and collecting the rest."""

values = ["10", "20", "abc", "30", "", "4.5"]

total = 0
rejected = []
for value in values:
    try:
        total += int(value)
    except ValueError:
        rejected.append(value)

print("Sum of valid numbers:", total)
print("Rejected:", rejected)
