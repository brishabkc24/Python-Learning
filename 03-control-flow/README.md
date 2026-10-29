# Control Flow

Control flow is how a program decides which lines to run. With `if` statements your code can take different paths depending on the data, which is what makes a program useful instead of fixed.

## What you will learn

- `if`, `if-else` and `if-elif-else`
- Nested `if` statements
- Comparison chaining such as `18 <= age < 60`
- Which values count as `True` and which as `False`
- The conditional expression and `pass`
- `match-case` for choosing between fixed options
- Classic decision programs: voting, odd or even, greatest of three, grades, leap years and a menu calculator

## 1. if

An `if` statement runs a block of code only when its condition is `True`. The condition ends with a colon, and the block below it is indented by four spaces. Indentation is not decoration in Python: it tells Python which lines belong to the `if`. The first line that is not indented is outside the `if` and always runs.

```python
temperature = 31
if temperature > 30:
    print("It is hot today.")
    print("Drink water.")
print("This line always runs.")
```

Output:

```
It is hot today.
Drink water.
This line always runs.
```

## 2. if-else

`else` adds a second block that runs when the condition is `False`. Exactly one of the two blocks runs.

```python
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

Output:

```
7 is odd
```

## 3. if-elif-else

`elif` is short for "else if". Python tests each condition from the top and runs the first block whose condition is `True`, then skips all the rest. The final `else` catches everything that did not match. You can have as many `elif` branches as you need.

```python
marks = 67
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

Output:

```
Grade B
```

The order of the tests matters. Python only reaches `marks >= 60` because `marks >= 80` was `False`. If the tests were written from smallest to largest, `marks >= 40` would win first and 67 would get a C.

## 4. Nested if

An `if` inside another `if` is called nested. The inner `if` is only tested when the outer condition is `True`. Nesting suits questions that only make sense after an earlier answer.

```python
is_citizen = True
age = 16
if is_citizen:
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible: under 18.")
else:
    print("Not eligible: not a citizen.")
```

Output:

```
Not eligible: under 18.
```

## 5. Comparison chaining

Python lets you write a range check the way it is written in maths. `18 <= age < 60` means "age is at least 18 and less than 60". It is the same as `18 <= age and age < 60`, only shorter and easier to read.

```python
age = 35
print(18 <= age < 60)
print(18 <= age and age < 60)

age = 65
print(18 <= age < 60)
```

Output:

```
True
True
False
```

## 6. Truthy and falsy values

An `if` does not need a comparison. Any value can be tested, and Python treats it as either `True` or `False`. Values that count as `False` are called falsy; everything else is truthy.

| Falsy values | Truthy values |
|---|---|
| `False` | `True` |
| `0` and `0.0` | any other number, such as `1`, `-3`, `0.5` |
| `""` (the empty string) | any non-empty string, even `" "` |
| `[]`, `()`, `{}` (empty list, tuple and dictionary) | any collection with at least one item |
| `None` | |

This makes a check such as "did the user type anything?" very short.

```python
name = ""
if name:
    print("Hello,", name)
else:
    print("You did not enter a name.")

items = 3
if items:
    print("You have", items, "items")

print(bool(0), bool(""), bool(None))
print(bool(1), bool("hi"), bool(" "))
```

Output:

```
You did not enter a name.
You have 3 items
False False False
True True True
```

## 7. Conditional expression

A conditional expression chooses between two values on a single line. The form is `value_if_true if condition else value_if_false`. Other languages call this the ternary operator. Use it when you only need to pick one of two values; use a full `if` statement when each branch does more than that.

```python
age = 15
status = "adult" if age >= 18 else "minor"
print(status)

number = 8
print("even" if number % 2 == 0 else "odd")
```

Output:

```
minor
even
```

## 8. pass

`pass` is a statement that does nothing. Every block must contain at least one statement, so `pass` acts as a placeholder for a block you have not written yet. The program runs normally and you can fill the block in later.

```python
balance = 500
if balance < 0:
    pass  # warning message to be written later
else:
    print("Balance is fine.")
```

Output:

```
Balance is fine.
```

## 9. match-case

`match` (available since Python 3.10) compares one value against a series of patterns and runs the first `case` that fits. It is clearer than a long `if-elif` chain when you check one variable against several fixed values, such as a menu choice. Several values can share one branch with `|`. The last line, `case _:`, is the catch-all that runs when nothing else matched.

```python
choice = "2"
match choice:
    case "1":
        print("You chose: new game")
    case "2":
        print("You chose: load game")
    case "3" | "4":
        print("You chose: settings or help")
    case _:
        print("Unknown option")
```

Output:

```
You chose: load game
```

## 10. Classic decision programs

Each program below is complete. They combine the ideas from this topic.

**Vote eligibility**

A person may vote when they are a citizen and at least 18 years old. The eligible case is tested first; the branches after it explain why someone was turned away.

```python
is_citizen = True
age = 20
if is_citizen and age >= 18:
    print("Eligible to vote.")
elif not is_citizen:
    print("Not eligible: not a citizen.")
else:
    print("Not eligible: under 18.")
```

Output:

```
Eligible to vote.
```

**Odd or even**

A number is even when dividing it by 2 leaves no remainder.

```python
number = 24
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

Output:

```
24 is even
```

**Greatest of three numbers**

```python
a = 42
b = 97
c = 65
if a >= b and a >= c:
    greatest = a
elif b >= c:
    greatest = b
else:
    greatest = c
print("Greatest:", greatest)
print("Check with max():", max(a, b, c))
```

Output:

```
Greatest: 97
Check with max(): 97
```

**Grade from GPA**

```python
gpa = 3.2
if 3.6 <= gpa <= 4.0:
    grade = "A"
elif 3.0 <= gpa < 3.6:
    grade = "B"
elif 2.0 <= gpa < 3.0:
    grade = "C"
else:
    grade = "D"
print(f"GPA {gpa} -> grade {grade}")
```

Output:

```
GPA 3.2 -> grade B
```

**Leap year**

A year is a leap year if it is divisible by 4, except that years divisible by 100 are not, unless they are also divisible by 400.

```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

Output:

```
2024 is a leap year
```

**Menu calculator**

```python
first = 10
second = 4
choice = "4"
match choice:
    case "1":
        print(first + second)
    case "2":
        print(first - second)
    case "3":
        print(first * second)
    case "4":
        if second == 0:
            print("Cannot divide by zero.")
        else:
            print(first / second)
    case _:
        print("Unknown option")
```

Output:

```
2.5
```

## Common mistakes

- Forgetting the colon, `if x > 5` -> every `if`, `elif`, `else`, `match` and `case` line ends with `:`.
- Forgetting to indent the block, or mixing tabs and spaces -> indent every line of the block by the same four spaces.
- Writing `if x = 5:` -> `=` assigns; use `==` to compare.
- Testing the broad condition first, `if marks >= 40` before `if marks >= 80` -> order the tests from the most specific to the least.
- Comparing the result of `input()` with a number, `if choice == 1` -> `input()` returns a string, so compare with `"1"` or convert with `int()`.
- Writing `if x == 1 or 2:` -> this is always `True` because `2` is truthy; write `if x == 1 or x == 2:`.

## Summary

- `if` runs a block when its condition is `True`; `else` runs when it is `False`; `elif` adds more tests in between.
- Only the first branch whose condition is `True` runs, so order the tests carefully.
- Nested `if` statements put one decision inside another.
- `18 <= age < 60` is a comparison chain and means `18 <= age and age < 60`.
- `0`, `0.0`, `""`, empty collections and `None` are falsy; everything else is truthy.
- `x if condition else y` picks one of two values on one line.
- `pass` fills a block that has no code yet.
- `match-case` chooses between fixed options; `case _:` catches the rest.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Strings](../02-strings/README.md) | [Next: Loops](../04-loops/README.md) | [Home](../README.md)
