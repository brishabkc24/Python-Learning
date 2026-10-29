"""Read the length and width of a rectangle and print its area and perimeter."""

length = float(input("Length: "))
width = float(input("Width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
