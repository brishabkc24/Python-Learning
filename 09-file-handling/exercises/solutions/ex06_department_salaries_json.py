"""Compute the average salary per department from employees.json and save it as JSON."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
OUTPUT_FILE = HERE / "output_department_salaries.json"

with open(DATA_DIR / "employees.json", encoding="utf-8") as file:
    employees = json.load(file)

# Collect the salaries of each department in a list.
salaries_by_department = {}
for person in employees:
    salaries_by_department.setdefault(person["department"], []).append(person["salary"])

averages = {}
for department, salaries in salaries_by_department.items():
    averages[department] = round(sum(salaries) / len(salaries), 2)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(averages, file, indent=2)

print(OUTPUT_FILE.read_text(encoding="utf-8"))
