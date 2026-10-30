# Exercises: Iterators and Generators

Solve each exercise in a new file. Compare with the files in [solutions/](solutions/) only after you have tried.

Scripts in the `solutions/` folder find the datasets with `Path(__file__).resolve().parents[3] / "datasets"` because they sit three folders below the repository root.

## 1. Manual iteration

**Letters one by one.** Create an iterator from the string `"abc"` with `iter()`. Use `next()` inside a `while True` loop to print each letter, and stop the loop by catching `StopIteration`. Print `done` at the end.

Example:

```
a
b
c
done
```

## 2. Squares iterator

**An iterator class.** Write a class `Squares(n)` with `__iter__` and `__next__` that produces 1, 4, 9, ... up to n squared. Loop over `Squares(5)` and print the values on one line.

Example:

```
1 4 9 16 25
```

## 3. Fibonacci generator

**A generator with a limit.** Write a generator function `fibonacci_below(limit)` that yields the Fibonacci numbers smaller than `limit`, starting from 0 and 1. Print `list(fibonacci_below(50))`.

Example:

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 4. Non-empty lines

**A file generator.** Write a generator `read_non_empty(path)` that opens the file and yields each stripped line that is not empty. Use it on `datasets/sample_text.txt` and print the number of words in each line.

Example:

```
Line 1: 18 words
Line 2: 16 words
Line 3: 14 words
Line 4: 7 words
Line 5: 13 words
```

## 5. Sum of odd squares

**A generator expression.** Read `datasets/numbers.txt` and use a single generator expression inside `sum()` to add up the squares of the odd numbers. Then build the same values as a list comprehension and print `sys.getsizeof` for both (the exact numbers can differ on your computer).

Example:

```
Sum of odd squares: 24491
List size: 184 bytes
Generator size: 200 bytes
```

## 6. Multiples

**An infinite generator.** Write `multiples_of(k)` that yields k, 2k, 3k, ... forever. Print the first five multiples of 7 using `itertools.islice`, then use a `for` loop with `break` to find the first multiple of 7 above 100.

Example:

```
First five: [7, 14, 21, 28, 35]
First above 100: 105
```

## 7. Chunks

**Groups of a fixed size.** Write a generator `chunks(items, size)` that yields lists of `size` items from any iterable, with a shorter last list if needed. Test it on `range(1, 11)` with size 3.

Example:

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10]
```

## 8. Students pipeline

**Three generators in a row.** Build a pipeline over `datasets/students.csv`: the first generator yields each row from `csv.DictReader`, the second keeps only rows with marks of 70 or more, the third yields the string `"name (marks)"`. Print each result from the last generator.

Example:

```
Aarav Sharma (85)
Sita Rai (92)
...
```
