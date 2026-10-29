# Modules and Packages: Exercises

Solve each exercise in its own file. Solutions are in the [solutions](solutions/) folder, named by exercise number. Try each one before looking. Exercises 2 and 3 belong together: exercise 3 imports the module you write in exercise 2, so keep both files in the same folder.

## 1. Three import styles

**Import styles.** Using the `math` module, print the square root of 144 with `import math`, the value of pi rounded to three decimals with `import math as m`, and the factorial of 6 with `from math import factorial`.

Example:

```
sqrt(144) = 12.0
pi rounded = 3.142
factorial(6) = 720
```

## 2. A temperature module

**Your own module.** Write a module with two functions, `c_to_f(celsius)` and `f_to_c(fahrenheit)`, each with a docstring. Under `if __name__ == "__main__":` add a small self-test that prints `c_to_f(100)` and `f_to_c(32)`. The self-test must run when the file is run directly and stay silent when the file is imported. The solution is named `ex02_temperature.py` so that exercise 3 can import it.

Example (running the module directly):

```
Self-test of the temperature module
c_to_f(100) = 212.0
f_to_c(32) = 0.0
```

## 3. Use the temperature module

**Importing your module.** In a new file in the same folder, import the module from exercise 2 and use it to convert 0, 25 and 37 degrees Celsius to Fahrenheit and 98.6 Fahrenheit to Celsius (rounded to one decimal). Also print the module's `__name__`. Notice that the self-test does not print.

Example:

```
0 C = 32.0 F
25 C = 77.0 F
37 C = 98.6 F
98.6 F = 37.0 C
module name: ex02_temperature
```

## 4. Dice rolls

**The random module.** Call `random.seed(7)` so the results repeat, roll a six-sided die 20 times with `random.randint`, store the rolls in a list, then print the list, how many sixes there were, and how many times each face from 1 to 6 came up.

Example:

```
Rolls: [3, 2, 4, 6, 1, 1, 5, 1, 3, 5, 1, 5, 2, 1, 1, 4, 4, 1, 2, 1]
Sixes: 1
Face 1 -> 8
Face 2 -> 3
Face 3 -> 2
Face 4 -> 3
Face 5 -> 3
Face 6 -> 1
```

## 5. Working with dates

**The datetime module.** Make the date 15 August 2005 with `datetime.date`. Print it, print its weekday name with `strftime("%A")`, print the date 100 days later using `datetime.timedelta`, and print the number of days from that date to 1 January 2026.

Example:

```
Birthday: 2005-08-15
Weekday: Monday
100 days later: 2005-11-23
Days from birthday to 2026-01-01: 7444
```

## 6. Describe the numbers file

**The statistics module.** Read `datasets/numbers.txt` (one integer per line) into a list and print the count, mean, median, standard deviation rounded to two decimals, and the smallest and largest values using the `statistics` module and the built-in `min` and `max`.

Example:

```
Count: 20
Mean: 37.95
Median: 31.0
Standard deviation: 30.99
Smallest and largest: 2 99
```

## 7. Use the shapes package from anywhere

**sys.path.** The `shapes` package lives in this lesson's `examples` folder, so a script in another folder cannot import it directly. Build the path to the `examples` folder relative to your script with `pathlib`, append it to `sys.path`, then import `shapes` and print the area of a circle with radius 5 (rounded to two decimals) and of a 7 by 3 rectangle.

Example:

```
Added to sys.path: examples
Circle area, radius 5: 78.54
Rectangle area, 7 x 3: 21
```
