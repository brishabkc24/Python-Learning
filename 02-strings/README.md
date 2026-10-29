# Strings

A string is a piece of text: a sequence of characters inside quotes. Almost every program works with text, so knowing how to look inside a string, cut it up and tidy it is a core skill.

## What you will learn

- The three ways to write a string
- How to pick out characters with indexes and parts with slices
- Why strings cannot be changed in place
- How to join, repeat, loop over and search strings
- The most useful string methods
- How Python compares strings
- Short programs: reverse, palindrome, counting and cleaning text

## 1. Creating strings

You can write a string with single quotes, double quotes or triple quotes. Single and double quotes mean the same thing; choose the one that lets you avoid escaping a quote inside the text. Triple quotes let the string run over several lines.

```python
city = 'Pokhara'
sentence = "It's a sunny day."
note = """Line one
Line two"""
print(city)
print(sentence)
print(note)
print(type(city))
```

Output:

```
Pokhara
It's a sunny day.
Line one
Line two
<class 'str'>
```

## 2. Indexing

Every character in a string has a position called an index. Counting starts at 0, not 1. Put the index in square brackets after the string to get the character at that position. Negative indexes count from the end: `-1` is the last character, `-2` the one before it.

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

```python
word = "Python"
print(word[0])
print(word[2])
print(word[-1])
print(word[-3])
```

Output:

```
P
t
n
h
```

Asking for an index that does not exist raises an `IndexError`. `"Python"[6]` fails because the valid indexes are 0 to 5.

## 3. Slicing

A slice takes a part of a string. The form is `text[start:stop:step]`. `start` is the first index you want, `stop` is the first index you do not want, and `step` is how far to jump each time. Each part is optional: `start` defaults to the beginning, `stop` to the end and `step` to 1.

| Slice | Meaning | Result for `"programming"` |
|---|---|---|
| `[0:3]` | indexes 0, 1, 2 | `pro` |
| `[3:7]` | indexes 3 to 6 | `gram` |
| `[:4]` | from the start to index 3 | `prog` |
| `[4:]` | from index 4 to the end | `ramming` |
| `[-4:]` | the last four characters | `ming` |
| `[:-4]` | everything except the last four | `program` |
| `[::2]` | every second character | `pormig` |
| `[::-1]` | the whole string backwards | `gnimmargorp` |

```python
word = "programming"
print(word[0:3])
print(word[3:7])
print(word[:4])
print(word[4:])
print(word[-4:])
print(word[:-4])
print(word[::2])
print(word[::-1])
```

Output:

```
pro
gram
prog
ramming
ming
program
pormig
gnimmargorp
```

A slice never raises an error for going past the end; it simply stops at the last character.

## 4. len()

`len()` returns the number of characters in a string, including spaces and punctuation. Because indexes start at 0, the last index is always `len(text) - 1`.

```python
greeting = "Good morning!"
print(len(greeting))
print(greeting[len(greeting) - 1])
print(len(""))
```

Output:

```
13
!
0
```

## 5. Strings are immutable

Immutable means "cannot be changed". Once a string exists, you cannot replace one of its characters in place. Trying to do so raises a `TypeError`. Suppose the file `C:\code\immutable.py` contains:

```python
word = "hello"
word[0] = "J"
```

Output:

```
Traceback (most recent call last):
  File "C:\code\immutable.py", line 2, in <module>
    word[0] = "J"
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

Instead, build a new string and store it, in the same variable if you like:

```python
word = "hello"
word = "J" + word[1:]
print(word)
```

Output:

```
Jello
```

Every string method in this topic works the same way: it returns a new string and leaves the original untouched.

## 6. Concatenation and repetition

Concatenation means joining strings end to end with `+`. Repetition means repeating a string with `*`. Both make new strings. You can only concatenate strings with strings; to add a number, convert it with `str()` first or use an f-string.

```python
first = "Asha"
last = "Thapa"
full = first + " " + last
print(full)
print("-" * 20)
print("ab" * 3)
age = 21
print(first + " is " + str(age))
```

Output:

```
Asha Thapa
--------------------
ababab
Asha is 21
```

## 7. Iterating with for

A `for` loop visits each character of a string in turn. The loop variable holds one character at a time. Loops are covered fully in the Loops topic; here you only need this one pattern.

```python
for character in "abc":
    print(character)

count = 0
for character in "banana":
    if character == "a":
        count += 1
print("a appears", count, "times")
```

Output:

```
a
b
c
a appears 3 times
```

## 8. Membership with in

The `in` operator checks whether one string appears inside another. It gives `True` or `False`. `not in` is the opposite. The check is case sensitive.

```python
email = "asha@example.com"
print("@" in email)
print(".com" in email)
print("ASHA" in email)
print("gov" not in email)
```

Output:

```
True
True
False
True
```

## 9. String methods

A method is a function attached to a value. You call it with a dot after the string: `text.upper()`. The table lists the methods you will use most. Every one returns a new value and leaves the original string unchanged.

| Method | What it does | Example | Result |
|---|---|---|---|
| `upper()` | all capitals | `"hello".upper()` | `'HELLO'` |
| `lower()` | all lower case | `"Hello".lower()` | `'hello'` |
| `title()` | capital at the start of every word | `"hello world".title()` | `'Hello World'` |
| `capitalize()` | capital at the start, rest lower case | `"hello WORLD".capitalize()` | `'Hello world'` |
| `strip()` | remove spaces at both ends | `"  hi  ".strip()` | `'hi'` |
| `lstrip()` | remove spaces at the left end | `"  hi  ".lstrip()` | `'hi  '` |
| `rstrip()` | remove spaces at the right end | `"  hi  ".rstrip()` | `'  hi'` |
| `split()` | cut into a list of words | `"a b c".split()` | `['a', 'b', 'c']` |
| `join()` | glue a list together with the string | `"-".join(["a", "b"])` | `'a-b'` |
| `replace()` | swap every match for new text | `"cat".replace("c", "b")` | `'bat'` |
| `find()` | index of the first match, `-1` if absent | `"hello".find("l")` | `2` |
| `index()` | like `find()`, but an error if absent | `"hello".index("l")` | `2` |
| `count()` | how many times a piece appears | `"banana".count("a")` | `3` |
| `startswith()` | does it begin with this? | `"python".startswith("py")` | `True` |
| `endswith()` | does it end with this? | `"file.py".endswith(".py")` | `True` |
| `isdigit()` | only digits? | `"123".isdigit()` | `True` |
| `isalpha()` | only letters? | `"abc".isalpha()` | `True` |
| `isalnum()` | only letters and digits? | `"abc123".isalnum()` | `True` |
| `isspace()` | only spaces, tabs and newlines? | `"   ".isspace()` | `True` |

```python
text = "  Python is fun  "
print(text.strip())
print(text.upper())
print(text.strip().title())
print(text.replace("fun", "useful"))
print(text.find("is"))
print(text.count("n"))
print(text.split())
print(", ".join(["red", "green", "blue"]))
print("2024".isdigit(), "2024".isalpha())
print("report.pdf".endswith(".pdf"))
print(text)
```

Output:

```
Python is fun
  PYTHON IS FUN  
Python Is Fun
  Python is useful  
9
2
['Python', 'is', 'fun']
red, green, blue
True False
True
  Python is fun  
```

The last line shows that `text` itself never changed.

## 10. Comparing strings

`==` and `!=` compare strings character by character, so `"Asha"` and `"asha"` are different. `<` and `>` compare alphabetically using each character's code number. All capital letters come before all lower-case letters, so `"Zebra"` is "less than" `"apple"`. To compare without caring about case, convert both sides with `lower()` first.

```python
print("Asha" == "asha")
print("Asha".lower() == "asha")
print("apple" < "banana")
print("Zebra" < "apple")
print("zebra" < "apple")
```

Output:

```
False
True
True
True
False
```

## 11. Common string programs

These short programs combine the ideas above. Each one is complete.

**Reverse a string**

```python
word = "python"
print(word[::-1])
```

Output:

```
nohtyp
```

**Palindrome check**

A palindrome reads the same forwards and backwards. Clean the text first so that capitals and spaces do not matter.

```python
phrase = "Never odd or even"
cleaned = phrase.lower().replace(" ", "")
print(cleaned == cleaned[::-1])
```

Output:

```
True
```

**Count vowels**

```python
sentence = "Programming in Python"
vowels = 0
for character in sentence.lower():
    if character in "aeiou":
        vowels += 1
print("Vowels:", vowels)
```

Output:

```
Vowels: 5
```

**Count words**

```python
sentence = "Python is easy to read and easy to learn"
words = sentence.split()
print("Words:", len(words))
print("Times 'easy' appears:", words.count("easy"))
```

Output:

```
Words: 9
Times 'easy' appears: 2
```

**Capitalise each word**

```python
name = "asha kumari thapa"
print(name.title())
```

Output:

```
Asha Kumari Thapa
```

**Remove spaces**

`strip()` removes spaces only at the ends. To remove every space, use `replace()`.

```python
code = " A B  C "
print("[" + code.strip() + "]")
print("[" + code.replace(" ", "") + "]")
```

Output:

```
[A B  C]
[ABC]
```

## Common mistakes

- Expecting `word[1]` to be the first character -> indexes start at 0, so the first character is `word[0]`.
- Writing `word[0] = "J"` to change a letter -> strings are immutable; build a new one: `word = "J" + word[1:]`.
- Calling `text.upper()` and expecting `text` to change -> methods return a new string; store it: `text = text.upper()`.
- Joining a number with `+`, as in `"Age: " + 21` -> convert first: `"Age: " + str(21)`, or use `f"Age: {21}"`.
- Using `index()` for a search that may fail -> `index()` raises `ValueError` when nothing is found; use `find()`, which returns `-1`.
- Comparing `"Yes"` with `"yes"` and getting `False` -> compare `text.lower() == "yes"`.

## Summary

- Strings are written with single, double or triple quotes.
- `text[i]` picks one character; indexes start at 0 and negative indexes count from the end.
- `text[start:stop:step]` takes a part; `text[::-1]` reverses the string.
- `len(text)` counts the characters.
- Strings are immutable: every method returns a new string.
- `+` joins strings, `*` repeats them, `in` searches inside them and `for` visits each character.
- Methods such as `strip()`, `split()`, `join()`, `replace()`, `find()` and `count()` do most everyday text work.
- `==` is case sensitive; use `lower()` on both sides to ignore case.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Python Basics](../01-python-basics/README.md) | [Next: Control Flow](../03-control-flow/README.md) | [Home](../README.md)
