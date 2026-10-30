# Exception Handling

An exception is an error that happens while a program is running, such as dividing by zero or opening a file that does not exist. Exception handling lets your program notice the problem, deal with it and carry on instead of crashing, which is what every real program needs.

## What you will learn

- The difference between syntax errors and runtime errors (exceptions)
- What a crash looks like and how `try`/`except` prevents it
- Catching one exception, several exceptions, or a tuple of exceptions, and reading the message with `as`
- The `else` and `finally` blocks and the full `try`/`except`/`else`/`finally` flow
- The common built-in exceptions and what causes each one
- Raising exceptions with `raise`, re-raising them, and why a bare `except` is a bad habit
- Writing your own exception classes
- Small programs: safe division, valid input, a bank account, an ATM, a login and a messy data file

Some code blocks read files from the `datasets` folder. They start with a `DATA_DIR` line that finds that folder relative to the script, so save them as `.py` files inside this topic's `examples` folder before running them.

## 1. Errors versus exceptions

There are two kinds of errors. A **syntax error** is a mistake in how the code is written, like a missing bracket. Python finds it before running anything, so nothing happens until you fix it. Save the two lines below as `hello.py` and run the file to see the message.

```python
print("Hello"
print("World")
```

Output:

```
  File "hello.py", line 1
    print("Hello"
         ^
SyntaxError: '(' was never closed
```

A **runtime error**, also called an exception, happens while the program is running. The code is written correctly, but something goes wrong with the data: a list is shorter than expected, a string cannot become a number, a file is missing. These are the errors this topic is about.

## 2. What happens without handling

When an exception is not handled, Python stops the program at that line and prints a traceback. A traceback shows where the error happened and what kind it was. The lines after the error never run. Save the code as `crash.py` to get the same file name in the traceback.

```python
numbers = [10, 20, 30]
print("Before the error")
print(numbers[5])
print("After the error")
```

Output:

```
Before the error
Traceback (most recent call last):
  File "crash.py", line 3, in <module>
    print(numbers[5])
          ~~~~~~~^^^
IndexError: list index out of range
```

With `try` and `except` the program handles the problem and continues. Put the risky code inside `try`. If an exception happens there, Python jumps to the matching `except` block, runs it, and then carries on after the whole statement.

```python
numbers = [10, 20, 30]
print("Before the error")
try:
    print(numbers[5])
except IndexError:
    print("There is no item at position 5")
print("After the error")
```

Output:

```
Before the error
There is no item at position 5
After the error
```

## 3. Catching a specific exception

Name the exception you expect after `except`. Here `int()` raises `ValueError` when the text is not a number. Only that error is caught; any other error would still stop the program, which is what you want, because an unexpected error means a bug you need to see.

```python
text = "abc"

try:
    number = int(text)
    print("Number:", number)
except ValueError:
    print(f"'{text}' is not a number")
```

Output:

```
'abc' is not a number
```

## 4. Several except blocks

One `try` can have several `except` blocks, one for each kind of problem. Python runs the first block whose exception type matches. The function below can fail in three different ways, and each way gets its own message.

```python
def describe(value, index):
    colours = ["red", "green", "blue"]
    try:
        number = int(value)
        print("Share:", 100 / number)
        print("Colour:", colours[index])
    except ValueError:
        print(f"{value!r} is not a whole number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except IndexError:
        print("No colour at that index")


describe("4", 1)
describe("four", 1)
describe("0", 1)
describe("4", 7)
```

Output:

```
Share: 25.0
Colour: green
'four' is not a whole number
Cannot divide by zero
Share: 25.0
No colour at that index
```

## 5. A tuple of exceptions

When several exceptions should be handled the same way, list them in a tuple (round brackets) after `except`. `float("abc")` raises `ValueError` and `float(None)` raises `TypeError`, but both just mean "not a number".

```python
def to_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


print(to_number("3.5"))
print(to_number("abc"))
print(to_number(None))
```

Output:

```
3.5
0.0
0.0
```

## 6. except ... as e

`as` gives the exception object a name so you can print its message or look at its type. The name is often `e` or `error`. Printing the object shows the message Python would have shown in the traceback.

```python
try:
    int("ten")
except ValueError as error:
    print("Something went wrong:", error)
    print("Type of error:", type(error).__name__)
```

Output:

```
Something went wrong: invalid literal for int() with base 10: 'ten'
Type of error: ValueError
```

## 7. else

The `else` block runs only when the `try` block finished without any exception. It keeps the "success" code separate from the risky code, so an error in the success code is not caught by mistake.

```python
for text in ["42", "forty-two"]:
    try:
        number = int(text)
    except ValueError:
        print(f"Could not convert {text!r}")
    else:
        print(f"Converted {text!r} to {number}, doubled is {number * 2}")
```

Output:

```
Converted '42' to 42, doubled is 84
Could not convert 'forty-two'
```

## 8. finally

The `finally` block runs every time, whether there was an exception or not, and even if the `try` block used `return`. That makes it the right place for cleanup: closing a file, closing a database or network connection, or printing a final message.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

file = open(DATA_DIR / "numbers.txt", encoding="utf-8")
try:
    total = sum(int(line) for line in file)
    print("Total:", total)
finally:
    file.close()
    print("File closed:", file.closed)
```

Output:

```
Total: 759
File closed: True
```

For files, the `with` statement does this closing for you, so `finally` is mostly used for other resources. The next example shows that `finally` runs even when the error is not caught inside the function.

```python
def risky(divisor):
    try:
        return 10 / divisor
    finally:
        print("cleanup for divisor", divisor)


print(risky(2))
try:
    risky(0)
except ZeroDivisionError:
    print("caught the error after cleanup")
```

Output:

```
cleanup for divisor 2
5.0
cleanup for divisor 0
caught the error after cleanup
```

## 9. The full flow

All four parts can appear together, in this order: `try`, one or more `except`, `else`, `finally`. The table shows which blocks run in each case, and the code shows both cases.

| What happened in `try` | `except` runs | `else` runs | `finally` runs |
|---|---|---|---|
| no exception | no | yes | yes |
| a matching exception | yes | no | yes |

```python
for divisor in [4, 0]:
    try:
        print(f"Trying 20 / {divisor}")
        result = 20 / divisor
    except ZeroDivisionError:
        print("  except: division by zero")
    else:
        print("  else: result is", result)
    finally:
        print("  finally: done")
```

Output:

```
Trying 20 / 4
  else: result is 5.0
  finally: done
Trying 20 / 0
  except: division by zero
  finally: done
```

## 10. Common built-in exceptions

Python has many built-in exception types. These are the ones a beginner meets most.

| Exception | Cause |
|---|---|
| `ZeroDivisionError` | dividing a number by zero |
| `ValueError` | the type is right but the value is wrong, such as `int("abc")` |
| `TypeError` | an operation on the wrong type, such as adding a string to a number |
| `IndexError` | a list or string index that does not exist |
| `KeyError` | a dictionary key that does not exist |
| `FileNotFoundError` | opening a file that is not there |
| `AttributeError` | using a method or attribute an object does not have |
| `NameError` | using a variable that has not been defined |

The code below triggers each one on purpose and prints its name and message. `lambda:` makes a tiny function out of each expression, so the expression only runs inside the `try` block.

```python
def show_error(action):
    try:
        action()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


show_error(lambda: 10 / 0)
show_error(lambda: int("abc"))
show_error(lambda: "age: " + 20)
show_error(lambda: [1, 2, 3][5])
show_error(lambda: {"a": 1}["b"])
show_error(lambda: open("no_such_file.txt"))
show_error(lambda: "hello".push("x"))
show_error(lambda: undefined_name)
```

Output:

```
ZeroDivisionError: division by zero
ValueError: invalid literal for int() with base 10: 'abc'
TypeError: can only concatenate str (not "int") to str
IndexError: list index out of range
KeyError: 'b'
FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'
AttributeError: 'str' object has no attribute 'push'
NameError: name 'undefined_name' is not defined
```

## 11. Why a bare except is bad

`except:` with no exception name catches everything, including typos in your own code and even the Ctrl+C that stops a program. The bug stays hidden and the function quietly returns a wrong answer. Always name the exception you expect. If you truly must catch everything, write `except Exception as error:` and print the error.

```python
def average_bad(values):
    try:
        return sum(values) / len(vlaues)    # typo: vlaues
    except:
        return 0


def average_good(values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0


print(average_bad([1, 2, 3]))
print(average_good([1, 2, 3]))
print(average_good([]))
```

Output:

```
0
2.0
0
```

The bare `except` swallowed the `NameError` caused by the typo and returned 0 for a list whose average is 2.0. With a specific `except`, the typo would have crashed the program and you would have found it straight away.

## 12. raise

`raise` creates an exception on purpose. Use it when a function receives data it cannot work with. Give the exception a clear message; the caller can catch it like any other exception.

```python
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"age {age} is out of range")
    print("Age set to", age)


set_age(25)
try:
    set_age(-3)
except ValueError as error:
    print("Rejected:", error)
```

Output:

```
Age set to 25
Rejected: age -3 is out of range
```

## 13. Re-raising

Sometimes a function wants to do something when an error happens, such as writing a log message, but it cannot fix the problem. A bare `raise` inside `except` sends the same exception onward to the caller.

```python
def load_setting(settings, key):
    try:
        return settings[key]
    except KeyError:
        print(f"(log) setting {key!r} is missing")
        raise


settings = {"theme": "dark"}
try:
    load_setting(settings, "font")
except KeyError as error:
    print("Caller also saw the error:", error)
```

Output:

```
(log) setting 'font' is missing
Caller also saw the error: 'font'
```

## 14. Custom exceptions

You can define your own exception by writing a class that inherits from `Exception`. A class is a blueprint for objects; inheriting means your class gets everything `Exception` can do. Give it an `__init__` that stores useful details and builds the message, then pass the message to `super().__init__()` so that printing the exception shows it. Custom names such as `InvalidAmountError` make `except` blocks read like plain English.

```python
class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Amount must be positive, got {amount}")


def deposit(balance, amount):
    if amount <= 0:
        raise InvalidAmountError(amount)
    return balance + amount


try:
    print(deposit(100, 50))
    print(deposit(100, -20))
except InvalidAmountError as error:
    print("Error:", error)
    print("The bad amount was", error.amount)
```

Output:

```
150
Error: Amount must be positive, got -20
The bad amount was -20
```

## 15. Practical programs

Safe division returns `None` instead of crashing.

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Cannot divide {a} by zero")
        return None


print(safe_divide(10, 2))
print(safe_divide(7, 0))
```

Output:

```
5.0
Cannot divide 7 by zero
None
```

Asking until the user types a valid integer: the loop repeats until `int()` succeeds, and `return` ends the loop.

```python
def ask_for_integer(prompt):
    while True:
        answer = input(prompt)
        try:
            return int(answer)
        except ValueError:
            print("That is not a whole number, try again.")


age = ask_for_integer("Enter your age: ")
print(f"You are {age} years old.")
```

Sample session:

```
Enter your age: abc
That is not a whole number, try again.
Enter your age: 12
You are 12 years old.
```

A bank account with two custom exceptions. Each exception stores the numbers that caused it, so the caller can print a helpful message.

```python
class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Amount must be positive, got {amount}")


class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}: balance is only {balance}")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount


account = BankAccount("Asha", 5000)
for amount in [1500, -200, 10000, 3500]:
    try:
        account.withdraw(amount)
    except InvalidAmountError as error:
        print("Invalid:", error)
    except InsufficientBalanceError as error:
        print(f"Refused: {error} (short by {error.amount - error.balance})")
    else:
        print(f"Withdrew {amount}, balance is now {account.balance}")
```

Output:

```
Withdrew 1500, balance is now 3500
Invalid: Amount must be positive, got -200
Refused: Cannot withdraw 10000: balance is only 3500 (short by 6500)
Withdrew 3500, balance is now 0
```

An ATM that counts the remaining attempts and raises `InvalidPinError`.

```python
class InvalidPinError(Exception):
    def __init__(self, attempts_left):
        self.attempts_left = attempts_left
        super().__init__(f"Wrong PIN, {attempts_left} attempt(s) left")


class ATM:
    def __init__(self, pin):
        self._pin = pin
        self.attempts_left = 3

    def check_pin(self, pin):
        if pin != self._pin:
            self.attempts_left -= 1
            raise InvalidPinError(self.attempts_left)
        print("PIN accepted")


atm = ATM("4321")
for pin in ["1111", "0000", "4321"]:
    try:
        atm.check_pin(pin)
    except InvalidPinError as error:
        print(error)
```

Output:

```
Wrong PIN, 2 attempt(s) left
Wrong PIN, 1 attempt(s) left
PIN accepted
```

A login with two custom exceptions, one for an unknown user and one for a wrong password. The emails and passwords are made up.

```python
class UserNotFoundError(Exception):
    def __init__(self, email):
        super().__init__(f"No account for {email}")


class WrongPasswordError(Exception):
    def __init__(self, email):
        super().__init__(f"Wrong password for {email}")


users = {"asha@example.com": "password123", "bibek@example.com": "secret456"}


def login(email, password):
    if email not in users:
        raise UserNotFoundError(email)
    if users[email] != password:
        raise WrongPasswordError(email)
    return f"Welcome, {email}"


attempts = [
    ("asha@example.com", "password123"),
    ("mina@example.com", "password123"),
    ("bibek@example.com", "wrong"),
]
for email, password in attempts:
    try:
        print(login(email, password))
    except (UserNotFoundError, WrongPasswordError) as error:
        print("Login failed:", error)
```

Output:

```
Welcome, asha@example.com
Login failed: No account for mina@example.com
Login failed: Wrong password for bibek@example.com
```

Reading a data file with broken lines: the code copies `marks.txt`, adds two bad lines, and then reads the copy. Unpacking three values from a line with fewer parts raises `ValueError`, and so does `int("abc")`, so one `except` handles both. The good lines are still processed.

```python
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

original = (DATA_DIR / "marks.txt").read_text(encoding="utf-8")
broken = Path("marks_with_errors.txt")
broken.write_text(original + "Kiran 70 abc 80\nMaya 65\n", encoding="utf-8")

with open(broken, encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        parts = line.split()
        try:
            name = parts[0]
            maths, science, english = parts[1:]
            average = (int(maths) + int(science) + int(english)) / 3
        except ValueError as error:
            print(f"Line {line_number} skipped: {error}")
        else:
            print(f"{name}: {average:.2f}")
```

Output:

```
Aarav: 84.33
Sita: 91.67
Bikash: 62.00
Priya: 80.00
Rohan: 52.33
Anjali: 86.00
Line 7 skipped: invalid literal for int() with base 10: 'abc'
Line 8 skipped: not enough values to unpack (expected 3, got 1)
```

The scripts in [examples/](examples/) contain fuller versions of these programs.

## Common mistakes

- Writing `except:` with no exception name -> name the exception, or use `except Exception as error:` and print it.
- Putting the whole program inside one `try` -> keep only the risky line or two inside `try`, so you know what failed.
- Using a variable inside `except` that was assigned inside `try` -> it may not exist yet; give it a default before `try` or move the code to `else`.
- Catching the wrong type, for example `except ValueError` around `open()` -> check the traceback for the real exception name (`FileNotFoundError`).
- Catching an exception and printing nothing -> at least print the error, otherwise bugs disappear silently.
- Forgetting that `raise` ends the function immediately -> code after `raise` never runs.

## Summary

- A syntax error stops the program before it starts; an exception happens while it runs.
- `try` holds the risky code, `except` handles the error, `else` runs on success and `finally` runs always.
- Catch specific exceptions; use a tuple when several should be handled the same way; `as error` gives you the message.
- Common exceptions: `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, `AttributeError`, `NameError`.
- A bare `except` hides bugs; avoid it.
- `raise` creates an exception; a bare `raise` inside `except` passes it on.
- A custom exception is a class that inherits from `Exception` and builds its message in `__init__`.
- Loops with `try`/`except` are the standard way to keep asking for valid input or to skip bad lines in a file.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: File Handling](../09-file-handling/README.md) | [Next: OOP Basics](../11-oop-basics/README.md) | [Home](../README.md)
