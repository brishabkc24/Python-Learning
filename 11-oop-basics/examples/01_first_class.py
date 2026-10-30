"""Define a class, create objects from it and give them starting values.

Shows an empty class that needs pass, the __init__ method that runs
automatically for every new object, and one simple method.
Run: python 01_first_class.py
"""


class EmptyBox:
    pass                                   # a class body cannot be empty, so pass fills it


class Dog:
    def __init__(self, name, age):
        # __init__ runs automatically when Dog(...) is called.
        # It stores the starting values inside the new object.
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old")


box = EmptyBox()
print("An object of an empty class:", type(box).__name__)

buddy = Dog("Buddy", 3)
rex = Dog("Rex", 5)

print("Type of buddy:", type(buddy).__name__)
print("buddy.name:", buddy.name)
print("rex.age:", rex.age)

print("\nCalling the describe() method on each object:")
buddy.describe()
rex.describe()

# Each object keeps its own data: changing rex does not touch buddy.
rex.age = 6
print("\nAfter rex's birthday:")
buddy.describe()
rex.describe()
