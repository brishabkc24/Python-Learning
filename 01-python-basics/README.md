# Python Basics

This topic covers the building blocks that every Python program uses: comments, variables, data types, input and output, type conversion and operators. Everything that follows in this repository is built from these pieces.

## What you will learn

- How to write comments and name variables correctly
- The basic data types: int, float, str, bool and None
- How print() and input() work
- How to convert values between types (casting)
- The arithmetic, comparison, logical, assignment, membership and identity operators
- Operator precedence
- How to build neat text with f-strings and str.format()
- Escape sequences and raw strings

## 1. Comments

A comment is a note for people who read the code. It starts with `#` and runs to the end of the line. Python ignores it completely. Use comments to explain why the code does something, not to repeat what the code obviously does.

```python
# This whole line is a comment.
price = 100  # A comment can also follow code on the same line.
print(price)
```

Output:

```
100
```

## 2. Variables and naming rules

A variable is a name that refers to a value. Think of it as a labelled box: the label is the name and the box holds the value. You create a variable by writing the name, then `=`, then the value. This is called assignment. Assigning again replaces the value in the box.

```python
name = "Asha"
age = 21
print(name)
print(age)

age = 22  # the same box now holds a new value
print(age)
```

Output:

```
Asha
21
22
```

Names must follow these rules:

| Rule | Allowed | Not allowed |
|---|---|---|
| Only letters, digits and underscores | `total_marks`, `item2` | `total-marks`, `total marks` |
| Cannot start with a digit | `marks1` | `1marks` |
| Cannot be a keyword (a word Python reserves, such as `if`, `for`, `class`) | `class_name` | `class` |
| Case sensitive: `Age` and `age` are two different variables | `age` | |

The Python convention is `snake_case`: lower-case words joined by underscores, for example `student_name`. Choose names that say what the value is.

```python
student_name = "Ravi"
Student_Name = "Meera"  # a different variable because of the capital letters
print(student_name)
print(Student_Name)
```

Output:

```
Ravi
Meera
```

You can print the full list of keywords with the `keyword` module:

```python
import keyword

print(keyword.kwlist)
```

Output:

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 3. Data types and type()

Every value has a type. The type decides what you can do with the value: you can add numbers, but you cannot add a number to a piece of text. The built-in function `type()` tells you the type of any value.

| Type | Meaning | Examples |
|---|---|---|
| `int` | whole number | `42`, `-7`, `0` |
| `float` | number with a decimal point | `3.14`, `-0.5`, `2.0` |
| `str` | text (a string of characters) | `"hello"`, `'A'`, `"42"` |
| `bool` | truth value | `True`, `False` |
| `NoneType` | the single value `None`, meaning "no value" | `None` |

```python
count = 10
price = 99.5
label = "Notebook"
in_stock = True
discount = None

print(type(count))
print(type(price))
print(type(label))
print(type(in_stock))
print(type(discount))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

Note that `"42"` with quotes is a string, not a number. You cannot do arithmetic with it until you convert it (section 6).

## 4. print() with several values, sep and end

`print()` accepts several values separated by commas and prints them with one space between them. The `sep` option changes that separator. The `end` option changes what is printed after the last value; the default is a newline, which is why each `print()` normally starts a new line.

```python
print("Total:", 42, "items")
print("red", "green", "blue", sep=", ")
print("2024", "06", "15", sep="-")
print("Loading", end="...")
print("done")
```

Output:

```
Total: 42 items
red, green, blue
2024-06-15
Loading...done
```

## 5. input() always returns a string

`input()` shows a message, waits for the user to type something and press Enter, then returns what was typed. The result is always a string, even when the user types a number. Suppose the file `C:\code\age.py` contains:

```python
age = input("How old are you? ")
print(type(age))
print(age + 1)
```

If the user types `20`, the output is:

```
How old are you? 20
<class 'str'>
Traceback (most recent call last):
  File "C:\code\age.py", line 3, in <module>
    print(age + 1)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Python refuses to add a string and a number. The fix is to convert the string first, which the next section explains.

## 6. Type casting

Casting means converting a value from one type to another. Python does some conversions on its own (implicit casting). When you mix an `int` and a `float` in arithmetic, the result is a `float`:

```python
total = 3 + 1.5
print(total)
print(type(total))
```

Output:

```
4.5
<class 'float'>
```

Every other conversion you ask for yourself (explicit casting) with these functions:

| Function | Converts to | Notes |
|---|---|---|
| `int(x)` | whole number | `int(3.99)` is `3`: it cuts off the decimals, it does not round. `int("42")` works, `int("4.2")` does not. |
| `float(x)` | decimal number | `float("2.5")` is `2.5`; `float(7)` is `7.0` |
| `str(x)` | text | `str(3.5)` is `"3.5"` |
| `bool(x)` | True or False | `0`, `0.0`, `""` and `None` become `False`; everything else becomes `True` |

```python
print(int("42") + 1)
print(int(3.99))
print(float("2.5") * 2)
print(float(7))
print(str(100) + " points")
print(bool(0), bool(5), bool(""), bool("hi"))
```

Output:

```
43
3
5.0
7.0
100 points
False True False True
```

This fixes the `input()` problem from section 5:

```python
age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```

If the user types `20`:

```
How old are you? 20
Next year you will be 21
```

Converting text that is not a number raises a `ValueError`. Suppose the file `C:\code\convert.py` contains:

```python
number = int("twelve")
```

Output:

```
Traceback (most recent call last):
  File "C:\code\convert.py", line 1, in <module>
    number = int("twelve")
ValueError: invalid literal for int() with base 10: 'twelve'
```

## 7. Operators

An operator is a symbol that does something with values. The values it works on are called operands.

**Arithmetic operators**

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | addition | `7 + 2` | `9` |
| `-` | subtraction | `7 - 2` | `5` |
| `*` | multiplication | `7 * 2` | `14` |
| `/` | division (always gives a float) | `7 / 2` | `3.5` |
| `//` | floor division (drops the remainder) | `7 // 2` | `3` |
| `%` | modulus (the remainder) | `7 % 2` | `1` |
| `**` | exponent (power) | `7 ** 2` | `49` |

```python
print(7 + 2, 7 - 2, 7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(7 ** 2)
print(10 / 5)
```

Output:

```
9 5 14
3.5
3
1
49
2.0
```

**Comparison operators**

They compare two values and give a `bool`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 5` | `False` |
| `>` | greater than | `5 > 3` | `True` |
| `<` | less than | `5 < 3` | `False` |
| `>=` | greater than or equal to | `5 >= 5` | `True` |
| `<=` | less than or equal to | `5 <= 3` | `False` |

```python
marks = 72
print(marks == 72)
print(marks != 72)
print(marks >= 40)
print(marks < 40)
```

Output:

```
True
False
True
False
```

**Logical operators**

They combine `bool` values.

| Operator | Result is `True` when | Example | Result |
|---|---|---|---|
| `and` | both sides are `True` | `5 > 3 and 2 > 1` | `True` |
| `or` | at least one side is `True` | `5 > 3 or 2 > 9` | `True` |
| `not` | the value is `False` | `not 5 > 3` | `False` |

```python
age = 25
has_id = False
print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)
```

Output:

```
False
True
True
```

**Assignment operators**

They store a value, or update a variable in place.

| Operator | Example | Same as |
|---|---|---|
| `=` | `x = 5` | store 5 in x |
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |

```python
x = 5
x += 2
print(x)
x -= 1
print(x)
x *= 3
print(x)
x /= 4
print(x)
```

Output:

```
7
6
18
4.5
```

**Membership operators**

They test whether a value is inside a string or a collection.

| Operator | Example | Result |
|---|---|---|
| `in` | `"a" in "cat"` | `True` |
| `not in` | `"a" not in "cat"` | `False` |

```python
print("a" in "cat")
print("x" in "cat")
print(3 in [1, 2, 3])
print(9 not in [1, 2, 3])
```

Output:

```
True
False
True
True
```

**Identity operators**

`is` and `is not` test whether two names refer to the very same object in memory, not whether their values are equal. Use `==` to compare values. The usual place for `is` is checking for `None`.

```python
result = None
print(result is None)
print(result is not None)

first = [1, 2, 3]
second = [1, 2, 3]
print(first == second)
print(first is second)
```

Output:

```
True
False
True
False
```

The two lists hold equal values, so `==` says `True`, but they are two separate boxes, so `is` says `False`.

## 8. Operator precedence

Precedence decides which operator runs first when several appear in one expression, just as multiplication comes before addition in arithmetic. Operators with the same priority run from left to right. Brackets always win, so use them whenever the order is not obvious.

| Priority | Operators | Note |
|---|---|---|
| 1 (highest) | `()` | brackets |
| 2 | `**` | exponent |
| 3 | `-x`, `+x` | negative and positive sign |
| 4 | `*`, `/`, `//`, `%` | multiply and divide |
| 5 | `+`, `-` | add and subtract |
| 6 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is`, `is not` | comparisons |
| 7 | `not` | |
| 8 | `and` | |
| 9 (lowest) | `or` | |

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 * 2)
print(10 - 4 - 3)
print(5 > 3 and 2 + 2 == 4)
print(not True or True)
```

Output:

```
14
20
16
3
True
True
```

In the last line `not` runs before `or`, so Python reads it as `(not True) or True`.

## 9. f-strings and str.format()

An f-string is a string with the letter `f` before the opening quote. Anything inside curly braces `{}` is evaluated and placed into the text. This is the easiest way to mix text and values.

```python
name = "Asha"
marks = 87.5
items = 3
print(f"{name} scored {marks} marks.")
print(f"Twice the items: {items * 2}")
print(f"Name in capitals: {name.upper()}")
```

Output:

```
Asha scored 87.5 marks.
Twice the items: 6
Name in capitals: ASHA
```

A format spec after a colon controls how the value is shown:

| Spec | Meaning | Example | Result |
|---|---|---|---|
| `:.2f` | 2 digits after the decimal point | `f"{3.14159:.2f}"` | `3.14` |
| `:8` | minimum width 8 (numbers right aligned, text left aligned) | `f"{42:8}"` | `      42` |
| `:<8`, `:>8`, `:^8` | left, right or centre in width 8 | `f"{'hi':>8}"` | `      hi` |
| `:,` | thousands separator | `f"{1234567:,}"` | `1,234,567` |
| `:,.2f` | separator and 2 decimals together | `f"{1234567.891:,.2f}"` | `1,234,567.89` |

```python
price = 1234567.891
print(f"Rounded: {price:.2f}")
print(f"With commas: {price:,.2f}")
print(f"[{'Item':<10}][{'Qty':>5}]")
print(f"[{'Pen':<10}][{12:>5}]")
print(f"[{'centre':^10}]")
```

Output:

```
Rounded: 1234567.89
With commas: 1,234,567.89
[Item      ][  Qty]
[Pen       ][   12]
[  centre  ]
```

`str.format()` is the older way. The placeholders are empty braces `{}` and the values are passed to `.format()` in order. You can also number the placeholders to reuse a value.

```python
name = "Ravi"
score = 92
print("{} scored {} marks.".format(name, score))
print("{0} scored {1}. Well done, {0}!".format(name, score))
print("Average: {:.1f}".format(85.333))
```

Output:

```
Ravi scored 92 marks.
Ravi scored 92. Well done, Ravi!
Average: 85.3
```

## 10. Escape sequences and raw strings

An escape sequence is a backslash followed by a character. It stands for something that is hard to type inside quotes, such as a new line.

| Sequence | Meaning |
|---|---|
| `\n` | new line |
| `\t` | tab |
| `\\` | one backslash |
| `\"` | a double quote inside a double-quoted string |
| `\'` | a single quote inside a single-quoted string |

```python
print("Line one\nLine two")
print("Name:\tAsha")
print("C:\\Users\\Asha")
print("She said \"hello\"")
print('It\'s a sunny day')
```

Output:

```
Line one
Line two
Name:	Asha
C:\Users\Asha
She said "hello"
It's a sunny day
```

A raw string has `r` before the opening quote. Backslashes inside it are kept exactly as typed, which is useful for Windows paths and, later, regular expressions.

```python
path = r"C:\new_folder\test.txt"
print(path)
```

Output:

```
C:\new_folder\test.txt
```

Without the `r`, the `\n` would become a new line and `\t` a tab.

## 11. The = versus == mistake

`=` stores a value. `==` asks whether two values are equal. Mixing them up is the most common beginner error.

```python
x = 5           # store 5 in x
print(x == 5)   # is x equal to 5?
print(x == 6)
```

Output:

```
True
False
```

Using `=` where a comparison is needed is a `SyntaxError`. Suppose the file `C:\code\compare.py` contains:

```python
x = 5
if x = 5:
    print("five")
```

Output:

```
  File "C:\code\compare.py", line 2
    if x = 5:
       ^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Python even suggests the fix: write `if x == 5:`.

## Common mistakes

- Writing `if x = 5:` -> use `==` to compare; `=` only stores a value.
- Doing arithmetic with the result of `input()` -> wrap it: `age = int(input("Age: "))`.
- Comparing a string with a number, `"5" == 5` is `False` -> convert first, then compare.
- Starting a variable name with a digit, `1st_place = "Asha"` -> start with a letter: `first_place`.
- Using `is` to compare values -> use `==` for values; keep `is` for `None`.
- Expecting `7 / 2` to give `3` -> `/` always gives a float (`3.5`); use `//` for whole-number division.

## Summary

- A comment starts with `#` and is ignored by Python.
- Variables are named boxes; names use letters, digits and underscores, cannot start with a digit and are case sensitive.
- The basic types are `int`, `float`, `str`, `bool` and `None`; `type()` shows the type of a value.
- `print()` takes several values and accepts `sep` and `end`; `input()` always returns a string.
- `int()`, `float()`, `str()` and `bool()` convert between types; a bad conversion raises `ValueError`.
- Arithmetic, comparison, logical, assignment, membership and identity operators each have a fixed priority; brackets come first.
- f-strings put expressions inside `{}` and format specs such as `:.2f` and `:,` control the look.
- `\n`, `\t`, `\\`, `\"` and `\'` are escape sequences; raw strings `r"..."` keep backslashes as typed.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Getting Started](../00-getting-started/README.md) | [Next: Strings](../02-strings/README.md) | [Home](../README.md)
