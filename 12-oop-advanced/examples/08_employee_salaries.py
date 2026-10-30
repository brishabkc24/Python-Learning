"""Override calculate_salary() in two kinds of Employee and run a payroll.

Employee is the parent. PermanentEmployee adds a bonus and an allowance;
TemporaryEmployee is paid by the hour. One loop prints every salary and
max() with a key finds the best paid person. Run: python 08_employee_salaries.py
"""


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def kind(self):
        return type(self).__name__

    def show(self):
        # Written once, but calculate_salary() is resolved per object.
        print(f"{self.name:<7} {self.kind():<18} {self.calculate_salary():>10.2f}")


class PermanentEmployee(Employee):
    def __init__(self, name, base_salary, bonus, allowance):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.allowance


class TemporaryEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name, 0)            # no base salary for temporary staff
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


staff = [
    PermanentEmployee("Asha", 50000, 5000, 3000),
    TemporaryEmployee("Bibek", 400, 120),
    PermanentEmployee("Deepa", 62000, 8000, 3000),
    TemporaryEmployee("Kiran", 350, 80),
    Employee("Mina", 30000),
]

print(f"{'Name':<7} {'Type':<18} {'Salary':>10}")
for person in staff:
    person.show()

total = sum(person.calculate_salary() for person in staff)
print(f"\nTotal payroll: {total:.2f}")

best_paid = max(staff, key=lambda person: person.calculate_salary())
print(f"Best paid    : {best_paid.name} ({best_paid.kind()})")

permanent = [person for person in staff if isinstance(person, PermanentEmployee)]
print(f"Permanent staff: {', '.join(person.name for person in permanent)}")
