"""
Demonstrates groups: group(), groups(), named groups (?P<name>...), and
the flags re.IGNORECASE and re.MULTILINE.
Run: python 04_groups_and_flags.py
"""

import re

date_text = "Joined on 2021-03-15"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
print("group()  :", match.group())        # the whole match
print("group(1) :", match.group(1))       # the first pair of brackets
print("group(3) :", match.group(3))
print("groups() :", match.groups())       # every bracket as a tuple

# Named groups make the result readable.
named = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date_text)
print("named year :", named.group("year"))
print("groupdict():", named.groupdict())
print("Reformatted:", f"{named['day']}/{named['month']}/{named['year']}")

# findall() with groups returns tuples of the groups, not the whole match.
log = "asha@example.com, bibek@example.com"
print("user and domain pairs:", re.findall(r"(\w+)@(\w+\.com)", log))

# re.IGNORECASE matches upper and lower case letters alike.
text = "Python python PYTHON"
print("without flag:", re.findall(r"python", text))
print("IGNORECASE  :", re.findall(r"python", text, re.IGNORECASE))

# re.MULTILINE makes ^ and $ work at every line, not just the whole string.
lines = "apple 10\nbanana 20\ncherry 30"
print("without flag:", re.findall(r"^\w+", lines))
print("MULTILINE   :", re.findall(r"^\w+", lines, re.MULTILINE))

# Flags can be combined with the | operator.
mixed = "ONE\ntwo\nThree"
print("both flags  :", re.findall(r"^[a-z]+$", mixed, re.IGNORECASE | re.MULTILINE))
