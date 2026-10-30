"""Write output_marks_report.txt with each student's total and average plus the topper, then print it."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"
REPORT_FILE = HERE / "output_marks_report.txt"

report_lines = []
topper_name = ""
topper_average = 0.0

with open(DATA_DIR / "marks.txt", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        name = parts[0]
        marks = [int(value) for value in parts[1:]]
        total = sum(marks)
        average = total / len(marks)
        report_lines.append(f"{name:<8} total {total}  average {average:.2f}\n")
        if average > topper_average:
            topper_name = name
            topper_average = average

report_lines.append(f"Topper: {topper_name} with {topper_average:.2f}\n")

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.writelines(report_lines)

print(REPORT_FILE.read_text(encoding="utf-8"), end="")
