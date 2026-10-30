"""Compare class attributes (shared) with instance attributes (per object).

Changing a class attribute through the class changes it for every
object. Assigning through one object creates an instance attribute
that hides the class attribute for that object only.
Run: python 03_class_attributes.py
"""


class Employee:
    company = "Example Tech"          # class attribute: one copy for the whole class
    raise_percent = 5                 # class attribute: a setting the methods use
    count = 0                         # class attribute: a counter of objects

    def __init__(self, name, salary):
        self.name = name              # instance attributes: one copy per object
        self.salary = salary
        Employee.count += 1           # update the shared counter

    def apply_raise(self):
        self.salary += self.salary * self.raise_percent // 100

    def show(self):
        print(f"{self.name} works at {self.company} and earns {self.salary}")


asha = Employee("Asha", 50000)
bibek = Employee("Bibek", 40000)
print("Employees created:", Employee.count)

asha.show()
bibek.show()

print("\nChanging the class attribute affects everyone:")
Employee.company = "Example Software"
asha.show()
bibek.show()

print("\nAssigning through one object affects only that object:")
asha.company = "Example Labs"
asha.show()
bibek.show()
print("Employee.company is still:", Employee.company)

print("\nA class attribute can be a setting shared by all methods:")
Employee.raise_percent = 10
asha.apply_raise()
bibek.apply_raise()
asha.show()
bibek.show()
