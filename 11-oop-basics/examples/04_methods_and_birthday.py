"""Write methods that take parameters, read attributes and change them.

Uses a Student class with default values in __init__, a birthday()
method that adds a year, and a grade() method that reads the marks.
Run: python 04_methods_and_birthday.py
"""


class Student:
    def __init__(self, name, age=18, marks=0):
        self.name = name
        self.age = age
        self.marks = marks

    def birthday(self):
        # Reads the age, adds one and stores it back in the object.
        self.age += 1
        print(f"{self.name} is now {self.age}")

    def add_marks(self, extra):
        # A method with a parameter besides self; marks never pass 100.
        self.marks = min(100, self.marks + extra)

    def grade(self):
        if self.marks >= 80:
            return "A"
        if self.marks >= 60:
            return "B"
        if self.marks >= 40:
            return "C"
        return "F"

    def report(self):
        print(f"{self.name} | age {self.age} | marks {self.marks} | grade {self.grade()}")


sita = Student("Sita", 21, 72)
rohan = Student("Rohan")                 # age and marks use the defaults

sita.report()
rohan.report()

print("\nAfter a birthday:")
sita.birthday()
sita.report()

print("\nAfter adding marks:")
sita.add_marks(10)
rohan.add_marks(55)
sita.report()
rohan.report()

print("\nadd_marks never goes above 100:")
sita.add_marks(50)
sita.report()
