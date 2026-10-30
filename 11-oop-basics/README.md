# OOP Basics

Object-oriented programming (OOP) is a way of organising a program around objects: things that keep their own data together with the actions that belong to that data. A beginner needs it because almost every real Python program, library and framework is built from classes and objects.

## What you will learn

- What an object and a class are, and how they relate
- How to define a class, create objects and give them starting values with `__init__`
- What `self` means and why it is the first parameter of every method
- The difference between instance attributes and class attributes
- How to write methods that read and change an object's data
- What `__str__` and `__repr__` change about `print(obj)`
- How to keep objects in lists and build objects from a CSV file
- When to use an instance method, a class method or a static method

## 1. What is OOP?

Think of a real thing, for example a car. It has data (its colour, its speed) and it can do actions (start, stop). In Python, such a thing is called an object. The data of an object is stored in its attributes. The actions are its methods: functions that belong to the object. A class is the blueprint that describes which attributes and methods every object of that kind has. In one sentence: a class is the blueprint of a house, and each house built from it is an object.

You already use objects all the time. Every string, list and number in Python is an object created from a built-in class.

```python
message = "hello"
numbers = [3, 1, 2]

print(type(message))
print(message.upper())      # a method of the string object
print(type(numbers))
numbers.append(4)           # a method of the list object
print(numbers)
```

Output:

```
<class 'str'>
HELLO
<class 'list'>
[3, 1, 2, 4]
```

`type()` tells you which class an object was made from. `upper()` and `append()` are methods: you call them with a dot after the object.

## 2. Defining a class and creating objects

A class is defined with the `class` keyword. Class names are written in CapWords, for example `Dog` or `BankAccount`. The body of a class cannot be empty, so for a class with nothing in it yet you write `pass`, a statement that does nothing. To create an object, call the class like a function. Each call creates a brand new object. Creating an object is also called instantiation, and the object is an instance of the class.

```python
class Dog:
    pass


first_dog = Dog()
second_dog = Dog()

print(type(first_dog))
print(first_dog is second_dog)
```

Output:

```
<class '__main__.Dog'>
False
```

`__main__` is simply the name of the script that is running. `first_dog is second_dog` is `False` because the two calls created two separate objects, even though they were built from the same blueprint.

## 3. `__init__` sets the starting values

An empty class is not very useful. Most objects need some starting data: a dog has a name and an age. The special method `__init__` (short for initialise) sets these starting values. Its name has two underscores on each side, so it is called a dunder method (double underscore). Python calls `__init__` automatically every time you create an object. You never call it yourself. The values you write in the parentheses when creating the object are passed to the parameters of `__init__` after `self`.

```python
class Dog:
    def __init__(self, name, age):
        print("__init__ is running for", name)
        self.name = name
        self.age = age


buddy = Dog("Buddy", 3)
print(buddy.name)
print(buddy.age)
```

Output:

```
__init__ is running for Buddy
Buddy
3
```

The line `self.name = name` means: store the value of the parameter `name` inside this object under the attribute `name`. The `print()` inside `__init__` proves that it ran at the moment `Dog("Buddy", 3)` was executed.

## 4. `self` is the object itself

Inside a class, methods need a way to say "the object I am working on right now". That is `self`. `self` must always be the first parameter of a method. When you write `buddy.bark()`, Python turns it into `Dog.bark(buddy)`, so inside `bark` the name `self` refers to `buddy`. You do not pass `self` yourself; Python does it for you. The word `self` is a convention. Any name would work, but every Python programmer uses `self`, so you should too.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")


buddy = Dog("Buddy")
rex = Dog("Rex")

buddy.bark()        # self is buddy
rex.bark()          # self is rex
Dog.bark(buddy)     # the long form: exactly what Python does behind the scenes
```

Output:

```
Buddy says Woof!
Rex says Woof!
Buddy says Woof!
```

## 5. Instance attributes and class attributes

An attribute created with `self.` inside `__init__` belongs to one object. It is an instance attribute, and every object has its own copy. An attribute written directly in the class body, outside any method, is a class attribute. It is shared by all objects of the class.

Changing a class attribute through the class (`Dog.species = ...`) changes it for every object. Assigning through one object (`buddy.species = ...`) does something different: it creates a new instance attribute on that one object, which hides the class attribute for that object only.

```python
class Dog:
    species = "Canis familiaris"     # class attribute, shared by every dog

    def __init__(self, name):
        self.name = name             # instance attribute, one per dog


buddy = Dog("Buddy")
rex = Dog("Rex")

print(buddy.species, "|", rex.species)

Dog.species = "Domestic dog"         # change through the class: affects all dogs
print(buddy.species, "|", rex.species)

buddy.species = "Special dog"        # assign through one object: only that object changes
print(buddy.species, "|", rex.species)
print(Dog.species)
```

Output:

```
Canis familiaris | Canis familiaris
Domestic dog | Domestic dog
Special dog | Domestic dog
Domestic dog
```

| | Instance attribute | Class attribute |
|---|---|---|
| Where it is created | `self.name = ...` inside a method | `name = ...` in the class body |
| How many copies | One per object | One for the whole class |
| Typical use | Data that differs per object (name, balance) | Settings or counters shared by all objects |
| How to change for everyone | Not possible | `ClassName.attribute = ...` |

## 6. Many objects from one class

One class can create as many objects as you need. Each object is independent: changing the data of one object does not change the others.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


aarav = Student("Aarav", 85)
sita = Student("Sita", 92)
bikash = Student("Bikash", 67)

sita.marks = 95                      # only sita changes

for student in (aarav, sita, bikash):
    print(student.name, student.marks)
```

Output:

```
Aarav 85
Sita 95
Bikash 67
```

## 7. Default values in `__init__`

`__init__` is a normal function, so its parameters can have default values. A parameter with a default can be left out when the object is created.

```python
class Student:
    def __init__(self, name, age=18, city="Kathmandu"):
        self.name = name
        self.age = age
        self.city = city


first = Student("Aarav")
second = Student("Sita", 21)
third = Student("Priya", 22, "Butwal")

print(first.name, first.age, first.city)
print(second.name, second.age, second.city)
print(third.name, third.age, third.city)
```

Output:

```
Aarav 18 Kathmandu
Sita 21 Kathmandu
Priya 22 Butwal
```

## 8. Methods

A method is a function defined inside a class. After `self`, a method can take any parameters you like. A method can read the attributes of its object (`self.age`) and it can change them (`self.age += 1`). The change stays in the object after the method ends.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, other_name):
        print("Hello", other_name + ", I am", self.name)

    def birthday(self):
        self.age += 1
        print("Happy birthday", self.name + "! You are now", self.age)

    def is_adult(self):
        return self.age >= 18


sita = Person("Sita", 17)
sita.greet("Aarav")
print("Adult?", sita.is_adult())
sita.birthday()
print("Adult?", sita.is_adult())
print("Age stored in the object:", sita.age)
```

Output:

```
Hello Aarav, I am Sita
Adult? False
Happy birthday Sita! You are now 18
Adult? True
Age stored in the object: 18
```

`greet` takes a parameter, `birthday` changes an attribute, and `is_adult` reads an attribute and returns a result.

## 9. `__str__` and `__repr__`

What happens when you print an object? Without any preparation, Python shows the class name and the address of the object in memory, which is not helpful.

```python
class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year


book = Book("Sapiens", 2011)
print(book)
```

Output:

```
<__main__.Book object at 0x000001E9C2A3B7D0>
```

The address after `at` will be different on your computer. To control the text, define the dunder method `__str__`. It must return a string, and `print()` uses that string. A second dunder method, `__repr__`, returns a text meant for programmers. It is used in the interactive shell and when an object sits inside a list or dictionary. A good `__repr__` looks like the code that would recreate the object.

```python
class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"Book('{self.title}', {self.year})"


book = Book("Sapiens", 2011)
print(book)                                 # uses __str__
print(str(book))                            # uses __str__
print(repr(book))                           # uses __repr__
print([book, Book("Clean Code", 2008)])     # a list shows the __repr__ of each item
```

Output:

```
Sapiens (2011)
Sapiens (2011)
Book('Sapiens', 2011)
[Book('Sapiens', 2011), Book('Clean Code', 2008)]
```

| | `__str__` | `__repr__` |
|---|---|---|
| Audience | People | Programmers |
| Used by | `print(obj)`, `str(obj)`, f-strings | `repr(obj)`, the shell, items inside lists and dicts |
| Should look like | A friendly description | Code that recreates the object |
| If missing | Python falls back to `__repr__` | Python shows `<ClassName object at address>` |

## 10. Adding, changing and deleting attributes and objects

Python objects are flexible. You can add a new attribute to an existing object at any time, change an attribute, delete an attribute with `del`, and delete the object itself. `hasattr(obj, "name")` tells you whether an object has an attribute, and `vars(obj)` shows all of its instance attributes as a dictionary.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Rohan", 20)

student.city = "Biratnagar"          # add a new attribute to this object only
student.age = 21                     # change an existing attribute
print(student.name, student.age, student.city)

del student.age                      # delete one attribute
print(hasattr(student, "age"))
print(vars(student))                 # the attributes the object still has

del student                          # delete the object itself
try:
    print(student.name)
except NameError as error:
    print("Error:", error)
```

Output:

```
Rohan 21 Biratnagar
False
{'name': 'Rohan', 'city': 'Biratnagar'}
Error: name 'student' is not defined
```

After `del student` the name no longer exists, so using it raises `NameError`.

## 11. Objects inside lists

Objects can be stored in lists like any other value. A list of objects is the normal way to handle many records of the same kind. You can loop over the list, compare attributes and pick the best one. `max()` and `min()` accept a `key` function that says which attribute to compare.

### Finding the latest book

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


books = [
    Book("The Hobbit", "J. R. R. Tolkien", 1937),
    Book("Sapiens", "Yuval Noah Harari", 2011),
    Book("1984", "George Orwell", 1949),
]

latest = books[0]
for book in books:
    if book.year > latest.year:
        latest = book
print("Latest book:", latest)

# The same result in one line with max() and a key function
print("Latest book:", max(books, key=lambda book: book.year))
```

Output:

```
Latest book: Sapiens by Yuval Noah Harari (2011)
Latest book: Sapiens by Yuval Noah Harari (2011)
```

### Finding the highest marks

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


students = [Student("Aarav", 85), Student("Sita", 92), Student("Bikash", 67)]

topper = max(students, key=lambda student: student.marks)
print("Highest marks:", topper.name, topper.marks)

print("Ranked:")
for student in sorted(students, key=lambda student: student.marks, reverse=True):
    print(" ", student.name, student.marks)
```

Output:

```
Highest marks: Sita 92
Ranked:
  Sita 92
  Aarav 85
  Bikash 67
```

### Building objects from a CSV file

Data usually comes from a file, not from code. The script below reads `datasets/books.csv` with `csv.DictReader`, which gives one dictionary per row, and turns every row into a `Book` object. Save it inside the `examples` folder: the path to the dataset is worked out from the location of the script file, so it runs from any folder.

```python
import csv
from pathlib import Path


class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.price:.2f}"


DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

books = []
with open(DATA_DIR / "books.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        books.append(Book(row["title"], row["author"], int(row["year"]), float(row["price"])))

print("Books loaded:", len(books))
print("Latest:", max(books, key=lambda book: book.year))
print("Cheapest:", min(books, key=lambda book: book.price))
```

Output:

```
Books loaded: 10
Latest: Automate the Boring Stuff with Python (2015) - 29.99
Cheapest: Pride and Prejudice (1813) - 9.99
```

Everything read from a CSV file is text, so `year` and `price` are converted with `int()` and `float()` before the object is created.

## 12. Instance methods, class methods and static methods

So far every method received `self`. Python has two more kinds of method. A class method is marked with `@classmethod` and receives the class itself as its first parameter, called `cls`. It is used to build objects in a different way (an alternative constructor) or to work with data that belongs to the whole class, such as a counter. A static method is marked with `@staticmethod` and receives neither `self` nor `cls`. It is an ordinary helper function that lives inside the class because it logically belongs there.

```python
class Student:
    count = 0                                  # how many students exist

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.count += 1

    def show(self):                            # instance method: needs the object
        print(self.name, self.marks, "->", Student.grade_for(self.marks))

    @classmethod
    def from_string(cls, text):               # class method: builds a new object
        name, marks = text.split(",")
        return cls(name, int(marks))

    @classmethod
    def total(cls):                            # class method: reads class data
        return cls.count

    @staticmethod
    def grade_for(marks):                      # static method: a helper, no self, no cls
        if marks >= 80:
            return "A"
        if marks >= 60:
            return "B"
        return "C"


first = Student("Aarav", 85)
second = Student.from_string("Sita,92")
first.show()
second.show()
print("Grade for 55:", Student.grade_for(55))
print("Total students:", Student.total())
```

Output:

```
Aarav 85 -> A
Sita 92 -> A
Grade for 55: C
Total students: 2
```

| Kind | Decorator | First parameter | Can use | Use it when |
|---|---|---|---|---|
| Instance method | none | `self` (the object) | the object's attributes and the class | the action needs the data of one object |
| Class method | `@classmethod` | `cls` (the class) | class attributes, can create objects | you need another way to build objects, or class-wide data |
| Static method | `@staticmethod` | none | only its own parameters | a helper that belongs to the topic but needs no object |

## 13. Worked examples

### BankAccount

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot withdraw {amount}. Balance is only {self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def show(self):
        print(f"{self.owner}: balance {self.balance}")


account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
account.show()
```

Output:

```
Deposited 500. Balance: 1500
Cannot withdraw 2000. Balance is only 1500
Withdrew 300. Balance: 1200
Asha: balance 1200
```

### Playlist

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []                  # every playlist starts with its own empty list

    def add_song(self, song):
        self.songs.append(song)
        print("Added:", song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print("Removed:", song)
        else:
            print("Not in playlist:", song)

    def show_songs(self):
        print(f"Playlist '{self.name}' ({len(self.songs)} songs)")
        for number, song in enumerate(self.songs, start=1):
            print(f"  {number}. {song}")


morning = Playlist("Morning Mix")
morning.add_song("Sunrise Walk")
morning.add_song("Coffee Time")
morning.add_song("Fresh Start")
morning.remove_song("Coffee Time")
morning.remove_song("Unknown Song")
morning.show_songs()
```

Output:

```
Added: Sunrise Walk
Added: Coffee Time
Added: Fresh Start
Removed: Coffee Time
Not in playlist: Unknown Song
Playlist 'Morning Mix' (2 songs)
  1. Sunrise Walk
  2. Fresh Start
```

### Student with a grade method

```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A+"
        if self.marks >= 80:
            return "A"
        if self.marks >= 70:
            return "B"
        if self.marks >= 60:
            return "C"
        return "F"

    def __str__(self):
        return f"{self.name} (age {self.age}): {self.marks} marks, grade {self.grade()}"


students = [Student("Aarav", 20, 85), Student("Sita", 21, 92), Student("Maya", 19, 38)]
for student in students:
    print(student)
```

Output:

```
Aarav (age 20): 85 marks, grade A
Sita (age 21): 92 marks, grade A+
Maya (age 19): 38 marks, grade F
```

### Car

```python
class Car:
    def __init__(self, brand, model, fuel=50):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.running = False

    def start(self):
        if self.fuel == 0:
            print("Cannot start: the tank is empty")
            return
        self.running = True
        print(f"{self.brand} {self.model} started")

    def drive(self, km):
        if not self.running:
            print("Start the car first")
            return
        needed = km // 10                      # the car uses 1 litre per 10 km
        if needed > self.fuel:
            print(f"Not enough fuel for {km} km")
            return
        self.fuel -= needed
        print(f"Drove {km} km. Fuel left: {self.fuel} litres")

    def stop(self):
        self.running = False
        print(f"{self.brand} {self.model} stopped")


car = Car("Toyota", "Corolla", fuel=5)
car.drive(20)
car.start()
car.drive(20)
car.drive(100)
car.stop()
```

Output:

```
Start the car first
Toyota Corolla started
Drove 20 km. Fuel left: 3 litres
Not enough fuel for 100 km
Toyota Corolla stopped
```

### Calculator

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return self.record(f"{a} + {b}", a + b)

    def subtract(self, a, b):
        return self.record(f"{a} - {b}", a - b)

    def multiply(self, a, b):
        return self.record(f"{a} * {b}", a * b)

    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return self.record(f"{a} / {b}", a / b)

    def record(self, text, result):
        self.history.append(f"{text} = {result}")
        return result

    def show_history(self):
        print("History:")
        for line in self.history:
            print(" ", line)


calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(4, 2.5))
print(calc.divide(9, 0))
print(calc.divide(9, 3))
calc.show_history()
```

Output:

```
15
5
10.0
Cannot divide by zero
None
3.0
History:
  10 + 5 = 15
  10 - 5 = 5
  4 * 2.5 = 10.0
  9 / 3 = 3.0
```

`divide(9, 0)` prints a message and returns `None`, so the `print()` around it shows `None`. The failed division is not added to the history.

## Common mistakes

- Forgetting `self` as the first parameter: `def bark():` gives `TypeError: Dog.bark() takes 0 positional arguments but 1 was given` -> write `def bark(self):`.
- Writing `name = name` inside `__init__` -> the value disappears when `__init__` ends; write `self.name = name` to store it in the object.
- Forgetting the parentheses: `dog = Dog` stores the class, not an object -> write `dog = Dog()`.
- Changing a class attribute through an object (`buddy.species = ...`) and expecting every object to change -> change it through the class: `Dog.species = ...`.
- Using a list as a default value: `def __init__(self, songs=[])` makes every object share one list -> use `songs=None` and create `self.songs = []` inside `__init__`.
- Calling a method without parentheses: `account.show` does nothing visible -> write `account.show()`.

## Summary

- A class is a blueprint; an object is one thing built from it, with its own attributes (data) and methods (behaviour).
- `__init__` runs automatically when an object is created and sets its starting values.
- `self` is the object a method was called on; it must be the first parameter of every instance method.
- Instance attributes (`self.x`) belong to one object; class attributes (written in the class body) are shared by all objects.
- Methods can take parameters and can read and change the attributes of their object.
- `__str__` controls what `print(obj)` shows; `__repr__` is the programmer-facing text used inside lists.
- Attributes can be added, changed and deleted on an object at any time; `del obj` removes the object's name.
- `@classmethod` receives the class (`cls`) and `@staticmethod` receives nothing; a plain method receives the object (`self`).

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Exception Handling](../10-exception-handling/README.md) | [Next: OOP Advanced](../12-oop-advanced/README.md) | [Home](../README.md)
