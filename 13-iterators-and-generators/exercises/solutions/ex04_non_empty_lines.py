"""Write read_non_empty(path), a generator of stripped non-empty lines, and count words per line."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"


def read_non_empty(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


for number, line in enumerate(read_non_empty(DATA_DIR / "sample_text.txt"), start=1):
    print(f"Line {number}: {len(line.split())} words")
