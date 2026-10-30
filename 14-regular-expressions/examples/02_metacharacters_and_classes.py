r"""
Demonstrates the regex metacharacters (. ^ $ * + ? {m,n} [] | () \) and
the character classes \d \D \w \W \s \S plus custom sets such as [a-z].
Run: python 02_metacharacters_and_classes.py
"""

import re


def show(pattern, text):
    matches = [match.group() for match in re.finditer(pattern, text)]
    print(f"{pattern:<12} in {text!r:<26} -> {matches}")


print("Metacharacters")
show(r"c.t", "cat cot cut ct")
show(r"^Hello", "Hello world, Hello again")
show(r"world$", "Hello world")
show(r"go*", "g go goo gooo")
show(r"go+", "g go goo gooo")
show(r"colou?r", "color colour")
show(r"\d{2,3}", "1 12 123 1234")
show(r"[aeiou]", "programming")
show(r"cat|dog", "cat dog bird")
show(r"(ha)+", "ha haha hahaha")
show(r"\.", "a.b.c")

print("Character classes")
show(r"\d", "Room 42B")
show(r"\D", "Room 42B")
show(r"\w+", "hello_world 123 !")
show(r"\W", "a-b c")
show(r"\s", "a b\tc")
show(r"\S+", "a b\tc")
show(r"[a-z]+", "Hello World")
show(r"[^0-9]+", "ab12cd")
show(r"[A-Z][a-z]+", "Sita and Aarav")
