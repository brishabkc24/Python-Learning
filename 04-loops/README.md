# Loops

A loop repeats a block of code. Instead of writing the same line ten times, you write it once and tell Python how many times to run it, or when to stop. Loops turn a few lines of code into programs that handle any amount of work.

## What you will learn

- `for` loops with `range()`, strings and lists
- `while` loops for repeating until a condition changes
- `break`, `continue` and the `else` clause of a loop
- Nested loops and star patterns
- A first look at `enumerate()` and `zip()`
- How to recognise and stop an infinite loop
- Classic loop programs: sums, tables, factorial, prime check, reversed digits, a login with limited attempts and an ATM menu

## 1. for loops with range()

A `for` loop runs its block once for each item in a sequence. `range()` produces a sequence of whole numbers, which makes it the usual partner of `for`. The loop variable (`number` below) takes each value in turn. Remember that `range()` stops one before the stop value.

| Form | Produces | Example |
|---|---|---|
| `range(stop)` | 0 up to, but not including, `stop` | `range(5)` gives 0, 1, 2, 3, 4 |
| `range(start, stop)` | `start` up to, but not including, `stop` | `range(1, 6)` gives 1, 2, 3, 4, 5 |
| `range(start, stop, step)` | counts in jumps of `step`; a negative step counts down | `range(10, 0, -2)` gives 10, 8, 6, 4, 2 |

```python
for number in range(5):
    print(number, end=" ")
print()

for number in range(1, 6):
    print(number, end=" ")
print()

for number in range(10, 0, -2):
    print(number, end=" ")
print()
```

Output:

```
0 1 2 3 4 
1 2 3 4 5 
10 8 6 4 2 
```

`end=" "` keeps the numbers on one line; the empty `print()` then moves to the next line.

## 2. for loops over strings and lists

A `for` loop can walk through any sequence, not only numbers. With a string it visits one character at a time. With a list (a collection of values in square brackets, covered fully in Data Structures) it visits one item at a time.

```python
for letter in "abc":
    print("Letter:", letter)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
```

Output:

```
Letter: a
Letter: b
Letter: c
Fruit: apple
Fruit: banana
Fruit: cherry
```

## 3. while loops

A `while` loop repeats as long as its condition is `True`. Use it when you do not know in advance how many repeats you need. Something inside the loop must change the condition; otherwise the loop never ends.

```python
count = 1
while count <= 5:
    print("count is", count)
    count += 1
print("Finished, count is now", count)
```

Output:

```
count is 1
count is 2
count is 3
count is 4
count is 5
Finished, count is now 6
```

Use `for` when you know how many times to repeat (or have a sequence to walk through) and `while` when you repeat until something happens.

## 4. break and continue

`break` leaves the loop at once, even if there are items left. `continue` skips the rest of the current round and moves on to the next item. Both work in `for` and `while` loops.

```python
for number in range(1, 10):
    if number == 4:
        break
    print(number, end=" ")
print()

for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number, end=" ")
print()
```

Output:

```
1 2 3 
1 3 5 7 9 
```

## 5. The else clause of a loop

A loop can have an `else` block. It runs when the loop finishes normally, that is, when it was not stopped by `break`. The common use is a search: if the loop ends without finding the item, the `else` block reports that.

```python
numbers = [4, 9, 15, 22]
for number in numbers:
    if number % 7 == 0:
        print("Found a multiple of 7:", number)
        break
else:
    print("No multiple of 7 found")
```

Output:

```
No multiple of 7 found
```

Change `15` to `14` and the loop breaks, so the `else` block is skipped.

## 6. Nested loops

A loop inside another loop is called nested. The inner loop runs completely for every single round of the outer loop. Nested loops are used for tables, grids and patterns.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")
    print()
```

Output:

```
1 2 3 
2 4 6 
3 6 9 
```

The inner `print()` with no arguments ends the row after the inner loop has printed three values.

## 7. Star patterns

Patterns are the classic exercise for nested loops. The outer loop chooses the row, and the inner loop (or string repetition with `*`) prints the stars for that row.

```python
rows = 4

for row in range(1, rows + 1):
    print("*" * row)
print()

for row in range(rows, 0, -1):
    print("*" * row)
print()

for row in range(1, rows + 1):
    print(" " * (rows - row) + "*" * (2 * row - 1))
```

Output:

```
*
**
***
****

****
***
**
*

   *
  ***
 *****
*******
```

The pyramid needs `rows - row` spaces before the stars, and row `n` has `2 * n - 1` stars, so the rows stay centred.

## 8. enumerate() and zip()

Two helpers make common loops shorter. `enumerate()` gives you a counter together with each item, so you do not need to manage a position variable yourself. `zip()` walks through two sequences side by side, pairing the first item with the first, the second with the second, and so on. Both are covered again, with lists and tuples, in Data Structures.

```python
fruits = ["apple", "banana", "cherry"]
for position, fruit in enumerate(fruits, start=1):
    print(position, fruit)

names = ["Asha", "Ravi"]
marks = [88, 72]
for name, mark in zip(names, marks):
    print(name, "scored", mark)
```

Output:

```
1 apple
2 banana
3 cherry
Asha scored 88
Ravi scored 72
```

## 9. Infinite loops and how to stop them

A loop whose condition never becomes `False` is an infinite loop. It happens when you forget to change the variable the condition depends on. If a program seems stuck and prints nothing (or prints the same line again and again), press `Ctrl+C` in the terminal to stop it.

This loop never ends, because `count` is never changed:

```python
count = 1
while count <= 3:
    print("still running")
```

Sometimes an infinite loop is intended: `while True:` runs until a `break` inside it, which is the usual shape for a menu that repeats until the user chooses Exit.

```python
total = 0
while True:
    total += 5
    if total >= 20:
        break
print("Stopped at", total)
```

Output:

```
Stopped at 20
```

## 10. Classic loop programs

Each program below is complete and uses only what this topic has covered.

**Print 1 to 20 and the even numbers**

```python
for number in range(1, 21):
    print(number, end=" ")
print()

for number in range(2, 21, 2):
    print(number, end=" ")
print()
```

Output:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
2 4 6 8 10 12 14 16 18 20 
```

**Sum of the first n natural numbers**

The variable `total` starts at 0 and grows by each number in turn. This "running total" pattern appears everywhere.

```python
n = 10
total = 0
for number in range(1, n + 1):
    total += number
print("Sum of 1 to", n, "is", total)
```

Output:

```
Sum of 1 to 10 is 55
```

**Sum of odd numbers up to 30**

```python
odd_total = 0
for number in range(1, 31, 2):
    odd_total += number
print("Sum of odd numbers up to 30:", odd_total)
```

Output:

```
Sum of odd numbers up to 30: 225
```

**Multiplication table**

```python
table_of = 7
for multiplier in range(1, 11):
    print(f"{table_of} x {multiplier:2} = {table_of * multiplier:2}")
```

Output:

```
7 x  1 =  7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70
```

**Factorial**

The factorial of n (written n!) is 1 x 2 x 3 x ... x n. The product starts at 1, not 0, because anything multiplied by 0 is 0.

```python
n = 6
factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(f"{n}! = {factorial}")
```

Output:

```
6! = 720
```

**Prime check**

A prime number has no divisors except 1 and itself. Try every possible divisor from 2 up to the number itself; the first one that divides exactly proves the number is not prime, so `break`. If the loop finishes without breaking, the `else` block declares it prime.

```python
candidate = 29
for divisor in range(2, candidate):
    if candidate % divisor == 0:
        print(candidate, "is not prime, divisible by", divisor)
        break
else:
    print(candidate, "is prime")
```

Output:

```
29 is prime
```

**Reverse the digits of a number**

`number % 10` gives the last digit and `number // 10` drops it. Each round moves one digit from the end of the number to the end of the result.

```python
number = 12345
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10
print("Reversed:", reversed_number)
```

Output:

```
Reversed: 54321
```

**Login with a maximum of three attempts**

The loop keeps asking while attempts remain and nobody has logged in. The password is fictional and would never be stored in real code.

```python
correct_password = "password123"
attempts_left = 3
logged_in = False

while attempts_left > 0 and not logged_in:
    password = input("Password: ")
    if password == correct_password:
        logged_in = True
    else:
        attempts_left -= 1
        print("Wrong password.", attempts_left, "attempt(s) left.")

if logged_in:
    print("Welcome!")
else:
    print("Account locked.")
```

If the user types `hello` and then `password123`:

```
Password: hello
Wrong password. 2 attempt(s) left.
Password: password123
Welcome!
```

**ATM menu loop**

`while True:` shows the menu again and again; the Exit option breaks out. The balance is kept in a variable that the other options update.

```python
balance = 1000.0

while True:
    print("1. Withdraw  2. Deposit  3. Check balance  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"New balance: {balance:.2f}")
    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        balance += amount
        print(f"New balance: {balance:.2f}")
    elif choice == "3":
        print(f"Current balance: {balance:.2f}")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")
```

If the user deposits 500, withdraws 200 and exits:

```
1. Withdraw  2. Deposit  3. Check balance  4. Exit
Choose an option: 2
Amount to deposit: 500
New balance: 1500.00
1. Withdraw  2. Deposit  3. Check balance  4. Exit
Choose an option: 1
Amount to withdraw: 200
New balance: 1300.00
1. Withdraw  2. Deposit  3. Check balance  4. Exit
Choose an option: 4
Goodbye.
```

## Common mistakes

- Expecting `range(1, 10)` to include 10 -> the stop value is never included; use `range(1, 11)`.
- Forgetting to change the variable in a `while` condition -> the loop runs forever; press `Ctrl+C` and add the update, such as `count += 1`.
- Starting a product at 0, `factorial = 0` -> every multiplication gives 0; start at 1.
- Starting a sum at 1 instead of 0 -> the total is one too high; start running totals at 0.
- Forgetting `end=" "` and getting one number per line -> `print(x, end=" ")` keeps items on one line.
- Putting the `else` of a loop at the wrong indentation -> align `else:` with `for` or `while`, not with the inner `if`.

## Summary

- `for` repeats once per item of a sequence; `range(start, stop, step)` supplies the numbers and never includes `stop`.
- `while` repeats as long as its condition is `True`; something in the loop must change that condition.
- `break` leaves a loop early and `continue` skips to the next round.
- The `else` block of a loop runs only when the loop was not stopped by `break`.
- A nested loop runs its inner loop fully for every round of the outer loop; patterns and tables use this.
- `enumerate()` adds a counter and `zip()` pairs up two sequences.
- `while True:` with a `break` is the standard shape for a menu that repeats until the user exits.
- A running total starts at 0; a running product starts at 1.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Control Flow](../03-control-flow/README.md) | [Next: Functions](../05-functions/README.md) | [Home](../README.md)
