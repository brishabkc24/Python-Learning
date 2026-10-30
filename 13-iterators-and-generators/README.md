# Iterators and Generators

An iterator is an object that hands out items one at a time, and a generator is the easiest way to write one. A beginner needs them because they explain how `for` loops really work and let you process data of any size, even a file with millions of lines, without filling up memory.

## What you will learn

- The difference between an iterable and an iterator
- `iter()`, `next()` and `StopIteration`
- What a `for` loop does behind the scenes
- Writing an iterator class with `__iter__` and `__next__`
- Generator functions with `yield`, and how they pause and resume
- Generator expressions and the memory they save
- Infinite generators and generator pipelines
- `count`, `cycle`, `chain` and `islice` from `itertools`

One code block reads `datasets/numbers.txt`. It starts with a `DATA_DIR` line that finds the datasets folder relative to the script, so save it as a `.py` file inside this topic's `examples` folder before running it.

## 1. Iterable versus iterator

An **iterable** is anything you can loop over with `for`: lists, strings, tuples, dictionaries, files. An **iterator** is the object that actually produces the items one by one and remembers where it is. Think of a book as the iterable and a bookmark as the iterator. You get an iterator from an iterable by calling `iter()`. A list has an `__iter__` method but no `__next__` method; the iterator has both.

```python
colours = ["red", "green", "blue"]
print(hasattr(colours, "__iter__"))
print(hasattr(colours, "__next__"))

iterator = iter(colours)
print(hasattr(iterator, "__iter__"))
print(hasattr(iterator, "__next__"))
print(type(iterator).__name__)
```

Output:

```
True
False
True
True
list_iterator
```

| | Iterable | Iterator |
|---|---|---|
| Examples | list, str, tuple, dict, file | `iter(list)`, a generator, a file object |
| Has `__iter__` | yes | yes (returns itself) |
| Has `__next__` | no | yes |
| Remembers a position | no | yes |
| Can be looped over many times | yes | no, once it is used up it stays empty |

## 2. iter() and next()

`iter(x)` returns an iterator for `x`. `next(iterator)` returns the next item and moves the position forward. Each call gives the following item.

```python
colours = ["red", "green", "blue"]
iterator = iter(colours)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```
red
green
blue
```

## 3. StopIteration

When there are no items left, `next()` raises the `StopIteration` exception. This is not a bug; it is the signal that the iterator is finished. You can catch it, or you can give `next()` a second argument which it returns instead of raising.

```python
iterator = iter([1, 2])
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("No more items")

print(next(iterator, "default value"))
```

Output:

```
1
2
No more items
default value
```

## 4. How the for loop works

A `for` loop does three things for you: it calls `iter()` on the iterable, calls `next()` again and again, and stops quietly when `StopIteration` is raised. The code below is the same loop written by hand.

```python
colours = ["red", "green", "blue"]

iterator = iter(colours)
while True:
    try:
        colour = next(iterator)
    except StopIteration:
        break
    print(colour)
```

Output:

```
red
green
blue
```

## 5. A custom iterator class

To make your own iterator, write a class with two methods. `__iter__` returns the iterator itself, and `__next__` returns the next value or raises `StopIteration`. `Countdown` counts from a start value down to 1, and `EvenNumbers` produces the even numbers up to a limit.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current


for number in Countdown(5):
    print(number)

print(list(EvenNumbers(10)))
```

Output:

```
5
4
3
2
1
[2, 4, 6, 8, 10]
```

## 6. Generators with yield

A generator function is a normal function that uses `yield` instead of `return`. Calling it does not run the body; it returns a generator object, which is an iterator. Each `yield` hands out one value. Python writes `__iter__` and `__next__` for you, so the `Countdown` class becomes four lines.

```python
def countdown(start):
    while start >= 1:
        yield start
        start -= 1


for number in countdown(3):
    print(number)

print(list(countdown(5)))
```

Output:

```
3
2
1
[5, 4, 3, 2, 1]
```

## 7. What happens on each next()

When `next()` is called, the generator runs until it reaches a `yield`, hands out that value and **pauses**. All its local variables are kept. The next `next()` call resumes right after the `yield`. When the function body ends, the generator raises `StopIteration`. The print statements below show the pauses.

```python
def three_steps():
    print("  step 1 runs")
    yield "A"
    print("  step 2 runs")
    yield "B"
    print("  step 3 runs")


gen = three_steps()
print("Created, nothing has run yet")
print("got", next(gen))
print("got", next(gen))
try:
    next(gen)
except StopIteration:
    print("finished")
```

Output:

```
Created, nothing has run yet
  step 1 runs
got A
  step 2 runs
got B
  step 3 runs
finished
```

## 8. Generator versus a function with return

A function with `return` builds the whole result, hands it over once and forgets everything. A generator hands over one value at a time and remembers its place. The values are the same; the difference is when they are produced and how much memory they take.

```python
def squares_with_return(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


def squares_with_yield(n):
    for i in range(1, n + 1):
        yield i * i


print(squares_with_return(4))
print(type(squares_with_yield(4)).__name__)
print(list(squares_with_yield(4)))
```

Output:

```
[1, 4, 9, 16]
generator
[1, 4, 9, 16]
```

| | `return` | `yield` |
|---|---|---|
| Values given | one, all at once | many, one at a time |
| Runs when called | yes, immediately | no, only when `next()` or a loop asks |
| Keeps local variables after giving a value | no | yes, until the next `next()` |
| Memory | holds the whole result | holds one value at a time |
| Can be used more than once | the result can | no, a finished generator stays empty |

## 9. Generator expressions versus list comprehensions

A generator expression looks like a list comprehension with round brackets instead of square ones. The list comprehension builds every value immediately; the generator expression builds them on demand. A generator can be looped over only once; after that it is empty. When the generator expression is the only argument of a function, the extra brackets can be dropped.

```python
squares_list = [n * n for n in range(5)]
squares_gen = (n * n for n in range(5))

print(squares_list)
print(type(squares_gen).__name__)
print(list(squares_gen))
print(list(squares_gen))
print(sum(n * n for n in range(5)))
```

Output:

```
[0, 1, 4, 9, 16]
generator
[0, 1, 4, 9, 16]
[]
30
```

## 10. The memory benefit

`sys.getsizeof()` reports how many bytes an object uses. The list grows with the number of items; the generator stays the same size because it only stores where it is, not the values. The exact byte counts can differ a little between computers, but the pattern is always the same.

```python
import sys

squares_list = [n * n for n in range(1000)]
squares_gen = (n * n for n in range(1000))
print("list of 1000     :", sys.getsizeof(squares_list), "bytes")
print("generator of 1000:", sys.getsizeof(squares_gen), "bytes")

million_list = [n for n in range(1_000_000)]
million_gen = (n for n in range(1_000_000))
print("list of a million     :", sys.getsizeof(million_list), "bytes")
print("generator of a million:", sys.getsizeof(million_gen), "bytes")
```

Output:

```
list of 1000     : 8856 bytes
generator of 1000: 200 bytes
list of a million     : 8448728 bytes
generator of a million: 192 bytes
```

## 11. Infinite generators

Because a generator produces values only when asked, it can describe an endless sequence with `while True`. The loop that uses it must stop on its own with `break`, otherwise the program never ends. Never call `list()` on an infinite generator.

```python
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


for n in natural_numbers():
    if n * n > 50:
        print("First number whose square is above 50:", n)
        break

gen = natural_numbers()
print([next(gen) for _ in range(5)])
print("continues with", next(gen))
```

Output:

```
First number whose square is above 50: 8
[1, 2, 3, 4, 5]
continues with 6
```

## 12. A generator pipeline

Generators can be chained so that each one takes its input from the previous one. This is a pipeline. Each stage pulls one item at a time from the stage before it, so the file is read line by line and nothing is stored in memory at once. The pipeline below reads `numbers.txt`, converts each line to an integer, keeps the even numbers and squares them.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"


def read_lines(path):
    with open(path, encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def to_integers(lines):
    for line in lines:
        yield int(line)


def keep_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square(numbers):
    for number in numbers:
        yield number * number


lines = read_lines(DATA_DIR / "numbers.txt")
numbers = to_integers(lines)
evens = keep_even(numbers)
squares = square(evens)

print(list(squares))
```

Output:

```
[144, 7744, 3136, 1156, 4, 784, 36, 2500, 7056]
```

## 13. itertools in brief

The `itertools` module has ready-made iterators. Four of them are worth knowing early. `count` and `cycle` are infinite, so they are usually combined with `islice`, which takes a slice from any iterator.

| Function | What it gives | Example |
|---|---|---|
| `count(start, step)` | numbers from `start`, forever | `count(10, 5)` gives 10, 15, 20, ... |
| `cycle(iterable)` | the items again and again, forever | `cycle("AB")` gives A, B, A, B, ... |
| `chain(a, b, ...)` | the items of `a`, then `b`, and so on | `chain([1, 2], [3])` gives 1, 2, 3 |
| `islice(iterable, stop)` or `islice(iterable, start, stop, step)` | a slice of any iterator | `islice(count(), 3)` gives 0, 1, 2 |

```python
from itertools import chain, count, cycle, islice

print(list(islice(count(10, 5), 4)))
print(list(islice(cycle("AB"), 5)))
print(list(chain([1, 2], (3, 4), "56")))
print(list(islice(count(), 2, 10, 3)))

for seat, name in zip(count(1), ["Aarav", "Sita", "Bikash"]):
    print(f"Seat {seat}: {name}")
```

Output:

```
[10, 15, 20, 25]
['A', 'B', 'A', 'B', 'A']
[1, 2, 3, 4, '5', '6']
[2, 5, 8]
Seat 1: Aarav
Seat 2: Sita
Seat 3: Bikash
```

## Common mistakes

- Calling `next()` directly on a list and getting `TypeError: 'list' object is not an iterator` -> call `iter()` on the list first.
- Looping over the same generator twice and getting nothing the second time -> create a new generator, or store the values in a list if you need them twice.
- Forgetting to raise `StopIteration` in `__next__` -> the `for` loop never ends; add the check at the top of `__next__`.
- Expecting a generator function to run when it is called -> nothing runs until `next()` or a `for` loop asks for a value.
- Printing a generator and seeing `<generator object ...>` -> wrap it in `list()` to see the values.
- Calling `len()` or using an index on a generator -> generators have no length; use a list when you need those.

## Summary

- An iterable can be looped over; an iterator produces the items one at a time with `next()` and remembers its position.
- `iter()` makes an iterator, `next()` takes the next item and `StopIteration` means the end.
- A `for` loop is `iter()` plus repeated `next()` plus catching `StopIteration`.
- An iterator class needs `__iter__` (returns `self`) and `__next__` (returns a value or raises `StopIteration`).
- `yield` turns a function into a generator; the function pauses at each `yield` and resumes on the next `next()`.
- Generator expressions use round brackets, produce values on demand and use far less memory than lists.
- Infinite generators need `break` or `islice`; chained generators form a pipeline that reads one item at a time.
- `itertools.count`, `cycle`, `chain` and `islice` are ready-made iterators.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: OOP Advanced](../12-oop-advanced/README.md) | [Next: Regular Expressions](../14-regular-expressions/README.md) | [Home](../README.md)
