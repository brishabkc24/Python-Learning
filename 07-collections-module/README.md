# The collections Module

The `collections` module is part of the standard library, the set of modules that come with Python. It adds a few special containers that solve common jobs, such as counting items or grouping records, in one or two lines instead of ten.

## What you will learn

- Why `collections` exists and how to import from it
- `Counter` for counting items and finding the most common ones
- `defaultdict` for dictionaries with an automatic default value
- `OrderedDict` and what it still offers over a plain dictionary
- `namedtuple` for tuples whose items have names
- `deque` for fast adding and removing at both ends, as a queue or a stack
- `ChainMap` for looking up keys in several dictionaries at once
- `UserDict`, `UserList` and `UserString` for customised containers

## 1. Why collections exists

Lists, tuples, sets and dictionaries cover most needs, but some jobs come up again and again: counting how often each item appears, grouping items under a key, or removing items from the front of a list quickly. Each can be done with the basic types, but the code is longer and easier to get wrong. The `collections` module packages the proven solutions. You import the one you need with `from collections import Name`.

```python
# Counting with a plain dictionary: four lines
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for fruit in fruits:
    counts[fruit] = counts.get(fruit, 0) + 1
print(counts)

# Counting with Counter: one line
from collections import Counter
print(Counter(fruits))
```

Output:

```
{'apple': 3, 'banana': 2, 'cherry': 1}
Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

## 2. Counter

A `Counter` is a dictionary whose values are counts. Give it any collection and it counts every item. Looking up a missing key gives 0 instead of an error. `most_common(n)` returns the `n` items with the highest counts as a list of `(item, count)` tuples. `update()` adds more items to the count and `total()` gives the sum of all counts.

```python
from collections import Counter

fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(fruits)
print(counts)
print("apples:", counts["apple"])
print("missing key:", counts["mango"])
print("most common:", counts.most_common(2))

letters = Counter("mississippi")
print(letters)
print("total letters:", letters.total())

counts.update(["banana", "mango"])
print("after update:", counts)
```

Output:

```
Counter({'apple': 3, 'banana': 2, 'cherry': 1})
apples: 3
missing key: 0
most common: [('apple', 3), ('banana', 2)]
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
total letters: 11
after update: Counter({'apple': 3, 'banana': 3, 'cherry': 1, 'mango': 1})
```

## 3. Counting words in a file

`datasets/words.txt` has one word per line, with repeats. Reading the lines into a list and passing the list to `Counter` gives the word frequencies at once. The `DATA_DIR` line finds the `datasets` folder relative to the script, as explained in `datasets/README.md`, so save this code inside the `examples` folder (it is the heart of `examples/02_count_words_in_file.py`).

```python
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

with open(DATA_DIR / "words.txt", encoding="utf-8") as file:
    words = [line.strip() for line in file]

word_counts = Counter(words)
print("different words:", len(word_counts))
print("top three:", word_counts.most_common(3))
for word, count in word_counts.most_common(3):
    print(word, "appears", count, "times")
```

Output:

```
different words: 10
top three: [('python', 6), ('java', 4), ('go', 3)]
python appears 6 times
java appears 4 times
go appears 3 times
```

## 4. defaultdict

A `defaultdict` is a dictionary that creates a default value the first time a missing key is used. You tell it how to make the default by passing a function such as `int` (which gives 0) or `list` (which gives an empty list). This removes the "does the key exist yet?" check from counting and grouping code.

```python
from collections import defaultdict

word_lengths = defaultdict(int)
for word in ["apple", "fig", "kiwi", "plum", "cherry"]:
    word_lengths[len(word)] += 1
print(dict(word_lengths))

students_by_city = defaultdict(list)
records = [("Sita", "Pokhara"), ("Aarav", "Kathmandu"), ("Anjali", "Pokhara"),
           ("Maya", "Kathmandu"), ("Priya", "Butwal")]
for name, city in records:
    students_by_city[city].append(name)
for city, names in students_by_city.items():
    print(city, "->", names)

print("unknown city:", students_by_city["Dharan"])
print("keys now:", list(students_by_city.keys()))
```

Output:

```
{5: 1, 3: 1, 4: 2, 6: 1}
Pokhara -> ['Sita', 'Anjali']
Kathmandu -> ['Aarav', 'Maya']
Butwal -> ['Priya']
unknown city: []
keys now: ['Pokhara', 'Kathmandu', 'Butwal', 'Dharan']
```

Notice the last two lines: simply reading a missing key adds it with the default value. Use `in` to check for a key when you do not want that.

## 5. OrderedDict

Since Python 3.7 a plain dictionary remembers the order in which keys were added, so `OrderedDict` is needed less often than it used to be. It still has two extras. `move_to_end(key)` moves a key to the end (or to the start with `last=False`), and `popitem(last=False)` removes the first item instead of the last. Also, two `OrderedDict`s are equal only if their keys are in the same order, while plain dictionaries ignore order.

```python
from collections import OrderedDict

tasks = OrderedDict()
tasks["write"] = "draft the report"
tasks["review"] = "check the numbers"
tasks["send"] = "email the report"
print(list(tasks.keys()))

tasks.move_to_end("write")
print("after move_to_end('write'):", list(tasks.keys()))
tasks.move_to_end("send", last=False)
print("after move_to_end('send', last=False):", list(tasks.keys()))

first = tasks.popitem(last=False)
print("popitem(last=False):", first)
print("remaining:", list(tasks.keys()))

a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print("OrderedDicts equal?", a == b)
print("plain dicts equal?", dict(a) == dict(b))
```

Output:

```
['write', 'review', 'send']
after move_to_end('write'): ['review', 'send', 'write']
after move_to_end('send', last=False): ['send', 'review', 'write']
popitem(last=False): ('send', 'email the report')
remaining: ['review', 'write']
OrderedDicts equal? False
plain dicts equal? True
```

## 6. namedtuple

A `namedtuple` is a tuple whose positions have names. You define a new type by giving it a type name and a list of field names, then create values like calling a function. Items can be read by name with a dot or by index as usual. Because it is a tuple it cannot be changed, but `_replace()` returns a new one with some fields changed, and `_asdict()` turns it into a dictionary.

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "city"])
sita = Student("Sita", 21, "Pokhara")
print(sita)
print("by name:", sita.name, "| by index:", sita[0])
print("as dict:", sita._asdict())

older = sita._replace(age=22)
print("replaced:", older)
print("original unchanged:", sita)

name, age, city = sita
print(name, "is", age, "from", city)
print("fields:", Student._fields)
```

Output:

```
Student(name='Sita', age=21, city='Pokhara')
by name: Sita | by index: Sita
as dict: {'name': 'Sita', 'age': 21, 'city': 'Pokhara'}
replaced: Student(name='Sita', age=22, city='Pokhara')
original unchanged: Student(name='Sita', age=21, city='Pokhara')
Sita is 21 from Pokhara
fields: ('name', 'age', 'city')
```

Use a namedtuple when a plain tuple would leave you guessing what `record[2]` means.

## 7. deque

A `deque` (pronounced "deck", short for double-ended queue) is a list-like container that adds and removes items at either end very quickly. A list is fast at the right end but slow at the left end, because `pop(0)` or `insert(0, x)` must shift every other item along by one. A deque keeps both ends ready, so `appendleft()` and `popleft()` take the same tiny time no matter how long it is. `rotate(n)` moves items from the end to the front `n` times, and `maxlen` makes the deque drop the oldest item when a new one arrives.

```python
from collections import deque

line = deque(["Sita", "Aarav"])
line.append("Bikash")
line.appendleft("Priya")
print(line)
print("popleft():", line.popleft())
print("pop():", line.pop())
print("now:", line)

line.rotate(1)
print("rotate(1):", line)
line.rotate(-1)
print("rotate(-1):", line)

recent = deque(maxlen=3)
for number in [1, 2, 3, 4, 5]:
    recent.append(number)
print("last three seen:", recent)
```

Output:

```
deque(['Priya', 'Sita', 'Aarav', 'Bikash'])
popleft(): Priya
pop(): Bikash
now: deque(['Sita', 'Aarav'])
rotate(1): deque(['Aarav', 'Sita'])
rotate(-1): deque(['Sita', 'Aarav'])
last three seen: deque([3, 4, 5], maxlen=3)
```

A queue is first in, first out, like a line at a counter: add with `append()` and take with `popleft()`. A stack is last in, first out, like a pile of plates: add with `append()` and take with `pop()`.

```python
from collections import deque

queue = deque()
queue.append("task 1")
queue.append("task 2")
queue.append("task 3")
print("queue serves:", queue.popleft(), "then", queue.popleft())

stack = deque()
stack.append("page 1")
stack.append("page 2")
stack.append("page 3")
print("stack goes back to:", stack.pop(), "then", stack.pop())
```

Output:

```
queue serves: task 1 then task 2
stack goes back to: page 3 then page 2
```

## 8. ChainMap

A `ChainMap` groups several dictionaries into one view. A lookup searches the dictionaries in order and returns the first match, which is ideal for settings: user choices first, then defaults. Changes through the ChainMap go to the first dictionary only, and the underlying dictionaries are not copied, so later changes to them show through.

```python
from collections import ChainMap

defaults = {"theme": "light", "language": "en", "font_size": 12}
user_settings = {"theme": "dark"}

settings = ChainMap(user_settings, defaults)
print("theme:", settings["theme"])
print("language:", settings["language"])
print("all keys:", sorted(settings.keys()))

settings["font_size"] = 16          # writes go to the FIRST dictionary
print("user_settings:", user_settings)
print("defaults unchanged:", defaults)
print("maps:", settings.maps)
```

Output:

```
theme: dark
language: en
all keys: ['font_size', 'language', 'theme']
user_settings: {'theme': 'dark', 'font_size': 16}
defaults unchanged: {'theme': 'light', 'language': 'en', 'font_size': 12}
maps: [{'theme': 'dark', 'font_size': 16}, {'theme': 'light', 'language': 'en', 'font_size': 12}]
```

## 9. UserDict, UserList and UserString

Sometimes you want a dictionary, list or string with one rule changed, for example keys that are always upper case. `UserDict`, `UserList` and `UserString` are classes made to be extended: you write a class that inherits from one of them and changes only the method you care about. The `class` keyword and inheritance are explained in OOP Basics, so feel free to come back to this section after that lesson. For now, notice that each example changes exactly one behaviour.

```python
from collections import UserDict, UserList, UserString


class UpperKeyDict(UserDict):
    """A dictionary that stores and looks up every key in upper case."""

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.upper())


class IntList(UserList):
    """A list that accepts only integers."""

    def append(self, item):
        if not isinstance(item, int):
            print("rejected:", repr(item))
            return
        super().append(item)


class StrippedString(UserString):
    """A string that always removes the spaces around it."""

    def __init__(self, text):
        super().__init__(str(text).strip())


settings = UpperKeyDict()
settings["theme"] = "dark"
print(settings)
print(settings["THEME"], settings["Theme"])

numbers = IntList()
numbers.append(1)
numbers.append("two")
numbers.append(3)
print(numbers)

city = StrippedString("   Pokhara  ")
print(repr(city), len(city), city.upper())
```

Output:

```
{'THEME': 'dark'}
dark dark
rejected: 'two'
[1, 3]
'Pokhara' 7 POKHARA
```

## Common mistakes

- Reading a missing key from a `defaultdict` just to check it -> the key is created; use `key in d` instead.
- Expecting `Counter` to raise an error for a missing item -> it returns 0; use `in` if you need to know whether it was counted at all.
- Using a list as a queue with `pop(0)` -> slow for long lists; use `deque` and `popleft()`.
- Trying `student.age = 22` on a namedtuple -> `AttributeError`; use `student._replace(age=22)`.
- Writing to a `ChainMap` and expecting the defaults to change -> only the first dictionary is written; change the defaults dictionary directly if that is what you want.
- Importing with `import collections` and then writing `Counter(...)` -> `NameError`; write `collections.Counter(...)` or use `from collections import Counter`.

## Summary

- `from collections import Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap` gives you the special containers.
- `Counter` counts items; `most_common(n)` lists the top `n`.
- `defaultdict(int)` counts and `defaultdict(list)` groups without any key checks.
- `OrderedDict` adds `move_to_end()` and `popitem(last=False)`; plain dictionaries already keep insertion order.
- `namedtuple` gives tuple fields names; `_asdict()` and `_replace()` are its helpers.
- `deque` is fast at both ends: `append`/`popleft` for a queue, `append`/`pop` for a stack.
- `ChainMap` looks up keys across several dictionaries in order.
- `UserDict`, `UserList` and `UserString` are base classes for containers with custom rules.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Data Structures](../06-data-structures/README.md) | [Next: Modules and Packages](../08-modules-and-packages/README.md) | [Home](../README.md)
