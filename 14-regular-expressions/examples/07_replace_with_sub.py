"""
Demonstrates replacing text with re.sub(): simple word replacement,
limiting the count, using groups in the replacement, and passing a
function that works out the replacement.
Run: python 07_replace_with_sub.py
"""

import re

text = "Python is easy. Python is popular. python is everywhere."

# Replace every match.
print(re.sub(r"Python", "Java", text))

# Replace only the first match with count=1.
print(re.sub(r"Python", "Java", text, count=1))

# Case-insensitive replacement.
print(re.sub(r"python", "Ruby", text, flags=re.IGNORECASE))

# Groups can be reused in the replacement as \1, \2 and so on.
date = "2024-03-15"
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", date))

# Hide the user part of email addresses.
emails = "Contact asha@example.com or bibek@example.com"
print(re.sub(r"\w+@", "***@", emails))

# Squash runs of spaces into one space.
messy = "too    many     spaces   here"
print(re.sub(r"\s+", " ", messy))


# A function decides the replacement for each match.
def double_number(match):
    return str(int(match.group()) * 2)


print(re.sub(r"\d+", double_number, "Prices: 10, 25 and 40"))

# subn() also reports how many replacements were made.
new_text, count = re.subn(r"is", "was", text)
print(count, "replacements:", new_text)
