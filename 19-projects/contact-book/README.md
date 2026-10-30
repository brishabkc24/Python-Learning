# Contact Book

## What it does

A menu-driven address book. Each contact has a name, a phone number and an email address. You can add, search, update, delete and list contacts. Everything is saved to `contacts.csv` in this folder, so the book is still there the next time you run the program.

## Concepts used

- The `csv` module: `DictReader` to load rows as dictionaries and `DictWriter` to save them
- A custom exception class, `ContactNotFoundError`, raised by `find_contact()` and caught by the menu loop
- A dictionary that maps menu choices to functions (`actions`)
- List comprehensions for searching
- `sorted()` with a `key` function for the alphabetical listing
- `pathlib.Path(__file__)` to find the CSV file next to the script
- Formatted output with `f"{value:<20}"` to line up columns

## Files

| File | Purpose |
|---|---|
| `contact_book.py` | the program |
| `contacts.csv` | created automatically on the first save; holds the contacts |

## How to run

```
cd 19-projects/contact-book
python contact_book.py
```

## Sample session

```
Contact Book (0 contact(s) in contacts.csv)

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 1
Name: Asha Rai
Phone: 9800000001
Email: asha@example.com
Saved Asha Rai.

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 1
Name: Bikash Thapa
Phone: 9800000002
Email: bikash@example.com
Saved Bikash Thapa.

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 2
Name to search: asha
Asha Rai             9800000001   asha@example.com

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 3
Name of the contact to update: asha rai
Press Enter to keep the current value.
Phone [9800000001]: 9800000009
Email [asha@example.com]:
Updated Asha Rai.

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 4
Name of the contact to delete: Nobody
Error: No contact named 'Nobody'.

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 5
Name                 Phone        Email
--------------------------------------------------
Asha Rai             9800000009   asha@example.com
Bikash Thapa         9800000002   bikash@example.com
2 contact(s).

1. Add  2. Search  3. Update  4. Delete  5. List all  6. Quit
Choose (1-6): 6
Goodbye!
```

## Ideas to extend it

- Check that the phone number contains only digits before saving.
- Add a "birthday" column and list contacts with a birthday this month.
- Export the contacts to a JSON file.

---

[Back to the project index](../README.md)
