"""Read three numbers and print the smallest using if statements."""

first = float(input("First number: "))
second = float(input("Second number: "))
third = float(input("Third number: "))

# Start by assuming the first is smallest, then let the others challenge it.
smallest = first
if second < smallest:
    smallest = second
if third < smallest:
    smallest = third

print("Smallest:", smallest)
