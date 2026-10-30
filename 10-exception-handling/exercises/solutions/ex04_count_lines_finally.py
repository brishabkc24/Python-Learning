"""Write count_lines(path) that returns -1 for a missing file and always prints a finally message."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"


def count_lines(path):
    try:
        with open(path, encoding="utf-8") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return -1
    finally:
        print("Finished checking", path.name)


for filename in ["sample_text.txt", "missing.txt"]:
    path = DATA_DIR / filename
    count = count_lines(path)
    print(f"{filename} has {count} lines")
