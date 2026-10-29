"""Find the greatest of three numbers in three different ways.

Run: python 03_greatest_of_three.py
"""

first = 42
second = 97
third = 65
print(f"Numbers: {first}, {second}, {third}")

# Way 1: compare each number with the other two using and.
if first >= second and first >= third:
    greatest = first
elif second >= first and second >= third:
    greatest = second
else:
    greatest = third
print("Greatest (and):", greatest)

# Way 2: keep a running "best so far" and replace it when a bigger one
# turns up. This pattern scales to any number of values.
greatest = first
if second > greatest:
    greatest = second
if third > greatest:
    greatest = third
print("Greatest (running best):", greatest)

# Way 3: the built-in max() does the same job in one line.
print("Greatest (max()):", max(first, second, third))

# The smallest works the same way with < and min().
smallest = first
if second < smallest:
    smallest = second
if third < smallest:
    smallest = third
print("Smallest (running best):", smallest)
print("Smallest (min()):", min(first, second, third))
