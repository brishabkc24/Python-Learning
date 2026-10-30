# Regular Expressions

A regular expression (regex) is a pattern that describes text, such as "ten digits starting with 98" or "some letters, then @, then a domain". Python's `re` module uses these patterns to check, find, extract and replace text, which is work that would otherwise take many lines of string methods.

## What you will learn

- What a regex is and the four jobs it does: validation, searching, extracting and replacing
- Why patterns are written as raw strings
- The `re` functions: `match`, `search`, `fullmatch`, `findall`, `finditer`, `split`, `sub` and `compile`
- Metacharacters, character classes and custom sets
- Quantifiers, and greedy versus non-greedy matching
- Groups, named groups and the `IGNORECASE` and `MULTILINE` flags
- Validating phone numbers, emails, dates and passwords
- Extracting numbers, words and sentences from a file, and replacing text with `sub`

One code block reads `datasets/sample_text.txt`. It starts with a `DATA_DIR` line that finds the datasets folder relative to the script, so save it as a `.py` file inside this topic's `examples` folder before running it.

## 1. What a regex is

A regex is a small language for describing text. The pattern `\d{10}` means "exactly ten digits". With string methods you would split the text, loop over the pieces and test each one; with a regex you write the pattern once and let `re.findall()` do the work. Use a regex when you need to check that input has the right shape (validation), find whether a pattern is present (searching), pull parts out of text (extracting), or change matching parts (replacing).

```python
import re

text = "Call 9800000001 or 9712345678 for help"
print(re.findall(r"\d{10}", text))

# The same job without a regex takes more code.
numbers = [word for word in text.split() if word.isdigit() and len(word) == 10]
print(numbers)
```

Output:

```
['9800000001', '9712345678']
['9800000001', '9712345678']
```

## 2. Raw strings

Regex patterns are full of backslashes, and in a normal Python string a backslash has its own meaning (`"\n"` is a newline). A raw string, written with an `r` before the opening quote, keeps every backslash as it is. Always write patterns as raw strings: `r"\d+"`, not `"\d+"`.

```python
print("a\nb")
print(r"a\nb")
print(len("\n"), len(r"\n"))
```

Output:

```
a
b
a\nb
1 2
```

## 3. The re functions

| Function | What it does | Returns |
|---|---|---|
| `re.match(p, s)` | tests the pattern at the **start** of the string | match object or `None` |
| `re.search(p, s)` | finds the **first** place the pattern appears | match object or `None` |
| `re.fullmatch(p, s)` | tests whether the **whole** string matches | match object or `None` |
| `re.findall(p, s)` | finds **every** match | list of strings (or tuples when there are groups) |
| `re.finditer(p, s)` | finds every match, one at a time | iterator of match objects |
| `re.split(p, s)` | cuts the string wherever the pattern matches | list of strings |
| `re.sub(p, new, s)` | replaces every match with `new` | new string |
| `re.compile(p)` | prepares a pattern for reuse | pattern object with the same methods |

`match()` only looks at the start. A match object prints its position (`span`) and the text it matched; `None` means no match.

```python
import re

text = "Order 66 shipped on 2024-03-15"
print(re.match(r"Order", text))
print(re.match(r"66", text))
```

Output:

```
<re.Match object; span=(0, 5), match='Order'>
None
```

`search()` scans the whole string and stops at the first match. `group()` gives the matched text, `start()` and `end()` give its position.

```python
import re

text = "Order 66 shipped on 2024-03-15"
match = re.search(r"\d+", text)
print(match)
print(match.group())
print(match.start(), match.end())
```

Output:

```
<re.Match object; span=(6, 8), match='66'>
66
6 8
```

`fullmatch()` succeeds only if the pattern covers the string from the first character to the last, which is what validation needs.

```python
import re

print(re.fullmatch(r"\d{10}", "9800000001"))
print(re.fullmatch(r"\d{10}", "98000"))
print(re.fullmatch(r"\d{10}", "9800000001 is my number"))
```

Output:

```
<re.Match object; span=(0, 10), match='9800000001'>
None
None
```

`findall()` returns every match as a list of strings. `finditer()` returns match objects instead, which is useful when you also need positions.

```python
import re

text = "Order 66 shipped on 2024-03-15, order 67 on 2024-03-18."
print(re.findall(r"\d+", text))

for match in re.finditer(r"\d{4}-\d{2}-\d{2}", text):
    print(match.group(), "at", match.span())
```

Output:

```
['66', '2024', '03', '15', '67', '2024', '03', '18']
2024-03-15 at (20, 30)
2024-03-18 at (44, 54)
```

`split()` cuts a string at every match, which handles messy separators better than `str.split()`. `sub()` replaces every match.

```python
import re

print(re.split(r",\s*", "apple, banana,cherry,  mango"))
print(re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", "from 2024-03-15 to 2024-03-18"))
```

Output:

```
['apple', 'banana', 'cherry', 'mango']
from <date> to <date>
```

`compile()` turns a pattern into an object with the same methods. Use it when the same pattern is used many times; it is faster and gives the pattern a name.

```python
import re

date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
print(date_pattern.findall("2024-03-15 and 2024-03-18"))
print(date_pattern.search("joined 2021-03-15").group())
```

Output:

```
['2024-03-15', '2024-03-18']
2021-03-15
```

## 4. Metacharacters

Most characters in a pattern match themselves: `cat` matches the text `cat`. A few characters have special meanings; these are the metacharacters.

| Metacharacter | Meaning | Example | Matches |
|---|---|---|---|
| `.` | any one character except a newline | `c.t` | `cat`, `cot`, `c9t` |
| `^` | start of the string | `^Hello` | `Hello` only at the start |
| `$` | end of the string | `world$` | `world` only at the end |
| `*` | zero or more of the previous item | `go*` | `g`, `go`, `goo` |
| `+` | one or more of the previous item | `go+` | `go`, `goo`, not `g` |
| `?` | zero or one of the previous item | `colou?r` | `color`, `colour` |
| `{m,n}` | between m and n of the previous item | `\d{2,3}` | `12`, `123` |
| `[]` | one character from a set | `[aeiou]` | any one vowel |
| `\|` | either the left or the right side | `cat\|dog` | `cat` or `dog` |
| `()` | a group, treated as one item | `(ha)+` | `ha`, `haha` |
| `\` | escapes the next character, or starts a class | `\.` | a real full stop |

```python
import re


def show(pattern, text):
    matches = [match.group() for match in re.finditer(pattern, text)]
    print(f"{pattern:<10} in {text!r:<26} -> {matches}")


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
```

Output:

```
c.t        in 'cat cot cut ct'           -> ['cat', 'cot', 'cut']
^Hello     in 'Hello world, Hello again' -> ['Hello']
world$     in 'Hello world'              -> ['world']
go*        in 'g go goo gooo'            -> ['g', 'go', 'goo', 'gooo']
go+        in 'g go goo gooo'            -> ['go', 'goo', 'gooo']
colou?r    in 'color colour'             -> ['color', 'colour']
\d{2,3}    in '1 12 123 1234'            -> ['12', '123', '123']
[aeiou]    in 'programming'              -> ['o', 'a', 'i']
cat|dog    in 'cat dog bird'             -> ['cat', 'dog']
(ha)+      in 'ha haha hahaha'           -> ['ha', 'haha', 'hahaha']
\.         in 'a.b.c'                    -> ['.', '.']
```

Notice that `\d{2,3}` found `123` inside `1234`: the pattern matched the first three digits and the leftover `4` was not enough for another match.

## 5. Character classes

A character class matches one character from a set. The backslash classes are shortcuts for common sets, and a capital letter means the opposite. You can also write your own set in square brackets, with a range like `a-z` or a `^` at the start to mean "anything except these".

| Class | Matches | Opposite |
|---|---|---|
| `\d` | a digit 0-9 | `\D` anything that is not a digit |
| `\w` | a letter, digit or underscore | `\W` anything else, such as spaces and punctuation |
| `\s` | a whitespace character (space, tab, newline) | `\S` anything that is not whitespace |
| `[a-z]` | one lowercase letter | `[^a-z]` anything except a lowercase letter |
| `[A-Za-z0-9]` | one letter or digit | `[^0-9]` anything except a digit |

```python
import re


def show(pattern, text):
    matches = [match.group() for match in re.finditer(pattern, text)]
    print(f"{pattern:<12} in {text!r:<20} -> {matches}")


show(r"\d", "Room 42B")
show(r"\D", "Room 42B")
show(r"\w+", "hello_world 123 !")
show(r"\W", "a-b c")
show(r"\s", "a b\tc")
show(r"\S+", "a b\tc")
show(r"[a-z]+", "Hello World")
show(r"[^0-9]+", "ab12cd")
show(r"[A-Z][a-z]+", "Sita and Aarav")
```

Output:

```
\d           in 'Room 42B'           -> ['4', '2']
\D           in 'Room 42B'           -> ['R', 'o', 'o', 'm', ' ', 'B']
\w+          in 'hello_world 123 !'  -> ['hello_world', '123']
\W           in 'a-b c'              -> ['-', ' ']
\s           in 'a b\tc'             -> [' ', '\t']
\S+          in 'a b\tc'             -> ['a', 'b', 'c']
[a-z]+       in 'Hello World'        -> ['ello', 'orld']
[^0-9]+      in 'ab12cd'             -> ['ab', 'cd']
[A-Z][a-z]+  in 'Sita and Aarav'     -> ['Sita', 'Aarav']
```

## 6. Quantifiers, greedy and non-greedy

A quantifier says how many times the item before it may repeat. By default quantifiers are **greedy**: they take as much text as possible while still letting the whole pattern match. Adding `?` after a quantifier makes it **non-greedy**: it takes as little as possible.

| Quantifier | Meaning | Non-greedy form |
|---|---|---|
| `*` | 0 or more | `*?` |
| `+` | 1 or more | `+?` |
| `?` | 0 or 1 | `??` |
| `{n}` | exactly n | - |
| `{n,}` | n or more | `{n,}?` |
| `{m,n}` | between m and n | `{m,n}?` |

```python
import re

html = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.*>", html))
print(re.findall(r"<.*?>", html))

print(re.match(r"\d+", "12345").group())
print(re.match(r"\d+?", "12345").group())

text = "a aa aaa aaaa"
print(re.findall(r"a{2}", text))
print(re.findall(r"a{2,}", text))
print(re.findall(r"a{1,3}", text))
```

Output:

```
['<b>bold</b> and <i>italic</i>']
['<b>', '</b>', '<i>', '</i>']
12345
1
['aa', 'aa', 'aa', 'aa']
['aa', 'aaa', 'aaaa']
['a', 'aa', 'aaa', 'aaa', 'a']
```

The greedy `<.*>` swallowed everything from the first `<` to the last `>`. The non-greedy `<.*?>` stopped at the first `>` each time, which is what you want for tags.

## 7. Groups

Round brackets make a group. A group does two jobs: it treats several characters as one item for a quantifier, and it captures the matched text so you can read it afterwards. `group()` or `group(0)` is the whole match, `group(1)` is the first bracket, and `groups()` returns all of them as a tuple. A named group, written `(?P<name>...)`, can be read by name, which is much clearer than a number.

```python
import re

text = "Joined on 2021-03-15"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(match.group())
print(match.group(1))
print(match.group(3))
print(match.groups())

named = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
print(named.group("year"))
print(named.groupdict())
print(f"{named['day']}/{named['month']}/{named['year']}")

log = "asha@example.com, bibek@example.com"
print(re.findall(r"(\w+)@(\w+\.com)", log))
```

Output:

```
2021-03-15
2021
15
('2021', '03', '15')
2021
{'year': '2021', 'month': '03', 'day': '15'}
15/03/2021
[('asha', 'example.com'), ('bibek', 'example.com')]
```

When the pattern has groups, `findall()` returns tuples of the groups instead of the whole match.

## 8. Flags

Flags change how a pattern is applied. They are passed as the last argument of the `re` functions and can be combined with `|`.

| Flag | Effect |
|---|---|
| `re.IGNORECASE` (or `re.I`) | upper and lower case letters match each other |
| `re.MULTILINE` (or `re.M`) | `^` and `$` match at the start and end of every line, not just the whole string |

```python
import re

text = "Python python PYTHON"
print(re.findall(r"python", text))
print(re.findall(r"python", text, re.IGNORECASE))

lines = "apple 10\nbanana 20\ncherry 30"
print(re.findall(r"^\w+", lines))
print(re.findall(r"^\w+", lines, re.MULTILINE))

mixed = "ONE\ntwo\nThree"
print(re.findall(r"^[a-z]+$", mixed, re.IGNORECASE | re.MULTILINE))
```

Output:

```
['python']
['Python', 'python', 'PYTHON']
['apple']
['apple', 'banana', 'cherry']
['ONE', 'two', 'Three']
```

## 9. Validation programs

Validation means checking that input has the right shape before using it. `fullmatch()` is the right tool because the whole string must fit. The patterns below also use `^` and `$` so that they work the same with `search()`.

A phone number that starts with 98 or 97 and has 10 digits in total: `^(98|97)\d{8}$` means start, then `98` or `97`, then exactly 8 more digits, then end.

```python
import re

for number in ["9800000001", "9712345678", "9600000001", "98000", "98000000012"]:
    status = "valid" if re.fullmatch(r"^(98|97)\d{8}$", number) else "invalid"
    print(number, status)
```

Output:

```
9800000001 valid
9712345678 valid
9600000001 invalid
98000 invalid
98000000012 invalid
```

A simple email check: some letters, digits or dots, then `@`, then a domain with at least one dot and an ending of two or more letters. Real email rules are more complicated, but this catches the common typing mistakes.

```python
import re

email_pattern = re.compile(r"^[\w.]+@[\w.]+\.[a-z]{2,}$")
for email in ["asha@example.com", "bibek.thapa@example.com", "no-at-sign.com", "a@b"]:
    status = "valid" if email_pattern.fullmatch(email) else "invalid"
    print(f"{email:<24} {status}")
```

Output:

```
asha@example.com         valid
bibek.thapa@example.com  valid
no-at-sign.com           invalid
a@b                      invalid
```

Dates in `YYYY-MM-DD` and `DD-MM-YYYY` are just groups of digits separated by hyphens. These patterns check the shape only; `2024-13-45` would pass, so a real program also checks the ranges afterwards.

```python
import re

ymd = re.compile(r"^\d{4}-\d{2}-\d{2}$")
dmy = re.compile(r"^\d{2}-\d{2}-\d{4}$")

for date in ["2024-03-15", "15-03-2024", "2024-3-15", "15/03/2024"]:
    print(f"{date:<12} YYYY-MM-DD: {bool(ymd.fullmatch(date))}  DD-MM-YYYY: {bool(dmy.fullmatch(date))}")
```

Output:

```
2024-03-15   YYYY-MM-DD: True  DD-MM-YYYY: False
15-03-2024   YYYY-MM-DD: False  DD-MM-YYYY: True
2024-3-15    YYYY-MM-DD: False  DD-MM-YYYY: False
15/03/2024   YYYY-MM-DD: False  DD-MM-YYYY: False
```

A strong password needs an uppercase letter, a lowercase letter, a digit and a special character, and must be 8 to 16 characters long. The clearest way is one small `search()` per rule rather than one giant pattern.

```python
import re


def is_strong_password(password):
    if not 8 <= len(password) <= 16:
        return False
    rules = [r"[A-Z]", r"[a-z]", r"\d", r"[!@#$%^&*]"]
    return all(re.search(rule, password) for rule in rules)


for password in ["Password123!", "password123", "Short1!", "ALLUPPER123!", "Good@Pass2024"]:
    print(f"{password:<16} {'strong' if is_strong_password(password) else 'weak'}")
```

Output:

```
Password123!     strong
password123      weak
Short1!          weak
ALLUPPER123!     weak
Good@Pass2024    strong
```

## 10. Extracting from a text file

`findall()` pulls every matching piece out of a text. `\b` marks a word boundary, the place where a word starts or ends, so `\b[A-Z][a-z]+\b` finds whole words that start with a capital letter. A sentence is a run of characters that are not a full stop, followed by a full stop.

```python
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
text = (DATA_DIR / "sample_text.txt").read_text(encoding="utf-8")

print("Numbers:", re.findall(r"\d+", text))

words = re.findall(r"[A-Za-z]+", text)
print("Word count:", len(words))
print("Capitalised:", sorted(set(re.findall(r"\b[A-Z][a-z]+\b", text))))

sentences = re.findall(r"[^.]+\.", text)
print("Sentences:", len(sentences))
for number, sentence in enumerate(sentences, start=1):
    print(f"  {number}. {sentence.strip()}")
```

Output:

```
Numbers: ['1991']
Word count: 67
Capitalised: ['English', 'Guido', 'It', 'Linux', 'Many', 'Python', 'Rossum', 'Windows']
Sentences: 6
  1. Python is a popular programming language.
  2. It was created by Guido van Rossum and first released in 1991.
  3. Python is easy to read and easy to learn, which makes it a great first language.
  4. It is used for web development, data analysis, automation, artificial intelligence and much more.
  5. Python runs on Windows, macOS and Linux.
  6. Many beginners start with Python because the code looks almost like plain English.
```

## 11. Replacing with sub

`re.sub(pattern, replacement, text)` replaces every match. `count` limits the number of replacements, `flags` works as before, and the replacement can refer to groups as `\1`, `\2` and so on. The replacement can even be a function that receives each match object and returns the new text.

```python
import re

text = "Python is easy. Python is popular. python is everywhere."
print(re.sub(r"Python", "Java", text))
print(re.sub(r"Python", "Java", text, count=1))
print(re.sub(r"python", "Ruby", text, flags=re.IGNORECASE))

print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", "2024-03-15"))
print(re.sub(r"\w+@", "***@", "Contact asha@example.com or bibek@example.com"))
print(re.sub(r"\s+", " ", "too    many     spaces"))


def double_number(match):
    return str(int(match.group()) * 2)


print(re.sub(r"\d+", double_number, "Prices: 10, 25 and 40"))
```

Output:

```
Java is easy. Java is popular. python is everywhere.
Java is easy. Python is popular. python is everywhere.
Ruby is easy. Ruby is popular. Ruby is everywhere.
15/03/2024
Contact ***@example.com or ***@example.com
too many spaces
Prices: 20, 50 and 80
```

## 12. Regex mistakes to avoid

| Mistake | What goes wrong | Fix |
|---|---|---|
| Forgetting the `r` prefix | `"\d"` may work by accident today and break later; `"\b"` becomes a backspace character | always write `r"..."` |
| Using `match()` when the text is in the middle | `match()` only tests the start, so it returns `None` | use `search()` or `findall()` |
| Writing `.` to mean a full stop | `.` matches any character, so `a.c` also matches `abc` | escape it: `\.` |
| Using `search()` for validation | `search(r"\d{10}", "9800000001x")` succeeds because the pattern is found inside | use `fullmatch()` or add `^` and `$` |
| Forgetting that `findall()` returns groups | with brackets in the pattern you get tuples, not whole matches | use `(?:...)` for a group you do not want to capture, or use `finditer()` |

```python
import re

text = "My number is 9800000001"
print(re.match(r"\d{10}", text))
print(re.search(r"\d{10}", text).group())

print(re.findall(r"a.c", "abc a.c"))
print(re.findall(r"a\.c", "abc a.c"))

print(re.search(r"\d{10}", "9800000001x") is not None)
print(re.fullmatch(r"\d{10}", "9800000001x") is not None)
```

Output:

```
None
9800000001
['abc', 'a.c']
['a.c']
True
False
```

## Common mistakes

- Pattern written as a normal string -> add the `r` prefix: `r"\d+"`.
- `match()` returns `None` although the text is there -> `match()` only checks the start; use `search()`.
- `findall()` returns tuples instead of the text -> the pattern has groups; use `finditer()` and `match.group()`, or `(?:...)`.
- `.*` grabs far too much -> make it non-greedy with `.*?`.
- A validation pattern accepts extra characters -> use `fullmatch()` or wrap the pattern in `^` and `$`.
- `^` does not match the start of each line -> add the `re.MULTILINE` flag.

## Summary

- A regex is a pattern for text; the `re` module checks, finds, extracts and replaces with it.
- Always write patterns as raw strings: `r"\d+"`.
- `match()` tests the start, `search()` finds the first match, `fullmatch()` tests the whole string, `findall()` and `finditer()` find every match, `split()` cuts, `sub()` replaces and `compile()` prepares a pattern for reuse.
- Metacharacters: `.` `^` `$` `*` `+` `?` `{m,n}` `[]` `|` `()` `\`; classes: `\d` `\w` `\s` and their capitals `\D` `\W` `\S`.
- Quantifiers are greedy by default; add `?` to make them non-greedy.
- Groups capture parts of the match; `(?P<name>...)` gives a group a name.
- `re.IGNORECASE` ignores case and `re.MULTILINE` makes `^` and `$` work per line.
- Validate with `fullmatch()`, extract with `findall()`, replace with `sub()`.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Iterators and Generators](../13-iterators-and-generators/README.md) | [Next: Multithreading](../15-multithreading/README.md) | [Home](../README.md)
