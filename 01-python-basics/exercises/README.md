# Exercises: Python Basics

Write each solution in its own `.py` file and run it with `python filename.py`. Solutions are in the `solutions/` folder; try on your own first.

## 1. Describe yourself

**Task:** Create four variables: `name` (a string), `age` (an integer), `height` (a float, in metres) and `is_student` (a boolean). Print each value together with its type.

**Example**

```
Asha <class 'str'>
21 <class 'int'>
1.62 <class 'float'>
True <class 'bool'>
```

## 2. Swap two numbers

**Task:** Start with `a = 5` and `b = 10`. Swap the values so that `a` holds 10 and `b` holds 5, then print both. Do it without typing the numbers a second time.

**Example**

```
Before: a = 5, b = 10
After: a = 10, b = 5
```

## 3. Rectangle area

**Task:** Ask the user for the length and the width of a rectangle. Convert the input to floats and print the area and the perimeter with two decimal places.

**Example**

```
Length: 4.5
Width: 3
Area: 13.50
Perimeter: 15.00
```

## 4. Celsius to Fahrenheit

**Task:** Ask for a temperature in Celsius and convert it with the formula `F = C * 9 / 5 + 32`. Print the result with one decimal place.

**Example**

```
Temperature in Celsius: 37
37.0 C is 98.6 F
```

## 5. Seconds to hours, minutes and seconds

**Task:** Ask for a number of seconds (a whole number) and print it as hours, minutes and seconds. Use `//` and `%`.

**Example**

```
Seconds: 3725
1 hour(s), 2 minute(s), 5 second(s)
```

## 6. Simple interest

**Task:** Ask for the principal amount, the yearly rate (in percent) and the number of years. Calculate the simple interest with `interest = principal * rate * years / 100` and print the interest and the total amount, each with a thousands separator and two decimals.

**Example**

```
Principal: 50000
Rate (% per year): 7.5
Years: 3
Interest: 11,250.00
Total: 61,250.00
```

## 7. Receipt

**Task:** Print a receipt for three items (Notebook 45.0, Pen 12.5, Bag 899.99). Use f-string alignment so that names are left aligned in 10 characters and prices are right aligned in 8 characters with two decimals. Finish with a total line.

**Example**

```
Notebook     45.00
Pen          12.50
Bag         899.99
------------------
Total       957.49
```
