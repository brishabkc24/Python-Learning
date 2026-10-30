"""
Demonstrates the quantifiers in detail and the difference between greedy
matching (take as much as possible) and non-greedy matching (take as
little as possible).
Run: python 03_quantifiers_greedy.py
"""

import re

html = "<b>bold</b> and <i>italic</i>"

# Greedy: .* takes as much as it can, so it runs to the LAST >.
print("Greedy     <.*> :", re.findall(r"<.*>", html))
# Non-greedy: .*? takes as little as it can, so each tag is separate.
print("Non-greedy <.*?>:", re.findall(r"<.*?>", html))

# The same idea with + and its non-greedy form +?.
digits = "12345"
print("Greedy     [0-9]+ :", re.match(r"[0-9]+", digits).group())
print("Non-greedy [0-9]+?:", re.match(r"[0-9]+?", digits).group())

# {m,n}: exactly m, at least m, or between m and n.
text = "a aa aaa aaaa"
print("a{2}   :", re.findall(r"a{2}", text))
print("a{2,}  :", re.findall(r"a{2,}", text))
print("a{1,3} :", re.findall(r"a{1,3}", text))
print("a{2,}? :", re.findall(r"a{2,}?", text))

# A quantifier applies only to the single item just before it.
print("ab+   :", re.findall(r"ab+", "ab abb abbb"))
print("(ab)+ :", [m.group() for m in re.finditer(r"(ab)+", "ab abab ababab")])

# ? after a single item means optional (zero or one).
print("https?:", re.findall(r"https?://\S+", "see http://a.example.com and https://b.example.com"))
