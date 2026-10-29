# Data Structures: Exercises

Solve each exercise in its own file. Solutions are in the [solutions](solutions/) folder, named by exercise number. Try each one before looking.

## 1. Shopping list

**List methods.** Start with `["milk", "bread", "eggs"]`. Add `"butter"` at the end, insert `"rice"` at the start, remove `"bread"`, then sort the list. Print the list after every step.

Example:

```
['milk', 'bread', 'eggs', 'butter']
['rice', 'milk', 'bread', 'eggs', 'butter']
['rice', 'milk', 'eggs', 'butter']
['butter', 'eggs', 'milk', 'rice']
```

## 2. Slices

**Slicing.** Make a list of the numbers 1 to 10 with `list(range(1, 11))`. Print the first three, the last three, every second number and the list reversed, using slices only.

Example:

```
First three: [1, 2, 3]
Last three: [8, 9, 10]
Every second: [1, 3, 5, 7, 9]
Reversed: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## 3. Points as tuples

**Tuples and unpacking.** Store the points `(3, 4)`, `(6, 8)` and `(1, 1)` in a list. Loop over the list, unpack each point into `x` and `y`, and print its distance from the origin, which is `(x * x + y * y) ** 0.5`. Then print the point with the greatest distance.

Example:

```
(3, 4) -> 5.0
(6, 8) -> 10.0
(1, 1) -> 1.4142135623730951
Farthest: (6, 8)
```

## 4. Common friends

**Set operations.** Sita's friends are `{"Aarav", "Bikash", "Priya", "Kiran"}` and Maya's friends are `{"Bikash", "Kiran", "Nabin"}`. Print the friends they share, the friends only Sita has, and everyone in either list. Print each result sorted.

Example:

```
Shared: ['Bikash', 'Kiran']
Only Sita: ['Aarav', 'Priya']
Everyone: ['Aarav', 'Bikash', 'Kiran', 'Nabin', 'Priya']
```

## 5. Word counter

**Dictionary counting.** Count how many times each word appears in the sentence `"the cat and the dog and the bird"` using a dictionary and `get()`. Print each word with its count, then the most common word.

Example:

```
the: 3
cat: 1
and: 2
dog: 1
bird: 1
Most common: the
```

## 6. Three comprehensions

**Comprehensions.** Build and print: a list of the squares of the odd numbers from 1 to 15, a dictionary that maps each number from 1 to 5 to its cube, and a set of the lengths of the words in `["apple", "fig", "cherry", "kiwi", "plum"]` (print the set sorted).

Example:

```
Odd squares: [1, 9, 25, 49, 81, 121, 169, 225]
Cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
Word lengths: [3, 4, 5, 6]
```

## 7. Invert a dictionary

**zip and dictionary comprehension.** Start with `marks = {"Sita": 92, "Aarav": 85, "Bikash": 67}`. Build a new dictionary that maps each mark to the name, first with a dictionary comprehension and then with `dict(zip(...))`. Print both and confirm they are equal.

Example:

```
Comprehension: {92: 'Sita', 85: 'Aarav', 67: 'Bikash'}
zip: {92: 'Sita', 85: 'Aarav', 67: 'Bikash'}
Equal: True
```

## 8. Average marks per city

**Putting it together.** Read `datasets/students.csv` the way the lesson did (skip the header, split each line on commas). Build a dictionary that maps each city to a list of marks, print the average marks of every city in alphabetical order rounded to two decimals, and finally the city with the highest average.

Example:

```
Bhaktapur: 95.0
Biratnagar: 45.0
Butwal: 78.0
Dharan: 59.0
Kathmandu: 70.33
Lalitpur: 67.0
Pokhara: 82.5
Highest average: Bhaktapur
```
