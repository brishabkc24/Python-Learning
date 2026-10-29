# Data Structures

A data structure is a way of storing many values under one name. Python gives you four built-in ones: lists, tuples, sets and dictionaries. Almost every real program keeps its data in them, so knowing which one to pick is a core skill.

## What you will learn

- Lists: creating, indexing, slicing, nesting and the common methods
- The difference between `sorted()` and `.sort()`, and between a copy and a reference
- Tuples: fixed collections, packing and unpacking
- Sets: unique items and the set operations
- Dictionaries: key-value pairs, safe lookup with `get()`, loops and nesting
- `zip` and `enumerate`
- List, dictionary and set comprehensions
- Which structure to choose for a given job

## 1. Lists: create, index, slice

A list is an ordered collection of items written inside square brackets. Each item has an index, which is its position counted from 0. Negative indexes count from the end, so `-1` is the last item. A slice `[start:stop]` gives a new list from `start` up to but not including `stop`. Lists are mutable, which means you can change them after they are made.

```python
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)
print("First:", fruits[0])
print("Last:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])
print("From index 2:", fruits[2:])
print("Every second item:", fruits[::2])
print("Number of items:", len(fruits))

fruits[1] = "blueberry"
print("After change:", fruits)

mixed = [1, "two", 3.0, True]
print("Mixed types:", mixed)
```

Output:

```
['apple', 'banana', 'cherry', 'mango']
First: apple
Last: mango
Slice [1:3]: ['banana', 'cherry']
From index 2: ['cherry', 'mango']
Every second item: ['apple', 'cherry']
Number of items: 4
After change: ['apple', 'blueberry', 'cherry', 'mango']
Mixed types: [1, 'two', 3.0, True]
```

## 2. Nested lists

A list can contain other lists. This is how a table or grid is stored: a list of rows, where each row is a list. Use two indexes to reach one cell, the first for the row and the second for the column.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Second row:", matrix[1])
print("Row 1, column 2:", matrix[1][2])

for row in matrix:
    print(row)

student = ["Sita", 21, ["Maths", "Science"]]
print("Second subject:", student[2][1])
```

Output:

```
Second row: [4, 5, 6]
Row 1, column 2: 6
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Second subject: Science
```

## 3. List methods

A method is a function that belongs to an object and is called with a dot, as in `numbers.append(1)`. These are the list methods you will use most.

| Method | What it does |
|---|---|
| `append(x)` | adds `x` at the end |
| `insert(i, x)` | adds `x` at index `i`, pushing later items right |
| `extend(items)` | adds every item of another collection at the end |
| `remove(x)` | removes the first item equal to `x` (error if missing) |
| `pop()` / `pop(i)` | removes and returns the last item, or the item at index `i` |
| `clear()` | removes everything |
| `index(x)` | returns the index of the first `x` (error if missing) |
| `count(x)` | returns how many times `x` appears |
| `sort()` | sorts the list in place |
| `reverse()` | reverses the list in place |
| `copy()` | returns a new list with the same items |

```python
numbers = [5, 2, 8]
numbers.append(1)
print("append(1):", numbers)
numbers.insert(0, 9)
print("insert(0, 9):", numbers)
numbers.extend([4, 2])
print("extend([4, 2]):", numbers)
numbers.remove(2)
print("remove(2):", numbers)
last = numbers.pop()
print("pop():", last, "->", numbers)
second = numbers.pop(1)
print("pop(1):", second, "->", numbers)
print("index(8):", numbers.index(8))
print("count(4):", numbers.count(4))
numbers.sort()
print("sort():", numbers)
numbers.reverse()
print("reverse():", numbers)
backup = numbers.copy()
numbers.clear()
print("clear():", numbers, "backup:", backup)
```

Output:

```
append(1): [5, 2, 8, 1]
insert(0, 9): [9, 5, 2, 8, 1]
extend([4, 2]): [9, 5, 2, 8, 1, 4, 2]
remove(2): [9, 5, 8, 1, 4, 2]
pop(): 2 -> [9, 5, 8, 1, 4]
pop(1): 5 -> [9, 8, 1, 4]
index(8): 1
count(4): 1
sort(): [1, 4, 8, 9]
reverse(): [9, 8, 4, 1]
clear(): [] backup: [9, 8, 4, 1]
```

## 4. sorted() vs .sort()

`sorted(items)` is a function that returns a new sorted list and leaves the original alone. `items.sort()` is a method that sorts the list in place and returns `None`. Both accept `reverse=True` and a `key` function.

```python
marks = [67, 92, 45, 85]

ordered = sorted(marks)
print("sorted() gave:", ordered)
print("original is unchanged:", marks)

result = marks.sort()
print(".sort() gave back:", result)
print("original is now sorted:", marks)

print("descending:", sorted(marks, reverse=True))
names = ["sita", "Aarav", "bikash"]
print("case-insensitive:", sorted(names, key=str.lower))
```

Output:

```
sorted() gave: [45, 67, 85, 92]
original is unchanged: [67, 92, 45, 85]
.sort() gave back: None
original is now sorted: [45, 67, 85, 92]
descending: [92, 85, 67, 45]
case-insensitive: ['Aarav', 'bikash', 'sita']
```

A common bug is `marks = marks.sort()`, which replaces the list with `None`.

## 5. Copy vs reference

Assigning a list to a new name does not copy it. Both names now refer to the same list, so a change through one name shows through the other. This is called aliasing. To get an independent list, make a copy with `.copy()`, `list(original)` or the slice `original[:]`.

```python
original = [1, 2, 3]
alias = original            # both names point to the SAME list
alias.append(4)
print("original:", original)
print("alias:", alias)
print("same object?", alias is original)

duplicate = original.copy()    # a new list with the same items
duplicate.append(5)
print("original:", original)
print("duplicate:", duplicate)
print("same object?", duplicate is original)
```

Output:

```
original: [1, 2, 3, 4]
alias: [1, 2, 3, 4]
same object? True
original: [1, 2, 3, 4]
duplicate: [1, 2, 3, 4, 5]
same object? False
```

`.copy()` copies only the outer list. If the list contains other lists, those inner lists are still shared. Use `copy.deepcopy()` from the `copy` module when you need everything copied.

## 6. Tuples

A tuple is an ordered collection like a list, but immutable: once made, its items cannot be changed, added or removed. Tuples are written with parentheses. A one-item tuple needs a trailing comma, because `(2)` is just the number 2. Putting several values into one tuple is called packing; pulling them out into separate names is unpacking.

```python
point = (3, 4)
print("point:", point, "x =", point[0], "y =", point[1])

single = (2,)
not_a_tuple = (2)
print(type(single), type(not_a_tuple))

student = "Sita", 21, "Pokhara"      # packing
name, age, city = student            # unpacking
print(name, "is", age, "from", city)

a, b = 1, 2
a, b = b, a                          # swap in one line
print("after swap:", a, b)

colours = ("red", "green", "red", "blue")
print("count('red'):", colours.count("red"))
print("index('blue'):", colours.index("blue"))

as_list = list(colours)              # convert to a list to change it
as_list.append("pink")
colours = tuple(as_list)             # and back to a tuple
print("after convert and back:", colours)

scores = (67, 92, 45)
print("sorted tuple:", tuple(sorted(scores)))
```

Output:

```
point: (3, 4) x = 3 y = 4
<class 'tuple'> <class 'int'>
Sita is 21 from Pokhara
after swap: 2 1
count('red'): 2
index('blue'): 3
after convert and back: ('red', 'green', 'red', 'blue', 'pink')
sorted tuple: (45, 67, 92)
```

Writing `point[0] = 10` gives `TypeError: 'tuple' object does not support item assignment`. Use a tuple when the data should not change, such as a coordinate, a date or a database row. Tuples are also a little faster than lists and can be used as dictionary keys.

## 7. Sets

A set is an unordered collection of unique items, written with curly braces. Adding an item that is already present does nothing. Because sets have no order, you cannot index them, but checking whether an item is present with `in` is very fast. `remove()` raises an error if the item is missing; `discard()` does not.

```python
numbers = {1, 2, 2, 3, 3, 3}
print("duplicates removed:", numbers)

numbers.add(4)
numbers.add(2)              # already there, nothing happens
print("after add:", numbers)
numbers.remove(1)
numbers.discard(99)         # missing item: no error
print("after remove and discard:", numbers)
print("is 3 in the set?", 3 in numbers)

cities = set(["Pokhara", "Kathmandu", "Pokhara"])
print("from a list:", sorted(cities))
numbers.clear()
print("after clear:", numbers)
```

Output:

```
duplicates removed: {1, 2, 3}
after add: {1, 2, 3, 4}
after remove and discard: {2, 3, 4}
is 3 in the set? True
from a list: ['Kathmandu', 'Pokhara']
after clear: set()
```

An empty set is written `set()`, because `{}` makes an empty dictionary. The printed order of a set is not guaranteed, so use `sorted()` when you need a fixed order.

Sets support the operations from mathematics. Each one has a method and an operator that do the same thing.

| Method | Operator | Result |
|---|---|---|
| `a.union(b)` | `a \| b` | items in `a` or `b` or both |
| `a.intersection(b)` | `a & b` | items in both |
| `a.difference(b)` | `a - b` | items in `a` but not in `b` |
| `a.symmetric_difference(b)` | `a ^ b` | items in exactly one of them |
| `a.issubset(b)` | `a <= b` | is every item of `a` in `b`? |
| `a.issuperset(b)` | `a >= b` | is every item of `b` in `a`? |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("union:", a.union(b), a | b)
print("intersection:", a.intersection(b), a & b)
print("difference:", a.difference(b), a - b)
print("symmetric difference:", a.symmetric_difference(b), a ^ b)

small = {1, 2}
print("small subset of a?", small.issubset(a), small <= a)
print("a superset of small?", a.issuperset(small), a >= small)

frozen = frozenset([1, 2, 3])    # an immutable set: no add or remove
print("frozenset:", frozen)
```

Output:

```
union: {1, 2, 3, 4, 5, 6} {1, 2, 3, 4, 5, 6}
intersection: {3, 4} {3, 4}
difference: {1, 2} {1, 2}
symmetric difference: {1, 2, 5, 6} {1, 2, 5, 6}
small subset of a? True True
a superset of small? True True
frozenset: frozenset({1, 2, 3})
```

## 8. Dictionaries

A dictionary stores key-value pairs inside curly braces. A key is a label and the value is the data stored under it, like a word and its meaning in a real dictionary. Keys must be unique and are usually strings or numbers. Look up a value with `d[key]`, which raises `KeyError` if the key is missing, or with `d.get(key)`, which returns `None` or a default you choose instead.

```python
student = {"name": "Sita", "age": 21, "city": "Pokhara"}
print(student)
print("name:", student["name"])
print("get('age'):", student.get("age"))
print("get('phone'):", student.get("phone"))
print("get with default:", student.get("phone", "not given"))
```

Output:

```
{'name': 'Sita', 'age': 21, 'city': 'Pokhara'}
name: Sita
get('age'): 21
get('phone'): None
get with default: not given
```

Assigning to a new key adds it; assigning to an existing key updates it. `update()` adds or changes several keys at once. `del` removes a key, and `pop(key)` removes it and returns its value.

```python
student = {"name": "Sita", "age": 21}
student["city"] = "Pokhara"             # add a new key
student["age"] = 22                     # update an existing key
print(student)
student.update({"age": 23, "marks": 92})
print(student)
del student["city"]
removed = student.pop("marks")
print("popped:", removed, "->", student)
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))
```

Output:

```
{'name': 'Sita', 'age': 22, 'city': 'Pokhara'}
{'name': 'Sita', 'age': 23, 'city': 'Pokhara', 'marks': 92}
popped: 92 -> {'name': 'Sita', 'age': 23}
keys: ['name', 'age']
values: ['Sita', 23]
items: [('name', 'Sita'), ('age', 23)]
```

A `for` loop over a dictionary gives its keys. Use `.items()` to get the key and the value together. Dictionaries remember the order in which keys were added.

```python
marks = {"Sita": 92, "Aarav": 85, "Bikash": 67}

for name in marks:
    print(name, "->", marks[name])

for name, score in marks.items():
    print(name, "scored", score)

print("total:", sum(marks.values()))
print("is 'Sita' a key?", "Sita" in marks)
```

Output:

```
Sita -> 92
Aarav -> 85
Bikash -> 67
Sita scored 92
Aarav scored 85
Bikash scored 67
total: 244
is 'Sita' a key? True
```

A value can itself be a dictionary. This nested dictionary is a natural way to store records, such as one dictionary per student.

```python
students = {
    "s1": {"name": "Sita", "marks": 92},
    "s2": {"name": "Aarav", "marks": 85},
}
print(students["s2"]["name"])
students["s2"]["marks"] = 88
for student_id, info in students.items():
    print(student_id, info["name"], info["marks"])
```

Output:

```
Aarav
s1 Sita 92
s2 Aarav 88
```

Two more ways to build a dictionary: from two lists with `zip`, or from a list of `(key, value)` tuples.

```python
names = ["Sita", "Aarav", "Bikash"]
scores = [92, 85, 67]
marks = dict(zip(names, scores))
print(marks)

pairs = [("red", "#FF0000"), ("green", "#00FF00")]
colours = dict(pairs)
print(colours)
```

Output:

```
{'Sita': 92, 'Aarav': 85, 'Bikash': 67}
{'red': '#FF0000', 'green': '#00FF00'}
```

## 9. zip and enumerate

`zip` pairs up the items of two or more collections, position by position, and stops at the shortest one. Writing `zip(*pairs)` does the reverse: the star spreads the pairs out as separate arguments, so you get the original collections back. `enumerate` gives you each item together with its index, which saves you from writing `range(len(items))`.

```python
names = ["Sita", "Aarav", "Bikash"]
scores = [92, 85, 67]

for name, score in zip(names, scores):
    print(name, score)

pairs = list(zip(names, scores))
print("pairs:", pairs)

unzipped_names, unzipped_scores = zip(*pairs)
print("unzipped:", unzipped_names, unzipped_scores)

for position, name in enumerate(names, start=1):
    print(position, name)
```

Output:

```
Sita 92
Aarav 85
Bikash 67
pairs: [('Sita', 92), ('Aarav', 85), ('Bikash', 67)]
unzipped: ('Sita', 'Aarav', 'Bikash') (92, 85, 67)
1 Sita
2 Aarav
3 Bikash
```

## 10. Comprehensions

A comprehension builds a new collection from an existing one in a single line. A list comprehension has the form `[expression for item in collection]`. Add `if condition` at the end to keep only some items. Put `value_if_true if condition else value_if_false` at the front to choose between two values for every item.

```python
numbers = [1, 2, 3, 4, 5, 6]

squares = [n * n for n in numbers]
print("squares:", squares)

evens = [n for n in numbers if n % 2 == 0]
print("evens:", evens)

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("labels:", labels)
```

Output:

```
squares: [1, 4, 9, 16, 25, 36]
evens: [2, 4, 6]
labels: ['odd', 'even', 'odd', 'even', 'odd', 'even']
```

Two `for` parts make a nested comprehension. The first `for` is the outer loop. A comprehension inside another comprehension builds a list of lists, such as a matrix.

```python
pairs = [(x, y) for x in [1, 2] for y in ["a", "b"]]
print("pairs:", pairs)

matrix = [[row * 3 + col for col in range(1, 4)] for row in range(3)]
print("matrix:", matrix)
```

Output:

```
pairs: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Curly braces make a dictionary comprehension (with `key: value`) or a set comprehension (with a single value). Comprehensions are perfect for small clean-up jobs such as dropping `None` values or labelling results.

```python
names = ["Sita", "Aarav", "Bikash"]
name_lengths = {name: len(name) for name in names}
print("dict:", name_lengths)

first_letters = {word[0] for word in ["apple", "avocado", "banana"]}
print("set:", sorted(first_letters))

raw = ["Sita", None, "Aarav", None, "Bikash"]
clean = [value for value in raw if value is not None]
print("clean:", clean)

marks = {"Sita": 92, "Rohan": 45, "Maya": 38}
status = {name: "pass" if score >= 40 else "fail" for name, score in marks.items()}
print("status:", status)
```

Output:

```
dict: {'Sita': 4, 'Aarav': 5, 'Bikash': 6}
set: ['a', 'b']
clean: ['Sita', 'Aarav', 'Bikash']
status: {'Sita': 'pass', 'Rohan': 'pass', 'Maya': 'fail'}
```

## 11. Students from a CSV file

This example combines the structures. It reads `datasets/students.csv`, where each line holds `id,name,age,city,marks`, splits every line on commas and builds a list of dictionaries, one per student. Reading files is covered properly in File Handling; here only three lines touch the file. The `DATA_DIR` line finds the `datasets` folder relative to the script, as explained in `datasets/README.md`, so save this code inside the `examples` folder (it is `examples/08_students_highest_marks.py`).

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

students = []
with open(DATA_DIR / "students.csv", encoding="utf-8") as file:
    header = file.readline()            # read and ignore the first line
    for line in file:
        parts = line.strip().split(",")
        students.append({"name": parts[1], "city": parts[3], "marks": int(parts[4])})

print("students read:", len(students))
print("first:", students[0])

top = students[0]
for student in students:
    if student["marks"] > top["marks"]:
        top = student
print("highest marks:", top["name"], top["marks"])

cities = {student["city"] for student in students}
print("cities:", sorted(cities))
```

Output:

```
students read: 10
first: {'name': 'Aarav Sharma', 'city': 'Kathmandu', 'marks': 85}
highest marks: Kiran Adhikari 95
cities: ['Bhaktapur', 'Biratnagar', 'Butwal', 'Dharan', 'Kathmandu', 'Lalitpur', 'Pokhara']
```

## 12. Comparison tables

| `append(x)` | `insert(i, x)` |
|---|---|
| adds at the end | adds at index `i` |
| one argument | two arguments |
| fast | slower, later items shift right |

| `pop(i)` | `remove(x)` |
|---|---|
| takes an index | takes a value |
| returns the removed item | returns `None` |
| default is the last item | removes the first match only |

| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Written as | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Ordered? | yes | yes | no | yes (insertion order) |
| Mutable? | yes | no | yes | yes |
| Duplicates? | yes | yes | no | keys no, values yes |
| Access by | index | index | `in` only | key |
| Use it for | a sequence that changes | fixed data, records | unique items, membership tests | lookups by name |

## Common mistakes

- `marks = marks.sort()` -> the list becomes `None`; call `marks.sort()` on its own or use `sorted(marks)`.
- `copy = original` and then changing `copy` -> the original changes too; use `original.copy()`.
- `(2)` is an integer, not a tuple -> write `(2,)` with a comma.
- `{}` makes an empty dictionary, not a set -> write `set()`.
- `student["phone"]` on a missing key -> `KeyError`; use `student.get("phone")` or check with `in` first.
- `numbers.remove(99)` when 99 is not there -> `ValueError`; check with `in` first, or use `discard()` on a set.

## Summary

- A list is ordered and mutable; index with `[i]`, slice with `[a:b]`, change with its methods.
- `sorted()` returns a new list; `.sort()` changes the list and returns `None`.
- Assigning a list to another name shares it; `.copy()` makes a separate list.
- A tuple is an immutable list, written with parentheses; unpack it into names in one line.
- A set holds unique items and supports union, intersection and difference.
- A dictionary maps keys to values; `get()` is the safe way to look up a key.
- `zip` pairs collections, `enumerate` numbers items, and comprehensions build collections in one line.
- Choose: list for sequences, tuple for fixed records, set for uniqueness, dict for lookups.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Functions](../05-functions/README.md) | [Next: The collections Module](../07-collections-module/README.md) | [Home](../README.md)
