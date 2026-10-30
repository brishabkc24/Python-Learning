# Databases: Exercises

Solutions are in the [solutions](solutions/) folder. Try each exercise yourself before looking. Every solution creates its SQLite file next to itself (for example `ex01_books.db`) and deletes the old file at the start, so you can run it as often as you like. All exercises use the built-in `sqlite3` module; no MySQL server is needed.

## 1. Books table

**Create and insert.** Create a table `books` with the columns `id` (primary key), `title`, `author`, `year` and `price`. Insert three books using `?` placeholders, commit, and print every row with `fetchall()`.

Example:

```
1. The Hobbit by J. R. R. Tolkien (1937) - 15.00
2. 1984 by George Orwell (1949) - 10.99
3. Clean Code by Robert C. Martin (2008) - 35.50
```

## 2. Filter and sort

**WHERE, ORDER BY and LIMIT.** Insert five products with `executemany()`: Notebook 120.0, Pen 25.5, Backpack 1500.0, Calculator 850.0, Eraser 10.0. Print the products that cost more than 100, most expensive first. Then print the two cheapest products using `LIMIT`.

Example:

```
Products above 100, most expensive first:
  Backpack     1500.00
  Calculator    850.00
  Notebook      120.00
Two cheapest products:
  Eraser         10.00
  Pen            25.50
```

## 3. Update and delete

**rowcount and COUNT.** Using the products Notebook 120.0, Pen 25.5, Backpack 1500.0 and Eraser 10.0, raise the price of the Notebook by 10 percent with `UPDATE`, then delete the cheapest product with `DELETE`. After each statement print `cursor.rowcount`. Print the number of products before and after using `COUNT(*)`.

Example:

```
Products before: 4
Rows updated: 1
Notebook now costs 132.00
Rows deleted: 1
Products after: 3
```

## 4. Books from CSV

**Load a dataset.** Read `datasets/books.csv` with the `csv` module and insert every row into a `books` table. Then use SQL to find the most expensive book, the number of books per genre (most common genre first) and the average price.

Example:

```
Loaded 10 books
Most expensive: Clean Code (35.50)
Books per genre:
  Fiction      3
  Programming  2
  Dystopian    1
  Fantasy      1
  History      1
  Romance      1
  Science      1
Average price: 17.90
```

## 5. Students by city

**GROUP BY with several aggregates.** Load `datasets/students.csv` into a table. Print one line per city with the number of students, their average marks and their best marks, sorted by average marks from high to low.

Example:

```
City        Count  Average  Best
Bhaktapur       1     95.0    95
Pokhara         2     82.5    92
Butwal          1     78.0    78
Kathmandu       3     70.3    88
Lalitpur        1     67.0    67
Dharan          1     59.0    59
Biratnagar      1     45.0    45
```

## 6. NotesDB class

**Hide the SQL in a class.** Write a `NotesDB` class with the methods `add(text)` (returns the new id), `list_all()`, `search(word)` (uses `LIKE` to find notes containing the word) and `delete(note_id)` (returns the number of rows deleted). Add three notes, list them, search for `Python`, delete note 1 twice and print the number of notes left.

Example:

```
All notes:
  1. Buy milk and eggs
  2. Finish the Python exercises
  3. Call the Python study group
Notes containing 'Python':
  2. Finish the Python exercises
  3. Call the Python study group
Deleted: 1
Deleted: 0
Notes left: 2
```

## 7. Money transfer with rollback

**All or nothing.** Create an `accounts` table with Priya (1000) and Rohan (200). Write `transfer(sender, receiver, amount)` that subtracts from the sender, checks that the sender's balance did not go below zero, and adds to the receiver, all inside `with connection:`. If the balance would go negative, raise `ValueError` so the whole transfer is rolled back. Show a transfer that works and one that fails; after the failed one both balances must be unchanged.

Example:

```
Start: [('Priya', 1000), ('Rohan', 200)]
After sending 300: [('Priya', 700), ('Rohan', 500)]
Failed: Rohan has only 500, cannot send 900
After the failed transfer: [('Priya', 700), ('Rohan', 500)]
```
