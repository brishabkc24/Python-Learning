"""Shape parent with Circle, Rectangle and Triangle children that each override area()."""

import math


class Shape:
    def area(self):
        return 0

    def name(self):
        return type(self).__name__


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 7)]
for shape in shapes:
    print(f"{shape.name():<10} area = {shape.area():.2f}")

print(f"Total area: {sum(shape.area() for shape in shapes):.2f}")
largest = max(shapes, key=lambda shape: shape.area())
print(f"Largest: {largest.name()}")
