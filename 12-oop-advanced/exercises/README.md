# OOP Advanced: Exercises

Solve each exercise in its own file. Compare your answer with the file of the same number in [solutions/](solutions/).

## 1. Vehicle family

**Task:** Write a `Vehicle` class with `brand` and `wheels` and a `display()` method. Write a `Car` child that always has 4 wheels and adds a `seats` attribute, and a `Bike` child that always has 2 wheels. `Car.display()` must call the parent's `display()` with `super()` and then print the seats. Create a few vehicles, display each one and print the total number of wheels.

Example:

```
Car: Toyota with 4 wheels
  seats: 5
Bike: Honda with 2 wheels
Car: Suzuki with 4 wheels
  seats: 7
Total wheels: 10
```

## 2. Extend, do not replace

**Task:** Write an `Employee` class with `name`, `salary` and an `introduce()` method. Write a `Manager` child that adds `team_size` through `super().__init__()` and overrides `introduce()` so that it first calls the parent's version with `super()` and then prints one more line.

Example:

```
I am Asha and I earn 50000
I am Deepa and I earn 91000
I manage a team of 6 people
Is deepa an Employee? True
```

## 3. Shapes with polymorphism

**Task:** Write a `Shape` parent with an `area()` method that returns 0. Write `Circle`, `Rectangle` and `Triangle` children that each override `area()`. Put one of each in a list, print every area with two decimals, then print the total area and the name of the largest shape using `max()` with a `key`.

Example:

```
Circle     area = 28.27
Rectangle  area = 20.00
Triangle   area = 21.00
Total area: 69.27
Largest: Circle
```

## 4. Distance operators

**Task:** Write a `Distance` class that stores kilometres. Define `__add__`, `__eq__`, `__lt__`, `__str__` and `__repr__` so that `+`, `==`, `<`, `max()`, `sorted()` and `sum()` all work on distances. For `sum()`, pass `Distance(0)` as the start value.

Example:

```
Morning + evening: 8.5 km
Equal?             True
Evening shorter?   True
Longest:           12 km
Sorted:            [Distance(3.5), Distance(5), Distance(12)]
Weekly total:      20.5 km
```

## 5. Temperature property

**Task:** Write a `Temperature` class with a private attribute behind a `celsius` property. The setter must raise `ValueError` for values below -273.15. Add a read-only `fahrenheit` property that is computed from the Celsius value. Show a valid change, a rejected change and an attempt to assign `fahrenheit`.

Example:

```
22 C = 71.6 F
30 C = 86.0 F
Error: -300 is below absolute zero
Error: fahrenheit is read-only
Still 30 C
```

## 6. Abstract payments

**Task:** Using `abc.ABC` and `@abstractmethod`, write an abstract `Payment` class with a `customer` attribute, an abstract `pay(amount)` method and a normal `receipt(amount)` method. Implement `CardPayment`, `CashPayment` and `WalletPayment`. Call `pay(1250)` on one of each, then show the `TypeError` you get when trying to create a `Payment` directly.

Example:

```
Charging 1250.00 to the card of Asha
Receipt for Asha: 1250.00 paid by CardPayment
Bibek hands over 1250.00 in cash
Receipt for Bibek: 1250.00 paid by CashPayment
Deducting 1250.00 from the wallet of Deepa
Receipt for Deepa: 1250.00 paid by WalletPayment
Error: Can't instantiate abstract class Payment without an implementation for abstract method 'pay'
```

## 7. A school of people

**Task:** Write a `Person` parent with `name` and `age`, and `Student` (adds `grade`) and `Teacher` (adds `subject`) children, each with its own `__str__`. Write a `School` class that contains a list of people with `add_person()`, `__len__`, `__iter__`, a `count(kind)` method that uses `isinstance()`, and an `oldest()` method that uses `max()` with a `key`.

Example:

```
Sunrise School has 5 people:
 - Sita (16), grade 10
 - Ramesh (45), teaches Maths
 - Aarav (17), grade 11
 - Gita (38), teaches Science
 - Priya (15), grade 9
Students: 3
Teachers: 2
Oldest:   Ramesh (45), teaches Maths
```

## 8. Payroll from a JSON file

**Task:** Write an `Employee` parent (`name`, `department`, `calculate_salary()` returning 0, `show()`), a `PermanentEmployee` child whose salary is the base salary plus a 10 percent bonus plus an allowance of 2000, and a `TemporaryEmployee` child paid `hourly_rate * hours`. Give `PermanentEmployee` a class method `from_record(cls, record)` that builds an object from one dictionary of `datasets/employees.json`. Load every record from the file, add two temporary employees of your own, then print each person, the total payroll, the best paid person and how many are permanent and temporary. Locate the dataset relative to your script with `Path(__file__)`.

Example:

```
Asha Koirala     Engineering      PermanentEmployee    95500.00
Bibek Thapa      Marketing        PermanentEmployee    70200.00
Deepa Rana       Engineering      PermanentEmployee   102100.00
Kiran Basnet     Finance          PermanentEmployee    79000.00
Mina Gurung      Human Resources  PermanentEmployee    65800.00
Nikesh Shrestha  Engineering      PermanentEmployee    87800.00
Pooja Maharjan   Marketing        PermanentEmployee    74600.00
Suman Adhikari   Finance          PermanentEmployee    82300.00
Rita Lama        Marketing        TemporaryEmployee    45000.00
Sanjay Pandey    Engineering      TemporaryEmployee    48000.00

Staff: 10  Total payroll: 750300.00
Best paid: Deepa Rana (102100.00)
Permanent: 8, temporary: 2
```
