"""Convert dates from YYYY-MM-DD to DD/MM/YYYY using named groups."""

import re

dates = ["2024-03-15", "1999-12-31", "2021-07-04"]
pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")

for date in dates:
    match = pattern.fullmatch(date)
    converted = f"{match['day']}/{match['month']}/{match['year']}"
    print(f"{date} -> {converted}")
