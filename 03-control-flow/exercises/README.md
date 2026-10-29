# Exercises: Control Flow

Write each solution in its own `.py` file and run it with `python filename.py`. Solutions are in the `solutions/` folder; try on your own first.

## 1. Positive, negative or zero

**Task:** Store a number in a variable and print whether it is positive, negative or zero.

**Example**

```
-4 is negative
```

## 2. Pass or fail

**Task:** Ask the user for their marks (0 to 100). Print `Pass` when the marks are 40 or more, otherwise print `Fail`.

**Example**

```
Enter your marks: 38
Fail
```

## 3. Divisible by 3 and 5

**Task:** Ask for a whole number. Print `divisible by 3 and 5`, `divisible by 3 only`, `divisible by 5 only` or `divisible by neither`, whichever is true.

**Example**

```
Enter a number: 45
45 is divisible by 3 and 5
```

## 4. Smallest of three

**Task:** Ask for three numbers and print the smallest one. Do it with `if` statements rather than `min()`.

**Example**

```
First number: 12
Second number: 7
Third number: 9
Smallest: 7.0
```

## 5. Day of the week

**Task:** Ask for a number from 1 to 7 and print the matching day name (1 is Monday). Use `match-case`. Print `Invalid day` for anything else.

**Example**

```
Enter a day number (1-7): 3
Wednesday
```

## 6. BMI category

**Task:** Ask for weight in kilograms and height in metres. Calculate BMI with `weight / height ** 2` and print it with one decimal place, followed by the category: under 18.5 is `Underweight`, 18.5 to under 25 is `Normal`, 25 to under 30 is `Overweight`, 30 and above is `Obese`. Use comparison chaining.

**Example**

```
Weight (kg): 70
Height (m): 1.75
BMI: 22.9
Category: Normal
```

## 7. Ticket price

**Task:** Ask for a visitor's age and print the ticket price. Under 5 is free, 5 to 17 pays 50, 18 to 59 pays 100 and 60 or older pays 60. Reject negative ages with the message `Invalid age`.

**Example**

```
Enter age: 64
Ticket price: 60
```
