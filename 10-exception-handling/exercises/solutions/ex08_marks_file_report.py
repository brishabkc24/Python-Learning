"""Read a copy of marks.txt with two broken lines added, reporting good lines and skipped lines."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
BROKEN_FILE = HERE / "output_marks_broken.txt"

original = (DATA_DIR / "marks.txt").read_text(encoding="utf-8")
BROKEN_FILE.write_text(original + "Kiran 70 abc 80\nMaya 65\n", encoding="utf-8")

good = 0
skipped = 0
with open(BROKEN_FILE, encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.split()
        try:
            name = parts[0]
            maths, science, english = parts[1:]
            average = (int(maths) + int(science) + int(english)) / 3
        except ValueError as error:
            print(f"Line {line_number} skipped: {error}")
            skipped += 1
        else:
            print(f"{name}: {average:.2f}")
            good += 1

print(f"Good lines: {good}, skipped lines: {skipped}")
