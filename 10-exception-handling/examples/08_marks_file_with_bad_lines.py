"""
Reads a marks file in which some lines are broken, and handles each
problem without stopping. The script copies datasets/marks.txt to
output_marks_with_errors.txt next to itself and adds two bad lines, so
the dataset itself is never changed.
Run: python 08_marks_file_with_bad_lines.py
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
BROKEN_FILE = HERE / "output_marks_with_errors.txt"

# Build the test file: the real data plus two lines with problems.
original = (DATA_DIR / "marks.txt").read_text(encoding="utf-8")
BROKEN_FILE.write_text(original + "Kiran 70 abc 80\nMaya 65\n", encoding="utf-8")

averages = {}
with open(BROKEN_FILE, encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.split()
        try:
            name = parts[0]
            maths, science, english = parts[1:]        # ValueError if not 3 values
            marks = [int(maths), int(science), int(english)]   # ValueError if not numbers
        except ValueError as error:
            print(f"Line {line_number} skipped: {line.strip()!r}")
            print(f"  reason: {error}")
            continue
        averages[name] = sum(marks) / 3

print("Valid students:", len(averages))
for name, average in averages.items():
    print(f"  {name:<8} {average:.2f}")
