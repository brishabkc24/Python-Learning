# The collections Module: Exercises

Solve each exercise in its own file. Solutions are in the [solutions](solutions/) folder, named by exercise number. Try each one before looking.

## 1. Letter counter

**Counter.** Count the letters in the word `"programming"` with a `Counter`. Print the whole counter, then the three most common letters.

Example:

```
Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
Top three: [('r', 2), ('g', 2), ('m', 2)]
```

## 2. Group by first letter

**defaultdict(list).** Group the words `["apple", "avocado", "banana", "blueberry", "cherry"]` by their first letter using a `defaultdict`. Print each letter with its list of words.

Example:

```
a -> ['apple', 'avocado']
b -> ['banana', 'blueberry']
c -> ['cherry']
```

## 3. Book records

**namedtuple.** Define a `Book` namedtuple with the fields `title`, `year` and `price`. Create a book, print it, print its title by name, then use `_replace` to make a copy with a new price and `_asdict` to show it as a dictionary.

Example:

```
Book(title='Learning Python', year=2021, price=450)
Title: Learning Python
Discounted: Book(title='Learning Python', year=2021, price=400)
As dict: {'title': 'Learning Python', 'year': 2021, 'price': 400}
```

## 4. Sliding average

**deque with maxlen.** Temperature readings arrive one at a time: `[20, 22, 25, 30, 28, 24]`. Keep only the last three in a `deque(maxlen=3)` and, once three are available, print the average of the last three after every new reading.

Example:

```
After 25: last three [20, 22, 25], average 22.33
After 30: last three [22, 25, 30], average 25.67
After 28: last three [25, 30, 28], average 27.67
After 24: last three [30, 28, 24], average 27.33
```

## 5. Layered settings

**ChainMap.** Build a `ChainMap` from three dictionaries: command-line options `{}` (empty), environment settings `{"debug": "yes"}` and defaults `{"debug": "no", "port": 8000, "host": "localhost"}`. Print the values of `debug`, `port` and `host`, then set `port` to `9000` through the ChainMap and show which dictionary changed.

Example:

```
debug: yes
port: 8000
host: localhost
command line now: {'port': 9000}
defaults still: {'debug': 'no', 'port': 8000, 'host': 'localhost'}
```

## 6. Recently used

**OrderedDict.** Keep the three most recently used items in an `OrderedDict`. Process the accesses `["a", "b", "c", "a", "d", "b"]` one by one: an item already present is moved to the end with `move_to_end`; a new item is added, and if there are now more than three, the oldest is removed with `popitem(last=False)`. Print the keys after every access.

Example:

```
a -> ['a']
b -> ['a', 'b']
c -> ['a', 'b', 'c']
a -> ['b', 'c', 'a']
d -> ['c', 'a', 'd']
b -> ['a', 'd', 'b']
```

## 7. Validated list

**UserList.** Write a class `IntList(UserList)` whose `append` only accepts integers and prints `rejected: <item>` for anything else. Add `5`, `"six"`, `7` and `2.5`, then print the list and its sum.

Example:

```
rejected: 'six'
rejected: 2.5
[5, 7]
Sum: 12
```

## 8. Students per city

**Counter on a file.** Read `datasets/students.csv` (skip the header, split on commas, the city is the fourth column) and count how many students come from each city with a `Counter`. Print the two most common cities and then every city with its count in alphabetical order.

Example:

```
Most common: [('Kathmandu', 3), ('Pokhara', 2)]
Bhaktapur: 1
Biratnagar: 1
Butwal: 1
Dharan: 1
Kathmandu: 3
Lalitpur: 1
Pokhara: 2
```
