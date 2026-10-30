# Exercises: Exception Handling

Solve each exercise in a new file. Compare with the files in [solutions/](solutions/) only after you have tried.

Scripts in the `solutions/` folder find the datasets with `Path(__file__).resolve().parents[3] / "datasets"` because they sit three folders below the repository root.

## 1. Safe division

**Divide without crashing.** Write a function `safe_divide(a, b)` that returns `a / b`. When `b` is zero it should print `Cannot divide by zero` and return `None`. Test it with the pairs (10, 2), (5, 0) and (9, 3).

Example:

```
10 / 2 = 5.0
Cannot divide by zero
5 / 0 = None
9 / 3 = 3.0
```

## 2. Clean the numbers

**Skip the bad values.** You are given the list `["10", "20", "abc", "30", "", "4.5"]`. Convert each item to an integer with `int()`. Add up the ones that work and collect the ones that fail in a separate list. Print the sum and the rejected items.

Example:

```
Sum of valid numbers: 60
Rejected: ['abc', '', '4.5']
```

## 3. Safe lookup

**One function for lists and dictionaries.** Write `get_item(data, key)` that returns `data[key]`. If the key or index does not exist, return the string `"missing"`. Catch `IndexError` and `KeyError` in a single `except` using a tuple. Test with a list and a dictionary.

Example:

```
colours[1] -> green
colours[5] -> missing
ages['Sita'] -> 21
ages['Kiran'] -> missing
```

## 4. Count lines with finally

**Always report.** Write `count_lines(path)` that opens the file, counts its lines and returns the count. If the file does not exist it should return `-1`. Whatever happens, a `finally` block must print `Finished checking <file name>`. Test with `datasets/sample_text.txt` and with a file that does not exist.

Example:

```
Finished checking sample_text.txt
sample_text.txt has 5 lines
Finished checking missing.txt
missing.txt has -1 lines
```

## 5. Valid age

**Keep asking.** Ask for the user's age until they type a whole number between 1 and 120. Use `try/except ValueError` for non-numbers and an `if` for the range. Print `Age accepted: N` at the end.

Example session:

```
Enter your age: twenty
Please type a whole number.
Enter your age: 200
Age must be between 1 and 120.
Enter your age: 20
Age accepted: 20
```

## 6. Negative square root

**A custom error.** Create a class `NegativeNumberError` that subclasses `Exception` and builds the message `Cannot take the square root of <number>` in its `__init__`. Write `square_root(number)` that raises it for negative numbers and otherwise returns `number ** 0.5`. Test with 16, -4 and 2.25.

Example:

```
square_root(16) = 4.0
Error: Cannot take the square root of -4
square_root(2.25) = 1.5
```

## 7. Bank account

**Two custom errors in one class.** Write a `BankAccount` class with `deposit(amount)` and `withdraw(amount)`. Raise `InvalidAmountError` when the amount is zero or negative and `InsufficientBalanceError` when a withdrawal is larger than the balance. Process the list `[("deposit", 500), ("withdraw", 200), ("withdraw", 1000), ("deposit", -50), ("withdraw", 300)]` starting from a balance of 100 and print one line per operation.

Example:

```
deposit 500 -> balance 600
withdraw 200 -> balance 400
withdraw 1000 -> error: Cannot withdraw 1000, balance is 400
deposit -50 -> error: Amount must be positive, got -50
withdraw 300 -> balance 100
```

## 8. Marks file report

**Broken lines.** Copy `datasets/marks.txt` to `output_marks_broken.txt` next to your script and add the lines `Kiran 70 abc 80` and `Maya 65`. Read the new file. For each good line print the name and the average; for each bad line print the line number and the reason. At the end print how many lines were good and how many were skipped.

Example:

```
Aarav: 84.33
...
Line 7 skipped: invalid literal for int() with base 10: 'abc'
Line 8 skipped: not enough values to unpack (expected 3, got 1)
Good lines: 6, skipped lines: 2
```
