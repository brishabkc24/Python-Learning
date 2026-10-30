"""Build a three-stage generator pipeline over students.csv: read rows, keep marks >= 70, format."""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            yield row


def keep_good_marks(rows):
    for row in rows:
        if int(row["marks"]) >= 70:
            yield row


def format_rows(rows):
    for row in rows:
        yield f"{row['name']} ({row['marks']})"


rows = read_rows(DATA_DIR / "students.csv")
good = keep_good_marks(rows)
for line in format_rows(good):
    print(line)
