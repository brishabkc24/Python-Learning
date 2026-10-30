"""Call the same method name on different objects and get different results.

Circle, Rectangle and Square all answer area() and perimeter() in their
own way, so one loop handles them all. The second part shows duck
typing: any object with a describe() method fits, parent or not.
Run: python 03_polymorphism_shapes.py
"""

import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        # Written once here, but it calls whichever area() the object has.
        name = type(self).__name__
        print(f"{name:<10} area {self.area():8.2f}   perimeter {self.perimeter():7.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Song:                              # not a Shape, but it has describe()
    def __init__(self, title):
        self.title = title

    def describe(self):
        print(f"Song       '{self.title}' (not a shape at all)")


shapes = [Circle(1.5), Rectangle(3, 4), Square(5)]
for shape in shapes:
    shape.describe()

total_area = sum(shape.area() for shape in shapes)
print(f"\nTotal area of all shapes: {total_area:.2f}")
largest = max(shapes, key=lambda shape: shape.area())
print("Largest shape:", type(largest).__name__)

print("\nDuck typing: anything with describe() works in the same loop")
for thing in [Square(2), Song("Morning Walk")]:
    thing.describe()
