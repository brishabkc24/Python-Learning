# Exercises: Loops

Write each solution in its own `.py` file and run it with `python filename.py`. Solutions are in the `solutions/` folder; try on your own first.

## 1. Countdown

**Task:** Print the numbers from 10 down to 1 on one line, then print `Go!` on the next line.

**Example**

```
10 9 8 7 6 5 4 3 2 1 
Go!
```

## 2. Squares table

**Task:** For each number from 1 to 10, print the number and its square, lined up in two columns.

**Example**

```
 1    1
 2    4
 3    9
 4   16
 5   25
 6   36
 7   49
 8   64
 9   81
10  100
```

## 3. Sum of digits

**Task:** Store a whole number in a variable and add up its digits using `%` and `//` in a `while` loop.

**Example**

```
Sum of the digits of 4521 is 12
```

## 4. Fibonacci numbers

**Task:** Print the first 10 Fibonacci numbers on one line. The sequence starts with 0 and 1, and every later number is the sum of the two before it.

**Example**

```
0 1 1 2 3 5 8 13 21 34 
```

## 5. Number triangle

**Task:** Print a triangle of numbers with 5 rows. Row 1 shows `1`, row 2 shows `1 2`, and so on.

**Example**

```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

## 6. Primes up to 50

**Task:** Print every prime number from 2 to 50 on one line. Use a nested loop with `break` and the loop `else`.

**Example**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
```

## 7. Greatest common divisor

**Task:** Store two positive whole numbers and find their greatest common divisor with a `while` loop. Hint: while the second number is not 0, replace the pair `(a, b)` with `(b, a % b)`. When `b` becomes 0, `a` is the answer.

**Example**

```
GCD of 48 and 18 is 6
```

## 8. Shopping total

**Task:** Keep asking the user for a price until they enter `0`. Then print how many items were entered and the total. Prices may have decimals.

**Example**

```
Enter a price (0 to finish): 45.5
Enter a price (0 to finish): 12
Enter a price (0 to finish): 99.99
Enter a price (0 to finish): 0
Items: 3
Total: 157.49
```
