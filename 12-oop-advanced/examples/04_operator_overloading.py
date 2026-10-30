"""Make +, ==, < and len() work on a Vector class, then mimic overloading.

Dunder methods such as __add__ and __lt__ let operators act on your
own objects. The last part shows that Python keeps only the last
definition of a method, and that default arguments and *args are the
way to accept different inputs. Run: python 04_operator_overloading.py
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):                    # a + b
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):                    # a - b
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):                   # a * 3
        return Vector(self.x * number, self.y * number)

    def __eq__(self, other):                     # a == b
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):                     # a < b, compares lengths
        return self.length() < other.length()

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


a = Vector(2, 3)
b = Vector(1, 1)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * 3  =", a * 3)
print("a == b ?", a == b)
print("a == Vector(2, 3) ?", a == Vector(2, 3))
print("b < a  ?", b < a)
print("Longest of several:", max(a, b, Vector(5, 5)))   # max() relies on __lt__
print("Sorted by length:", sorted([a, Vector(5, 5), b]))


class Greeter:
    def hello(self):
        return "Hello!"

    def hello(self, name):                       # replaces the version above
        return f"Hello, {name}"


print("\nPython keeps only the last definition of hello():")
print(Greeter().hello("Sita"))
try:
    Greeter().hello()
except TypeError as error:
    print("Error:", error)


class FlexibleGreeter:
    def hello(self, name="friend", *extra_names):     # defaults and *args instead
        names = ", ".join((name,) + extra_names)
        return f"Hello, {names}"


print("\nOne method that accepts many argument counts:")
flexible = FlexibleGreeter()
print(flexible.hello())
print(flexible.hello("Sita"))
print(flexible.hello("Sita", "Aarav", "Priya"))
