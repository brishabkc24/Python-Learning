"""
Demonstrates the json module: load() and dump() for files, loads() and
dumps() for strings, using datasets/employees.json.
Run: python 06_json_files.py
Creates output_engineering.json next to this script.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

# json.load() reads a file and turns it into Python objects.
with open(DATA_DIR / "employees.json", encoding="utf-8") as file:
    employees = json.load(file)

print("Type after load:", type(employees).__name__)
print("Number of employees:", len(employees))
print("First employee:", employees[0]["name"], "-", employees[0]["department"])

# A JSON list of objects becomes a list of dictionaries.
engineering = [person for person in employees if person["department"] == "Engineering"]
total_salary = sum(person["salary"] for person in engineering)
print("Engineering staff:", [person["name"] for person in engineering])
print("Average engineering salary:", round(total_salary / len(engineering), 2))

# json.dump() writes Python objects to a file. indent makes it readable.
with open(HERE / "output_engineering.json", "w", encoding="utf-8") as file:
    json.dump(engineering, file, indent=2)
print("Saved", len(engineering), "records to output_engineering.json")

# json.dumps() returns a string instead of writing a file.
summary = {"department": "Engineering", "count": len(engineering)}
text = json.dumps(summary)
print("dumps() gave:", text)
print("Type of that result:", type(text).__name__)

# json.loads() turns a string back into Python objects.
back = json.loads('{"name": "Asha Koirala", "skills": ["Python", "SQL"]}')
print("loads() gave:", back["name"], "knows", back["skills"])
