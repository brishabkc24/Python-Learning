"""Rectangle class with area(), perimeter() and is_square() methods."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def show(self):
        print(f"Rectangle {self.width} x {self.height}: area {self.area()}, "
              f"perimeter {self.perimeter()}, square? {self.is_square()}")


Rectangle(4, 6).show()
Rectangle(5, 5).show()
