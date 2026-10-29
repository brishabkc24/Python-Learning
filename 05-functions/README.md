# Functions

A function is a named block of code that does one job. You write it once and call it as many times as you like, which keeps programs short, readable and easy to fix.

## What you will learn

- How to define a function with `def` and how to call it
- The difference between parameters and arguments, and between `return` and `print`
- The four kinds of functions, default values, keyword arguments, `*args` and `**kwargs`
- How variable scope works and why the `global` keyword is best avoided
- Docstrings, `help()`, type hints and lambda functions
- `map`, `filter`, `sorted` with `key`, and `reduce`
- Recursion and the base case that stops it
- Useful built-in functions you will use every day

## 1. Why functions

Suppose you need to print a welcome message in three places. Without a function you copy the same lines three times. If the message changes, you must fix every copy. A function keeps the code in one place, so you fix it once. A function also gives a block of code a name, so the program reads like a list of steps. Think of a function as a recipe: write it once, cook from it many times.

```python
def show_welcome():
    print("Welcome to the shop")
    print("Today everything is 10% off")

show_welcome()
show_welcome()
```

Output:

```
Welcome to the shop
Today everything is 10% off
Welcome to the shop
Today everything is 10% off
```

## 2. Defining and calling a function

The word `def` starts a function definition. After it come the function name, a pair of parentheses and a colon. The indented lines below are the body of the function. Defining a function does not run it. To run it you call it, which means writing its name followed by parentheses.

```python
def say_hello():
    print("Hello!")

print("Before the call")
say_hello()
say_hello()
print("After the calls")
```

Output:

```
Before the call
Hello!
Hello!
After the calls
```

## 3. Parameters and arguments

A parameter is a name inside the parentheses of the definition. It receives a value when the function is called. An argument is the actual value you pass in the call. In `def greet(name)`, `name` is the parameter. In `greet("Sita")`, `"Sita"` is the argument.

```python
def greet(name):
    print("Hello,", name)

def add(a, b):
    print(a, "+", b, "=", a + b)

greet("Sita")
greet("Aarav")
add(2, 3)
add(10, 25)
```

Output:

```
Hello, Sita
Hello, Aarav
2 + 3 = 5
10 + 25 = 35
```

## 4. return vs print

`print` shows a value on the screen and nothing more. `return` sends a value back to the place where the function was called, so the rest of the program can use it. A function that only prints cannot be used inside a calculation. A function with no `return` gives back the special value `None`.

```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(2, 3)
total = add_return(2, 3)
print("Double the total:", total * 2)

result = add_print(4, 5)
print("add_print gave back:", result)
```

Output:

```
5
Double the total: 10
9
add_print gave back: None
```

When Python reaches a `return`, the function stops at once. Any lines after it never run.

## 5. The four kinds of functions

A function may or may not take arguments, and may or may not return a value. That gives four kinds. All four are useful; pick the one that fits the job.

```python
# 1. No arguments, no return value
def show_line():
    print("----------")

# 2. No arguments, with a return value
def get_pi():
    return 3.14159

# 3. Arguments, no return value
def show_square(number):
    print(number, "squared is", number * number)

# 4. Arguments, with a return value
def add(a, b):
    return a + b

show_line()
print("Pi is", get_pi())
show_square(7)
print("3 + 4 =", add(3, 4))
```

Output:

```
----------
Pi is 3.14159
7 squared is 49
3 + 4 = 7
```

## 6. Default parameters

A default value is used when the caller does not pass an argument for that parameter. Write it with `=` in the definition. Parameters with defaults must come after the ones without.

```python
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

def power(base, exponent=2):
    return base ** exponent

greet("Sita")
greet("Sita", "Good morning")
print(power(5))
print(power(5, 3))
```

Output:

```
Hello, Sita!
Good morning, Sita!
25
125
```

## 7. Keyword arguments

Normally arguments are matched to parameters by position: the first argument goes to the first parameter. A keyword argument names the parameter it belongs to, so the order no longer matters and the call is easier to read.

```python
def describe_pet(animal, name):
    print("I have a", animal, "called", name)

describe_pet("dog", "Rex")
describe_pet(name="Rex", animal="dog")
describe_pet("cat", name="Misty")
```

Output:

```
I have a dog called Rex
I have a dog called Rex
I have a cat called Misty
```

Positional arguments must come before keyword arguments in a call.

## 8. *args and **kwargs

Sometimes you do not know how many arguments a function will receive. A parameter written as `*numbers` collects any number of positional arguments into a tuple. A parameter written as `**details` collects any number of keyword arguments into a dictionary. The names `args` and `kwargs` are the common choice, but any name works; the stars do the job.

```python
def total(*numbers):
    print("numbers is a tuple:", numbers)
    return sum(numbers)

print("Total:", total(1, 2, 3))
print("Total:", total(10, 20))

def show_profile(**details):
    print("details is a dict:", details)
    for key, value in details.items():
        print(key, "=", value)

show_profile(name="Sita", age=21, city="Pokhara")
```

Output:

```
numbers is a tuple: (1, 2, 3)
Total: 6
numbers is a tuple: (10, 20)
Total: 30
details is a dict: {'name': 'Sita', 'age': 21, 'city': 'Pokhara'}
name = Sita
age = 21
city = Pokhara
```

## 9. Scope: local and global

Scope is the part of a program where a variable can be seen. A variable created inside a function is local: it exists only while the function runs and cannot be used outside. A variable created at the top level of the file is global: every function can read it.

```python
count = 0                   # global variable

def show_count():
    message = "Count is"    # local variable
    print(message, count)   # reading a global variable is fine

show_count()
print("Outside the function, count is", count)
```

Output:

```
Count is 0
Outside the function, count is 0
```

Using `message` outside the function would give `NameError: name 'message' is not defined`, because it is local.

A function can read a global variable, but assigning to it inside the function creates a new local variable instead. To change the global variable you must write `global count` first.

```python
count = 0

def increase():
    global count
    count = count + 1

increase()
increase()
print("count:", count)
```

Output:

```
count: 2
```

Avoid `global`. When many functions change the same global variable, it becomes hard to tell which one changed it and when. The cleaner way is to pass the value in and return the new value.

```python
def increase(value):
    return value + 1

count = 0
count = increase(count)
count = increase(count)
print("count:", count)
```

Output:

```
count: 2
```

## 10. Docstrings and help()

A docstring is a string written as the first line of a function body. It describes what the function does. Python stores it in `__doc__`, and the built-in `help()` shows it. Good docstrings let other people, and your future self, use the function without reading its code.

```python
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

print(area(3, 4))
print(area.__doc__)
help(area)
```

Output:

```
12
Return the area of a rectangle.
Help on function area in module __main__:

area(width, height)
    Return the area of a rectangle.

```

## 11. Lambda functions

A lambda is a small function written in one line without a name. The syntax is `lambda parameters: expression`. The value of the expression is returned automatically. Lambdas are handy when a function is needed only once, usually as an argument to another function.

```python
square = lambda x: x * x
add = lambda a, b: a + b

print(square(5))
print(add(2, 3))
```

Output:

```
25
5
```

For anything longer than one expression, use `def`.

## 12. map, filter, sorted with key, and reduce

These functions take another function as an argument. `map` applies a function to every item. `filter` keeps the items for which the function returns `True`. `sorted` can take a `key` function that says what to sort by. `reduce` from the `functools` module combines all items into one value by applying a two-argument function again and again.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda n: n * n, numbers))
print("squares:", squares)

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("evens:", evens)

words = ["banana", "fig", "apple", "kiwi"]
print("by length:", sorted(words, key=len))

students = [("Sita", 92), ("Aarav", 85), ("Kiran", 95)]
print("by marks:", sorted(students, key=lambda s: s[1], reverse=True))

product = reduce(lambda a, b: a * b, numbers)
print("product:", product)
```

Output:

```
squares: [1, 4, 9, 16, 25, 36]
evens: [2, 4, 6]
by length: ['fig', 'kiwi', 'apple', 'banana']
by marks: [('Kiran', 95), ('Sita', 92), ('Aarav', 85)]
product: 720
```

`map` and `filter` return special objects, so wrap them in `list()` to see the items.

## 13. Recursion

A recursive function is a function that calls itself. Every recursive function needs a base case: a simple input for which the answer is known and no further call is made. Without a base case the function would call itself forever. The factorial of 5 is `5 * 4 * 3 * 2 * 1`, and the factorial of 0 is 1, so 0 is the base case.

```python
def factorial(n):
    if n == 0:                      # base case
        return 1
    return n * factorial(n - 1)     # recursive case

def fibonacci(n):
    if n <= 1:                      # base cases: fibonacci(0) = 0, fibonacci(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("5! =", factorial(5))
print("fibonacci(8) =", fibonacci(8))
```

Output:

```
5! = 120
fibonacci(8) = 21
```

How `factorial(3)` works: it returns `3 * factorial(2)`, which returns `2 * factorial(1)`, which returns `1 * factorial(0)`, which is the base case and returns 1. The results multiply back up: 1, 1, 2, 6.

## 14. Type hints

A type hint notes the type you expect for each parameter and for the return value. Write `name: type` after a parameter and `-> type` before the colon. Hints make code easier to read and let editors warn you about mistakes. Python itself does not check them, so the program still runs if you pass something else.

```python
def add(a: int, b: int) -> int:
    return a + b

def shout(text: str) -> str:
    return text.upper() + "!"

print(add(2, 3))
print(shout("hello"))
print(add("2", "3"))    # hints are not enforced, so this still runs
```

Output:

```
5
HELLO!
23
```

## 15. Useful built-in functions

Python comes with many functions you can call without writing them. These are the ones you will use most.

| Function | What it does | Example | Result |
|---|---|---|---|
| `len(x)` | number of items | `len([4, 1, 7])` | `3` |
| `sum(x)` | total of the items | `sum([4, 1, 7])` | `12` |
| `min(x)` | smallest item | `min([4, 1, 7])` | `1` |
| `max(x)` | largest item | `max([4, 1, 7])` | `7` |
| `abs(n)` | distance from zero | `abs(-3)` | `3` |
| `round(n, d)` | round to `d` decimals | `round(3.14159, 2)` | `3.14` |
| `sorted(x)` | new sorted list | `sorted([4, 1, 7])` | `[1, 4, 7]` |
| `reversed(x)` | items in reverse order | `list(reversed([4, 1, 7]))` | `[7, 1, 4]` |
| `range(a, b)` | numbers from `a` up to `b - 1` | `list(range(1, 4))` | `[1, 2, 3]` |
| `isinstance(x, t)` | is `x` of type `t`? | `isinstance(7, int)` | `True` |

```python
numbers = [4, 1, 7, -3]

print("len:", len(numbers), " sum:", sum(numbers))
print("min:", min(numbers), " max:", max(numbers))
print("abs:", abs(-3), " round:", round(3.14159, 2))
print("sorted:", sorted(numbers))
print("reversed:", list(reversed(numbers)))
print("range:", list(range(1, 6)))
print("isinstance:", isinstance(7, int), isinstance("7", int))
```

Output:

```
len: 4  sum: 9
min: -3  max: 7
abs: 3  round: 3.14
sorted: [-3, 1, 4, 7]
reversed: [-3, 7, 1, 4]
range: [1, 2, 3, 4, 5]
isinstance: True False
```

## 16. Small programs with functions

Each of these programs puts one job into one function. Notice that every function returns a value and the printing happens outside, which makes the functions easy to reuse.

```python
def add_two(a, b):
    return a + b

def square(number):
    return number * number

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count = count + 1
    return count

def find_largest(values):
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest

print("add_two(3, 4) =", add_two(3, 4))
print("square(9) =", square(9))
print("is_prime(17) =", is_prime(17))
print("is_prime(18) =", is_prime(18))
print("25 C =", celsius_to_fahrenheit(25), "F")
print("vowels in 'Programming' =", count_vowels("Programming"))
print("largest of [3, 9, 2, 7] =", find_largest([3, 9, 2, 7]))
```

Output:

```
add_two(3, 4) = 7
square(9) = 81
is_prime(17) = True
is_prime(18) = False
25 C = 77.0 F
vowels in 'Programming' = 3
largest of [3, 9, 2, 7] = 9
```

## Common mistakes

- Writing `say_hello` without parentheses -> nothing runs; call it with `say_hello()`.
- Forgetting `return` and then using the result -> you get `None`; add `return value` at the end of the function.
- Putting code after `return` -> it never runs; move it before the `return`.
- Writing `def f(a=1, b):` -> `SyntaxError`; parameters with defaults must come last.
- Assigning to a global variable inside a function without `global` -> `UnboundLocalError`; pass the value in and return the new value instead.
- A recursive function with no base case -> `RecursionError`; add an `if` that returns without calling the function again.

## Summary

- `def name(parameters):` defines a function; `name(arguments)` calls it.
- `return` sends a value back; `print` only shows it. A function with no `return` gives `None`.
- Default values, keyword arguments, `*args` and `**kwargs` make calls flexible.
- Variables made inside a function are local; prefer passing values over `global`.
- A docstring explains a function and `help()` shows it.
- `lambda` makes a tiny one-line function, often for `map`, `filter`, `sorted` and `reduce`.
- Recursion needs a base case that stops the calls.
- Type hints document the expected types but are not enforced.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Loops](../04-loops/README.md) | [Next: Data Structures](../06-data-structures/README.md) | [Home](../README.md)
