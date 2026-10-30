# Exercises: Regular Expressions

Solve each exercise in a new file. Compare with the files in [solutions/](solutions/) only after you have tried.

Scripts in the `solutions/` folder find the datasets with `Path(__file__).resolve().parents[3] / "datasets"` because they sit three folders below the repository root.

## 1. Starts with Python

**match() at the start.** For each string in `["Python is fun", "I like Python", "python3", "Pythonic code"]`, use `re.match` to check whether it starts with `Python` (capital P) and print `True` or `False`.

Example:

```
Python is fun -> True
I like Python -> False
python3 -> False
Pythonic code -> True
```

## 2. Joining years

**A group inside findall.** Read `datasets/employees.json` as plain text. Use `re.findall` with a pattern that has one group to pull the year out of every `joined` date (format `YYYY-MM-DD`). Print the list of years and how many employees joined after 2020.

Example:

```
Years: ['2021', '2019', '2018', '2022', '2020', '2023', '2021', '2017']
Joined after 2020: 4
```

## 3. Phone check

**fullmatch() for validation.** Validate the numbers `["9801234567", "9741234567", "9601234567", "980123456", "98012345678"]` with the pattern `^(98|97)\d{8}$`. Print `valid` or `invalid` next to each number.

Example:

```
9801234567 valid
9741234567 valid
9601234567 invalid
980123456 invalid
98012345678 invalid
```

## 4. Split into words

**re.split() on punctuation.** Split the sentence `"Hello, world! Regex is fun; is it not?"` into words using `re.split` with a pattern that matches one or more non-word characters. Remove any empty strings and print the words and their count.

Example:

```
['Hello', 'world', 'Regex', 'is', 'fun', 'is', 'it', 'not']
8 words
```

## 5. Hide emails

**re.sub() for privacy.** Replace every email address in `"Write to asha@example.com or support@example.org today"` with `[hidden]` and print the result. Also print how many addresses were replaced (use `re.subn`).

Example:

```
Write to [hidden] or [hidden] today
2 addresses hidden
```

## 6. Capital words

**A set of matches.** Find every word in `datasets/sample_text.txt` that starts with a capital letter. Print how many there are in total and the sorted list of the different ones.

Example:

```
Total capitalised words: 12
Different words: ['English', 'Guido', 'It', ...]
```

## 7. Date converter

**Named groups.** Convert each date in `["2024-03-15", "1999-12-31", "2021-07-04"]` from `YYYY-MM-DD` to `DD/MM/YYYY` using a pattern with the named groups `year`, `month` and `day`.

Example:

```
2024-03-15 -> 15/03/2024
1999-12-31 -> 31/12/1999
2021-07-04 -> 04/07/2021
```

## 8. Password report

**Which rules are missing.** Write `missing_rules(password)` that returns a list of the rules a password fails: `length 8-16`, `uppercase`, `lowercase`, `digit`, `special character`. Check each rule with `re.search`. Test it with `"Strong@123"`, `"weak"`, `"NoDigits!"` and `"alllower123"`.

Example:

```
Strong@123 -> strong
weak -> missing: length 8-16, uppercase, digit, special character
NoDigits! -> missing: digit
alllower123 -> missing: uppercase, special character
```
