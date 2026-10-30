"""Manager extends Employee: super().__init__() adds team_size and super().introduce() keeps the parent's line."""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def introduce(self):
        print(f"I am {self.name} and I earn {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def introduce(self):
        super().introduce()                       # the parent's sentence first
        print(f"I manage a team of {self.team_size} people")


asha = Employee("Asha", 50000)
deepa = Manager("Deepa", 91000, 6)

asha.introduce()
deepa.introduce()
print("Is deepa an Employee?", isinstance(deepa, Employee))
