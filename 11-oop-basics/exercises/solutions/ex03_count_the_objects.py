"""Employee class with a shared company name and a counter of created objects."""


class Employee:
    company = "Example Tech"
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def show(self):
        print(f"{self.name} works at {self.company}")


employees = [
    Employee("Asha", 50000),
    Employee("Bibek", 42000),
    Employee("Deepa", 61000),
]

print("Employees created:", Employee.count)
for employee in employees:
    employee.show()

Employee.company = "Example Software"       # changed through the class: everyone sees it
print("After the rename:")
for employee in employees:
    employee.show()
