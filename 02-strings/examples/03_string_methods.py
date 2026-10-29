"""Call the most useful string methods and show that the original string
never changes (strings are immutable).

Run: python 03_string_methods.py
"""

text = "  Python is Fun  "
print(f"Original: '{text}'")

# Methods return a new string. The original is untouched.
print(f"upper():      '{text.upper()}'")
print(f"lower():      '{text.lower()}'")
print(f"strip():      '{text.strip()}'")
print(f"lstrip():     '{text.lstrip()}'")
print(f"rstrip():     '{text.rstrip()}'")
print(f"Still there:  '{text}'")

clean = text.strip()
print()
print(f"title():      '{clean.title()}'")
print(f"capitalize(): '{clean.capitalize()}'")
print(f"replace():    '{clean.replace('Fun', 'useful')}'")

# Searching inside a string.
print()
print("find('is'):     ", clean.find("is"))       # index of the first match
print("find('xyz'):    ", clean.find("xyz"))      # -1 when there is no match
print("index('Fun'):   ", clean.index("Fun"))     # like find, but errors if missing
print("count('n'):     ", clean.count("n"))
print("startswith('Py'):", clean.startswith("Py"))
print("endswith('.'):  ", clean.endswith("."))

# split() breaks a string into a list of words; join() does the reverse.
print()
words = clean.split()
print("split():", words)
print("join() with '-':", "-".join(words))
csv_line = "Asha,21,Pokhara"
print("split(','):", csv_line.split(","))

# The is...() methods check what kind of characters the string holds.
print()
print("'2024'.isdigit():   ", "2024".isdigit())
print("'abc'.isalpha():    ", "abc".isalpha())
print("'abc123'.isalnum(): ", "abc123".isalnum())
print("'   '.isspace():    ", "   ".isspace())
print("'ab 12'.isalnum():  ", "ab 12".isalnum())   # the space makes it False
