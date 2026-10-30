"""
Practical file programs: save student records to a file, read them back and
filter by city; then count word frequency in datasets/words.txt with a plain
dictionary and again with collections.Counter.
Run: python 08_records_and_word_frequency.py
Creates output_students.txt next to this script.
"""

from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
RECORDS_FILE = HERE / "output_students.txt"

students = [
    ("Aarav Sharma", 20, "Kathmandu"),
    ("Sita Rai", 21, "Pokhara"),
    ("Bikash Thapa", 19, "Lalitpur"),
    ("Anjali Shrestha", 21, "Kathmandu"),
    ("Maya Limbu", 19, "Kathmandu"),
]

# Write one record per line, fields separated by commas.
with open(RECORDS_FILE, "w", encoding="utf-8") as file:
    for name, age, city in students:
        file.write(f"{name},{age},{city}\n")
print("Saved", len(students), "records to", RECORDS_FILE.name)

# Read the records back and keep only the students from Kathmandu.
print("Students from Kathmandu:")
with open(RECORDS_FILE, encoding="utf-8") as file:
    for line in file:
        name, age, city = line.strip().split(",")
        if city == "Kathmandu":
            print(f"  {name}, age {age}")

# Word frequency, first with a plain dictionary.
frequency = {}
with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        frequency[word] = frequency.get(word, 0) + 1

# Sort by count, highest first, and show the top three.
ranked = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
print("Top words with a dict:")
for word, count in ranked[:3]:
    print(f"  {word}: {count}")

# The same job with Counter, which counts and ranks for us.
with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    counter = Counter(line.strip() for line in file)
print("Top words with Counter:")
for word, count in counter.most_common(3):
    print(f"  {word}: {count}")
