"""Use re.match to report whether each string starts with "Python"."""

import re

sentences = ["Python is fun", "I like Python", "python3", "Pythonic code"]

for sentence in sentences:
    starts_with_python = re.match(r"Python", sentence) is not None
    print(f"{sentence} -> {starts_with_python}")
