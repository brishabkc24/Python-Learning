# Functions: Exercises

Solve each exercise in its own file. Solutions are in the [solutions](solutions/) folder, named by exercise number. Try each one before looking.

## 1. Greet with a default

**Greeting function.** Write a function `greet(name, greeting="Hello")` that prints `<greeting>, <name>!`. Call it once with only a name and once with both arguments.

Example:

```
Hello, Sita!
Good evening, Aarav!
```

## 2. Rectangle area

**Return a value.** Write a function `area(width, height)` that returns the area of a rectangle. Use it to print the area of a 5 by 3 rectangle and a 2.5 by 4 rectangle.

Example:

```
Area of 5 x 3 = 15
Area of 2.5 x 4 = 10.0
```

## 3. Even or odd

**Boolean return.** Write a function `is_even(number)` that returns `True` when the number is even and `False` otherwise. Use it in a loop to print every even number from 1 to 10 on one line.

Example:

```
2 4 6 8 10
```

## 4. Average of any count

**Using `*args`.** Write a function `average(*numbers)` that returns the average of all the numbers passed to it. If no numbers are passed, it should return `0`.

Example:

```
average(10, 20, 30) = 20.0
average(5) = 5.0
average() = 0
```

## 5. Reverse and palindrome

**Functions calling functions.** Write `reverse_text(text)` that builds and returns the reversed string with a loop. Then write `is_palindrome(text)` that returns `True` when the lower-case text reads the same both ways, using `reverse_text` to do it.

Example:

```
reverse_text('python') = nohtyp
is_palindrome('Level') = True
is_palindrome('python') = False
```

## 6. Primes up to a limit

**Reusing a helper.** Write `is_prime(number)` and then `primes_up_to(limit)` that returns a list of every prime from 2 up to `limit`, using `is_prime`. Print the primes up to 50 and how many there are.

Example:

```
Primes up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Count: 15
```

## 7. Sum of digits with recursion

**Recursion.** Write a recursive function `sum_of_digits(number)` that returns the sum of the digits of a positive integer. The base case is a number with one digit. Test it with 4729 and 10000.

Example:

```
sum_of_digits(4729) = 22
sum_of_digits(10000) = 1
```

## 8. Students by marks

**Lambda, sorted, map and filter.** Start with this list of `(name, marks)` tuples: `[("Aarav", 85), ("Sita", 92), ("Bikash", 67), ("Priya", 78), ("Kiran", 95)]`. Print the top three students sorted by marks (highest first), a list of all names made with `map`, and the names of students with more than 80 marks made with `filter`.

Example:

```
Top 3: [('Kiran', 95), ('Sita', 92), ('Aarav', 85)]
Names: ['Aarav', 'Sita', 'Bikash', 'Priya', 'Kiran']
Above 80: ['Aarav', 'Sita', 'Kiran']
```
