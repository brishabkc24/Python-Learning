# OOP Basics: Exercises

Solve each exercise in its own file. Compare your answer with the file of the same number in [solutions/](solutions/).

## 1. Introduce yourself

**Task:** Write a `Person` class with the attributes `name` and `city`, set in `__init__`. Add a method `introduce()` that prints one sentence. Create two people and call `introduce()` on each.

Example:

```
Hi, I am Sita from Pokhara.
Hi, I am Aarav from Kathmandu.
```

## 2. Rectangle

**Task:** Write a `Rectangle` class with `width` and `height`. Add the methods `area()`, `perimeter()` and `is_square()`, which returns `True` when the width equals the height. Create a 4 x 6 rectangle and a 5 x 5 rectangle and print the result of each method.

Example:

```
Rectangle 4 x 6: area 24, perimeter 20, square? False
Rectangle 5 x 5: area 25, perimeter 20, square? True
```

## 3. Count the objects

**Task:** Write an `Employee` class with a class attribute `company = "Example Tech"` and a class attribute `count` that starts at 0 and goes up by one every time an employee is created. Each employee has a `name` and a `salary`. Create three employees, print the count, then change `company` through the class and show that every employee sees the new name.

Example:

```
Employees created: 3
Asha works at Example Tech
Bibek works at Example Tech
Deepa works at Example Tech
After the rename:
Asha works at Example Software
Bibek works at Example Software
Deepa works at Example Software
```

## 4. Printable books

**Task:** Write a `Book` class with `title`, `author` and `year`. Give it a `__str__` that returns text like `The Hobbit by J. R. R. Tolkien (1937)` and a `__repr__` that returns text like `Book('The Hobbit', 'J. R. R. Tolkien', 1937)`. Create three books, print one of them with `print()`, and print the whole list to see `__repr__` at work.

Example:

```
The Hobbit by J. R. R. Tolkien (1937)
[Book('The Hobbit', 'J. R. R. Tolkien', 1937), Book('1984', 'George Orwell', 1949), Book('Sapiens', 'Yuval Noah Harari', 2011)]
```

## 5. Bank account with history

**Task:** Write a `BankAccount` class with `owner`, `balance` (default 0) and a `history` list. `deposit(amount)` and `withdraw(amount)` must refuse amounts that are not positive, `withdraw` must refuse to go below zero, and every successful action must be added to `history` as text. Add `show_history()` that prints each entry on its own line and the final balance.

Example:

```
Refused: cannot withdraw 2000, balance is 1500
Refused: amount must be positive
History of Asha:
  deposit 500
  withdraw 300
Final balance: 1200
```

## 6. Shopping cart

**Task:** Write an `Item` class (`name`, `price`, `quantity`) with a method `cost()` that returns `price * quantity`. Then write a `Cart` class that keeps a list of items, with `add_item(item)`, `remove_item(name)`, `total()` and `show()`. Removing a name that is not in the cart prints a message instead of failing.

Example:

```
Cart:
  Notebook     x 3 =   150.00
  Pen          x 5 =    50.00
  Backpack     x 1 =  1200.00
Total: 1400.00
Not in cart: Ruler
After removing Pen, total: 1350.00
```

## 7. Students from a CSV file

**Task:** Write a `Student` class with `name`, `age`, `city` and `marks`. Add a class method `from_row(cls, row)` that builds a `Student` from a dictionary produced by `csv.DictReader` (convert `age` and `marks` to `int`). Read every row of `datasets/students.csv` into a list of `Student` objects, then print the three students with the highest marks, the class average with two decimals, and the names of students with fewer than 40 marks. Locate the dataset relative to your script with `Path(__file__)`.

Example:

```
Students loaded: 10
Top 3:
  Kiran Adhikari (95)
  Sita Rai (92)
  Anjali Shrestha (88)
Average marks: 72.00
Below 40: Maya Limbu
```

## 8. Products with class and static methods

**Task:** Write a `Product` class with `name`, `price` and `stock`, a class attribute `tax_rate = 13` (percent), a static method `price_with_tax(price)` that returns the price plus tax, and a class method `from_string(cls, text)` that builds a product from text like `"Pen,10,100"`. Add an instance method `stock_value()` that returns `price * stock`. Create at least four products (some with `from_string`), then print the price with tax of each, the product with the highest stock value using `max()` with a `key`, and the total stock value of all products.

Example:

```
Pen        price 10.00  with tax 11.30
Notebook   price 50.00  with tax 56.50
Backpack   price 1200.00  with tax 1356.00
Pencil     price 5.00  with tax 5.65
Highest stock value: Backpack (24000.00)
Total stock value: 27000.00
```
