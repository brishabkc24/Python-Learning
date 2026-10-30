"""Extract the year of every joined date in employees.json with a group in findall."""

import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
text = (DATA_DIR / "employees.json").read_text(encoding="utf-8")

# The group keeps only the year; findall returns the group values.
years = re.findall(r"(\d{4})-\d{2}-\d{2}", text)
print("Years:", years)

after_2020 = sum(1 for year in years if int(year) > 2020)
print("Joined after 2020:", after_2020)
