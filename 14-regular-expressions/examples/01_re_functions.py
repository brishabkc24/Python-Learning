"""
Demonstrates the main functions of the re module: match, search,
fullmatch, findall, finditer, split, sub and compile.
Run: python 01_re_functions.py
"""

import re

text = "Order 66 shipped on 2024-03-15, order 67 on 2024-03-18."

# match() looks only at the very start of the string.
print("match 'Order':", re.match(r"Order", text))
print("match '66'   :", re.match(r"66", text))

# search() finds the first place the pattern appears anywhere.
found = re.search(r"\d{4}-\d{2}-\d{2}", text)
print("search date  :", found.group(), "at position", found.start())

# fullmatch() succeeds only if the whole string fits the pattern.
print("fullmatch 9800000001:", re.fullmatch(r"\d{10}", "9800000001") is not None)
print("fullmatch 98000     :", re.fullmatch(r"\d{10}", "98000") is not None)

# findall() returns every match as a list of strings.
print("findall numbers:", re.findall(r"\d+", text))

# finditer() gives match objects one by one, with their positions.
for match in re.finditer(r"\d{4}-\d{2}-\d{2}", text):
    print("finditer:", match.group(), "at", match.span())

# split() cuts the string wherever the pattern matches.
print("split:", re.split(r",\s*|\s+", "one, two,three  four"))

# sub() replaces every match.
print("sub:", re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", text))

# compile() saves a pattern that you will use again and again.
date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
print("compiled findall:", date_pattern.findall(text))
print("compiled search :", date_pattern.search(text).group())
