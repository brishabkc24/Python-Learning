"""Append one "Visit N" line to output_visits.txt on every run and print the total."""

from pathlib import Path

VISITS_FILE = Path(__file__).resolve().parent / "output_visits.txt"

# Count the lines already there. A missing file means zero visits so far.
if VISITS_FILE.exists():
    with open(VISITS_FILE, encoding="utf-8") as file:
        previous_visits = len(file.readlines())
else:
    previous_visits = 0

visit_number = previous_visits + 1
with open(VISITS_FILE, "a", encoding="utf-8") as file:
    file.write(f"Visit {visit_number}\n")

print(f"Recorded Visit {visit_number}. Total visits: {visit_number}")
