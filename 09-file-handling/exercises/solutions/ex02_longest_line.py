"""Count the lines in datasets/sample_text.txt and print the longest line with its length."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[3] / "datasets"

longest = ""
line_count = 0
with open(DATA_DIR / "sample_text.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        line_count += 1
        if len(line) > len(longest):
            longest = line

print("Lines:", line_count)
print(f"Longest line ({len(longest)} characters):")
print(longest)
