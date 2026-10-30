"""Build PermanentEmployee objects from datasets/employees.json, add temporary staff and run the payroll."""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def calculate_salary(self):
        return 0

    def show(self):
        print(f"{self.name:<16} {self.department:<16} {type(self).__name__:<18} "
              f"{self.calculate_salary():>10.2f}")


class PermanentEmployee(Employee):
    def __init__(self, name, department, base_salary):
        super().__init__(name, department)
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = self.base_salary * 10 / 100           # 10 percent bonus
        allowance = 2000
        return self.base_salary + bonus + allowance

    @classmethod
    def from_record(cls, record):
        return cls(record["name"], record["department"], record["salary"])


class TemporaryEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


with open(DATA_DIR / "employees.json", encoding="utf-8") as file:
    records = json.load(file)

staff = [PermanentEmployee.from_record(record) for record in records]
staff.append(TemporaryEmployee("Rita Lama", "Marketing", 450, 100))
staff.append(TemporaryEmployee("Sanjay Pandey", "Engineering", 600, 80))

for person in staff:
    person.show()

total = sum(person.calculate_salary() for person in staff)
print(f"\nStaff: {len(staff)}  Total payroll: {total:.2f}")

best_paid = max(staff, key=lambda person: person.calculate_salary())
print(f"Best paid: {best_paid.name} ({best_paid.calculate_salary():.2f})")

permanent_count = sum(1 for person in staff if isinstance(person, PermanentEmployee))
print(f"Permanent: {permanent_count}, temporary: {len(staff) - permanent_count}")
