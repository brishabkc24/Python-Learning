# OOP Advanced

This topic builds on OOP Basics and covers the four pillars of object-oriented programming: inheritance, polymorphism, encapsulation and abstraction, plus composition. A beginner needs them to reuse code without copying it, to protect an object's data, and to read the class hierarchies found in every real library.

## What you will learn

- How a child class inherits from a parent class and when to call `super().__init__()`
- The five types of inheritance and how Python decides which method to run (MRO)
- Polymorphism: the same method name doing different things, duck typing and operator overloading
- Why Python has no true method overloading and what to use instead
- Encapsulation with public, protected and private attributes, getters, setters and `@property`
- Abstraction with `abc.ABC` and `@abstractmethod`
- Composition (has-a) compared with inheritance (is-a)
- `isinstance()`, `issubclass()`, `__del__` and the most useful dunder methods

## 1. Inheritance

Inheritance lets a new class take over the attributes and methods of an existing class. The existing class is the parent (also called base class or superclass). The new class is the child (also called derived class or subclass). You write the parent's name in parentheses after the child's name. A child "is a" kind of parent: a Dog is an Animal. Inheritance removes duplication, because code shared by many classes is written once in the parent.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")


class Dog(Animal):                  # Dog is-a Animal
    def bark(self):
        print(self.name, "says Woof!")


buddy = Dog("Buddy")
buddy.eat()          # inherited from Animal
buddy.sleep()        # inherited from Animal
buddy.bark()         # defined in Dog
print(isinstance(buddy, Dog), isinstance(buddy, Animal))
```

Output:

```
Buddy is eating
Buddy is sleeping
Buddy says Woof!
True True
```

`Dog` did not define `__init__`, `eat` or `sleep`, yet a `Dog` object has all of them. They come from `Animal`.

## 2. `super().__init__()` when the child adds attributes

Often the child needs extra attributes. Then the child defines its own `__init__`, and that replaces the parent's `__init__` completely. To keep the parent's work, the child calls `super().__init__(...)` first. `super()` means "the parent class", so `super().__init__(name, age)` runs the parent's `__init__` on the current object. After that, the child adds its own attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)      # let Person set name and age
        self.student_id = student_id     # then add the new attribute

    def show_id(self):
        print(f"{self.name} has student id {self.student_id}")


sita = Student("Sita", 21, "S-102")
sita.introduce()
sita.show_id()
```

Output:

```
I am Sita, 21 years old
Sita has student id S-102
```

If `Student.__init__` forgot the `super().__init__(name, age)` line, `sita.name` would not exist and `introduce()` would raise `AttributeError`.

## 3. The five types of inheritance

| Type | Shape | Example |
|---|---|---|
| Single | one parent, one child | `Animal -> Dog` |
| Multilevel | a chain: grandparent -> parent -> child | `Grandparent -> Parent -> Child` |
| Multiple | one child with two or more parents | `Child(Mother, Father)` |
| Hierarchical | one parent with several children | `Animal -> Dog`, `Animal -> Cat` |
| Hybrid | a mix of the types above | `Car(Vehicle)`, `Boat(Vehicle)`, `AmphibiousCar(Car, Boat)` |

### Single inheritance

```python
class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):
    pass


Child().greet()
```

Output:

```
Hello from Parent
```

### Multilevel inheritance

Each level inherits everything from the levels above it.

```python
class Grandparent:
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def phone(self):
        print("Child's phone")


child = Child()
child.house()
child.car()
child.phone()
```

Output:

```
Grandparent's house
Parent's car
Child's phone
```

### Multiple inheritance

The child lists several parents and gets the methods of all of them.

```python
class Mother:
    def cooking(self):
        print("Mother teaches cooking")


class Father:
    def driving(self):
        print("Father teaches driving")


class Child(Mother, Father):
    pass


child = Child()
child.cooking()
child.driving()
```

Output:

```
Mother teaches cooking
Father teaches driving
```

### Hierarchical inheritance

Several children share one parent.

```python
class Animal:
    def breathe(self):
        print("Breathing")


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


for animal in (Dog(), Cat()):
    animal.breathe()
    animal.sound()
```

Output:

```
Breathing
Woof
Breathing
Meow
```

### Hybrid inheritance

A combination. Here `Vehicle` has two children (hierarchical) and `AmphibiousCar` inherits from both of them (multiple).

```python
class Vehicle:
    def start(self):
        print("Engine started")


class Car(Vehicle):
    def drive(self):
        print("Driving on the road")


class Boat(Vehicle):
    def sail(self):
        print("Sailing on water")


class AmphibiousCar(Car, Boat):      # hybrid: hierarchical + multiple
    pass


amphibious = AmphibiousCar()
amphibious.start()
amphibious.drive()
amphibious.sail()
```

Output:

```
Engine started
Driving on the road
Sailing on water
```

## 4. Method overriding and `super()`

When a child defines a method with the same name as a parent method, the child's version wins for child objects. This is called overriding. Sometimes you want the parent's behaviour plus something extra. Then call the parent's version with `super().method_name()` inside the child's method.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")


class Dog(Animal):
    def speak(self):                    # overrides Animal.speak
        print(self.name, "says Woof!")


class Puppy(Dog):
    def speak(self):
        super().speak()                 # run Dog's version first
        print(self.name, "wags its tail")


Animal("Generic").speak()
Dog("Buddy").speak()
Puppy("Tiny").speak()
```

Output:

```
Generic makes a sound
Buddy says Woof!
Tiny says Woof!
Tiny wags its tail
```

## 5. Method Resolution Order (MRO)

When a class has several parents, Python needs a rule for which method to run first. The rule is the Method Resolution Order (MRO): Python searches the class itself, then its parents from left to right, then their parents, and finally `object`, the built-in root of every class. Each class is visited only once. `ClassName.__mro__` shows the order.

```python
class A:
    def who(self):
        print("A")


class B(A):
    def who(self):
        print("B")


class C(A):
    def who(self):
        print("C")


class D(B, C):
    pass


D().who()                     # B comes before C, so B.who runs
print(" -> ".join(cls.__name__ for cls in D.__mro__))
```

Output:

```
B
D -> B -> C -> A -> object
```

## 6. Polymorphism

Polymorphism means "many forms". In OOP it means that the same method name can behave differently depending on the object. You can call `shape.area()` on any shape without knowing which kind of shape it is.

### Same method name, different behaviour

```python
import math


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


shapes = [Circle(2), Rectangle(3, 4), Square(5)]
for shape in shapes:
    print(f"{type(shape).__name__:<10} area = {shape.area():.2f}")
```

Output:

```
Circle     area = 12.57
Rectangle  area = 12.00
Square     area = 25.00
```

The loop does not care which class each object has. It calls `area()` and each object answers in its own way.

### Duck typing

Python does not even require a shared parent. If an object has the method you call, it works. This is called duck typing: "if it walks like a duck and quacks like a duck, it is a duck".

```python
class Duck:
    def speak(self):
        return "Quack"


class Robot:
    def speak(self):
        return "Beep"


class Stone:
    pass


def make_it_speak(thing):
    print(thing.speak())


make_it_speak(Duck())
make_it_speak(Robot())
try:
    make_it_speak(Stone())
except AttributeError as error:
    print("Error:", error)
```

Output:

```
Quack
Beep
Error: 'Stone' object has no attribute 'speak'
```

### Built-in polymorphism

The built-in functions and operators are polymorphic too. `len()` works on strings, lists and dictionaries, and `+` adds numbers, joins strings and concatenates lists.

```python
print(len("hello"), len([1, 2, 3]), len({"a": 1}))
print(2 + 3)
print("Hello, " + "world")
print([1, 2] + [3])
```

Output:

```
5 3 1
5
Hello, world
[1, 2, 3]
```

### Operator overloading

You can teach the operators to work on your own classes by defining dunder methods. `a + b` calls `a.__add__(b)`, `a == b` calls `a.__eq__(b)` and `a < b` calls `a.__lt__(b)`. This is called operator overloading.

```python
class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __add__(self, other):
        return Money(self.rupees + other.rupees)

    def __eq__(self, other):
        return self.rupees == other.rupees

    def __lt__(self, other):
        return self.rupees < other.rupees

    def __str__(self):
        return f"Rs {self.rupees}"


price = Money(500)
tax = Money(65)
total = price + tax                 # calls price.__add__(tax)

print(total)
print(total == Money(565))          # calls total.__eq__(Money(565))
print(tax < price)                  # calls tax.__lt__(price)
print(max(price, tax, total))       # max() compares with __lt__ as well
```

Output:

```
Rs 565
True
True
Rs 565
```

| Operator | Dunder method | Operator | Dunder method |
|---|---|---|---|
| `a + b` | `__add__` | `a == b` | `__eq__` |
| `a - b` | `__sub__` | `a != b` | `__ne__` |
| `a * b` | `__mul__` | `a < b` | `__lt__` |
| `a / b` | `__truediv__` | `a > b` | `__gt__` |
| `a // b` | `__floordiv__` | `a <= b` | `__le__` |
| `a % b` | `__mod__` | `a >= b` | `__ge__` |

### "Method overloading" in Python

In some languages you can define the same method twice with different parameter lists, and the language picks one by the arguments. Python does not have this. If you define a method twice, the last definition replaces the first one.

```python
class Greeter:
    def hello(self):
        print("Hello!")

    def hello(self, name):            # this definition replaces the first one
        print("Hello,", name)


greeter = Greeter()
greeter.hello("Sita")
try:
    greeter.hello()
except TypeError as error:
    print("Error:", error)
```

Output:

```
Hello, Sita
Error: Greeter.hello() missing 1 required positional argument: 'name'
```

The Python way is one method that accepts different inputs, using default arguments or `*args` (which collects any number of positional arguments into a tuple).

```python
class Calculator:
    def add(self, *numbers):                          # any number of arguments
        return sum(numbers)

    def greet(self, name="friend", excited=False):    # default arguments
        text = f"Hello, {name}"
        if excited:
            text += "!"
        return text


calc = Calculator()
print(calc.add(2, 3))
print(calc.add(1, 2, 3, 4))
print(calc.greet())
print(calc.greet("Sita", excited=True))
```

Output:

```
5
10
Hello, friend
Hello, Sita!
```

## 7. Encapsulation

Encapsulation means keeping an object's data together with the methods that work on it, and controlling who may touch the data directly. Python uses naming conventions for this.

| Kind | Written as | Inside the class | In a child class | Outside the class |
|---|---|---|---|---|
| Public | `self.name` | yes | yes | yes |
| Protected | `self._name` | yes | yes | possible, but by convention you should not |
| Private | `self.__name` | yes | no (the name is mangled) | no (the name is mangled) |

A single leading underscore is only a signal to other programmers: "internal, please do not touch". Two leading underscores trigger name mangling: Python renames `__balance` to `_Account__balance`, so the short name does not work from outside.

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner              # public
        self._bank = "Example Bank"     # protected (by convention)
        self.__balance = balance        # private (name mangled)

    def show_balance(self):
        print("Balance inside the class:", self.__balance)


account = Account("Asha", 1000)
print(account.owner)
print(account._bank)                    # possible, but the underscore says: please do not
account.show_balance()

try:
    print(account.__balance)
except AttributeError as error:
    print("Error:", error)

print(account._Account__balance)        # name mangling: how Python really stores it
```

Output:

```
Asha
Example Bank
Balance inside the class: 1000
Error: 'Account' object has no attribute '__balance'
1000
```

### Getter and setter methods

To let outside code read or change a private attribute safely, the class offers methods: a getter that returns the value and a setter that checks the new value before storing it.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
        else:
            print("Invalid age:", new_age)


sita = Student("Sita", 21)
print(sita.get_age())
sita.set_age(22)
print(sita.get_age())
sita.set_age(200)
print(sita.get_age())
```

Output:

```
21
22
Invalid age: 200
22
```

### `@property` and the setter

Getter and setter methods work, but `sita.get_age()` reads less naturally than `sita.age`. The `@property` decorator lets a method be used like an attribute. A second method marked `@age.setter` runs whenever someone assigns `sita.age = ...`, so the validation still happens. Raising `ValueError` is the usual way to reject a bad value.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age                   # this line already uses the setter below

    @property
    def age(self):                       # runs when you read student.age
        return self.__age

    @age.setter
    def age(self, value):                # runs when you assign student.age = ...
        if not 0 <= value <= 120:
            raise ValueError(f"age must be between 0 and 120, got {value}")
        self.__age = value


sita = Student("Sita", 21)
print(sita.age)
sita.age = 22
print(sita.age)
try:
    sita.age = 200
except ValueError as error:
    print("Error:", error)
print(sita.age)
```

Output:

```
21
22
Error: age must be between 0 and 120, got 200
22
```

## 8. Abstraction

Abstraction means showing only what an object can do and hiding how it does it. An abstract class is a parent that lists the methods every child must have, without writing them itself. You create one by inheriting from `ABC` (abstract base class) in the `abc` module and marking the required methods with `@abstractmethod`. An abstract class cannot be instantiated. A child must implement every abstract method before it can be instantiated.

```python
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):                  # a normal method, shared by all shapes
        print(f"{type(self).__name__}: area {self.area():.2f}, perimeter {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


Circle(1).describe()
Rectangle(3, 4).describe()

try:
    shape = Shape()
except TypeError as error:
    print("Error:", error)
```

Output:

```
Circle: area 3.14, perimeter 6.28
Rectangle: area 12.00, perimeter 14.00
Error: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'
```

Python versions before 3.12 word the error slightly differently, but it is always a `TypeError`. A second common use is a family of services that all do the same job in different ways.

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient):
        self.recipient = recipient

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email to {self.recipient}: {message}")


class SmsNotification(Notification):
    def send(self, message):
        print(f"SMS to {self.recipient}: {message}")


notifications = [
    EmailNotification("asha@example.com"),
    SmsNotification("9800000001"),
]
for notification in notifications:
    notification.send("Your order has shipped")
```

Output:

```
Email to asha@example.com: Your order has shipped
SMS to 9800000001: Your order has shipped
```

## 9. Composition: has-a relationships

Not every relationship is "is-a". A car is not an engine; a car has an engine. Composition (also called containership) means one object stores another object as an attribute and uses it. The outer object delegates work to the inner one.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True
        print(f"Engine ({self.horsepower} hp) started")


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)     # a Car has-a Engine

    def start(self):
        print(f"{self.brand}: turning the key")
        self.engine.start()                  # delegate the work to the engine


car = Car("Toyota", 120)
car.start()
print("Engine running?", car.engine.running)
```

Output:

```
Toyota: turning the key
Engine (120 hp) started
Engine running? True
```

A container object can also hold many objects in a list. A library contains books.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []                      # a Library contains many Books

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def show(self):
        print(f"{self.name} has {len(self.books)} books:")
        for book in self.books:
            print(" -", book)


library = Library("City Library")
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Animal Farm", "George Orwell"))
library.add_book(Book("The Hobbit", "J. R. R. Tolkien"))
library.show()
for book in library.find_by_author("George Orwell"):
    print("By Orwell:", book)
```

Output:

```
City Library has 3 books:
 - 1984 by George Orwell
 - Animal Farm by George Orwell
 - The Hobbit by J. R. R. Tolkien
By Orwell: 1984 by George Orwell
By Orwell: Animal Farm by George Orwell
```

| | Inheritance | Composition |
|---|---|---|
| Relationship | is-a (a Dog is an Animal) | has-a (a Car has an Engine) |
| How it is written | `class Dog(Animal)` | `self.engine = Engine()` |
| Use it when | the child is a special kind of the parent | one object is built from other objects |

## 10. `isinstance()` and `issubclass()`

`isinstance(obj, Class)` asks whether an object was made from a class or from any of its children. `issubclass(Child, Parent)` asks the same question about two classes. Both accept a tuple of classes, meaning "any of these".

```python
class Animal:
    pass


class Dog(Animal):
    pass


buddy = Dog()
print(isinstance(buddy, Dog))
print(isinstance(buddy, Animal))
print(isinstance(buddy, str))
print(isinstance(5, (int, float)))        # a tuple means "any of these"
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print(issubclass(bool, int))
```

Output:

```
True
True
False
True
True
False
True
```

## 11. The `__del__` destructor

`__del__` is called when an object is about to be destroyed, which happens after the last name that refers to it is gone. It is the opposite of `__init__` and is sometimes called the destructor.

```python
class TempFile:
    def __init__(self, name):
        self.name = name
        print("Opened", self.name)

    def __del__(self):
        print("Cleaned up", self.name)


note = TempFile("note.txt")
del note                     # the last reference is gone, so __del__ runs now
print("End of program")
```

Output:

```
Opened note.txt
Cleaned up note.txt
End of program
```

Caution: the exact moment `__del__` runs is not guaranteed, especially when an object is referenced from several places or when the program is shutting down. Do not rely on it for important clean-up such as closing files. Use `with` blocks for that (see File Handling).

## 12. Useful dunder methods

Dunder methods let your objects work with Python's built-in syntax and functions.

| Dunder method | Called by | Purpose |
|---|---|---|
| `__init__` | `ClassName(...)` | set the starting values |
| `__str__` | `print(obj)`, `str(obj)` | readable text for people |
| `__repr__` | `repr(obj)`, the shell, lists | programmer text, ideally valid code |
| `__len__` | `len(obj)` | the size of a container object |
| `__eq__` | `obj == other` | decide when two objects count as equal |
| `__add__` | `obj + other` | define addition |
| `__getitem__` | `obj[index]` | indexing and slicing |
| `__iter__` | `for item in obj` | make the object loopable |

```python
class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = list(members)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        return self.members[index]

    def __iter__(self):
        return iter(self.members)

    def __eq__(self, other):
        return self.members == other.members

    def __repr__(self):
        return f"Team('{self.name}', {self.members})"


team = Team("Blue", ["Asha", "Bibek", "Deepa"])
print(team)
print(len(team))
print(team[0])
for member in team:
    print(" -", member)
print(team == Team("Red", ["Asha", "Bibek", "Deepa"]))
```

Output:

```
Team('Blue', ['Asha', 'Bibek', 'Deepa'])
3
Asha
 - Asha
 - Bibek
 - Deepa
True
```

## 13. Worked examples

### Employee salaries with an overridden method

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def show(self):
        print(f"{type(self).__name__:<18} {self.name:<6} salary: {self.calculate_salary():>9.2f}")


class PermanentEmployee(Employee):
    def __init__(self, name, base_salary, bonus, allowance):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.allowance


class TemporaryEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_rate * self.hours


staff = [
    PermanentEmployee("Asha", 50000, 5000, 3000),
    TemporaryEmployee("Bibek", 400, 120),
    Employee("Deepa", 30000),
]
for person in staff:
    person.show()
print("Total payroll:", sum(person.calculate_salary() for person in staff))
```

Output:

```
PermanentEmployee  Asha   salary:  58000.00
TemporaryEmployee  Bibek  salary:  48000.00
Employee           Deepa  salary:  30000.00
Total payroll: 136000
```

`show()` is written once in `Employee`, but it calls `self.calculate_salary()`, so each object uses its own version. That is polymorphism and overriding working together.

### Vehicle, Car and Bike

```python
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def display(self):
        print(f"{self.brand} with {self.wheels} wheels")


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand, 4)
        self.seats = seats

    def display(self):
        super().display()
        print(f"  Car with {self.seats} seats")


class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand, 2)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print(f"  Bike with a {self.engine_cc} cc engine")


for vehicle in (Car("Toyota", 5), Bike("Honda", 150)):
    vehicle.display()
```

Output:

```
Toyota with 4 wheels
  Car with 5 seats
Honda with 2 wheels
  Bike with a 150 cc engine
```

### Person, Student and Teacher: who is the oldest?

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def role(self):
        return "person"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def role(self):
        return f"student in grade {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def role(self):
        return f"teacher of {self.subject}"


people = [
    Student("Sita", 16, 10),
    Teacher("Ramesh", 45, "Maths"),
    Student("Aarav", 17, 11),
    Teacher("Gita", 38, "Science"),
]
for person in people:
    print(f"{person.name} ({person.age}) is a {person.role()}")

oldest = max(people, key=lambda person: person.age)
print("Oldest person:", oldest.name)

students = [person for person in people if isinstance(person, Student)]
oldest_student = max(students, key=lambda person: person.age)
print("Oldest student:", oldest_student.name)
```

Output:

```
Sita (16) is a student in grade 10
Ramesh (45) is a teacher of Maths
Aarav (17) is a student in grade 11
Gita (38) is a teacher of Science
Oldest person: Ramesh
Oldest student: Aarav
```

### Animal, Dog and Cat sounds

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "..."

    def speak(self):
        print(f"{self.name} the {type(self).__name__.lower()} says {self.sound()}")


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


for animal in (Dog("Buddy"), Cat("Misty"), Animal("Nemo")):
    animal.speak()
```

Output:

```
Buddy the dog says Woof
Misty the cat says Meow
Nemo the animal says ...
```

### BankAccount with a private balance and a property

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance                  # private: only methods touch it

    @property
    def balance(self):                            # read-only from outside
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("insufficient balance")
        self.__balance -= amount


account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.balance)

try:
    account.balance = 1000000                   # no setter, so this is refused
except AttributeError as error:
    print("Error:", error)

try:
    account.withdraw(5000)
except ValueError as error:
    print("Error:", error)
```

Output:

```
Balance: 1300
Error: property 'balance' of 'BankAccount' object has no setter
Error: insufficient balance
```

Because `balance` has a getter but no setter, outside code can read it but cannot assign to it. The only ways to change the balance are `deposit()` and `withdraw()`, which check the amount first. (Python 3.10 prints the first error as `can't set attribute 'balance'`.)

## Common mistakes

- The child defines `__init__` but forgets `super().__init__(...)` -> the parent's attributes are never created and you get `AttributeError`; call `super().__init__(...)` first.
- Reading `obj.__secret` from outside the class -> `AttributeError`, because Python renamed it to `_ClassName__secret`; provide a method or a `@property` instead.
- A child of an abstract class forgets one abstract method -> `TypeError` when you create an object; implement every method marked `@abstractmethod`.
- Defining the same method twice hoping for overloading -> only the last definition survives; use default arguments or `*args`.
- Using inheritance for a has-a relationship (`class Car(Engine)`) -> confusing design; store the engine as an attribute instead.
- Comparing two objects with `==` without defining `__eq__` -> Python compares identity, so two equal-looking objects are "not equal"; define `__eq__`.

## Summary

- A child class inherits the attributes and methods of its parent; `super().__init__()` lets the child add attributes without losing the parent's.
- The five types of inheritance are single, multilevel, multiple, hierarchical and hybrid; `ClassName.__mro__` shows the search order for methods.
- A child overrides a method by defining it again; `super().method()` calls the parent's version.
- Polymorphism lets one method name behave differently per class; duck typing needs no shared parent at all.
- Operator overloading uses dunder methods such as `__add__`, `__eq__` and `__lt__`; Python has no true method overloading, so use default arguments and `*args`.
- Public, protected (`_x`) and private (`__x`) attributes differ by convention and name mangling; `@property` with a setter validates values while keeping attribute syntax.
- `abc.ABC` and `@abstractmethod` force child classes to implement required methods; an abstract class cannot be instantiated.
- Composition (has-a) stores objects inside objects; `isinstance()` and `issubclass()` test class relationships.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: OOP Basics](../11-oop-basics/README.md) | [Next: Iterators and Generators](../13-iterators-and-generators/README.md) | [Home](../README.md)
