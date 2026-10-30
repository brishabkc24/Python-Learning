# Student Management System

## What it does

A menu-driven program that keeps student records in an SQLite database. You can add a student, list everyone, search by name, update marks, delete a student and show the top students. Each record gets a grade (A to F) worked out from the marks.

On the first run the program creates `students.db` in this folder and fills it with the ten students from the repository file `datasets/students.csv`. After that it reads and writes the database only.

## Concepts used

- Two classes: `Student` (one record, with a `grade` property and `__str__`) and `StudentDB` (every database operation)
- The `sqlite3` module: `CREATE TABLE IF NOT EXISTS`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `ORDER BY ... LIMIT`
- Parameterised queries with `?` placeholders, never string formatting, so the input is safe
- `executemany()` to load the CSV rows in one go
- `cursor.rowcount` to find out whether an update or delete changed a row
- `pathlib.Path(__file__).resolve().parents[2]` to find the repository `datasets` folder from any working directory
- A reusable `ask_int()` function that validates numbers and ranges

## Files

| File | Purpose |
|---|---|
| `student_management.py` | the program |
| `students.db` | created on the first run; the SQLite database |
| `../../datasets/students.csv` | the sample data used to fill the database once |

## How to run

```
cd 19-projects/student-management
python student_management.py
```

Delete `students.db` to start again from the CSV file.

## Sample session

```
First run: loaded 10 students from students.csv.
Student Management (10 students in students.db)

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 6
How many top students? 3
ID  Name                 Age  City          Marks  Grade
9   Kiran Adhikari       22   Bhaktapur     95     A
2   Sita Rai             21   Pokhara       92     A
6   Anjali Shrestha      21   Kathmandu     88     B

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 3
Name contains: rai
ID  Name                 Age  City          Marks  Grade
2   Sita Rai             21   Pokhara       92     A

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 1
Name: Asha Rai
Age: 20
City: Pokhara
Marks (0-100): 81
Added Asha Rai with id 11.

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 4
Student id: 99
New marks (0-100): 50
No student with id 99.

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 5
Student id to delete: 11
Deleted.

1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit
Choose (1-7): 7
Goodbye!
```

## Ideas to extend it

- Add a column for the course name and let the user filter by it.
- Show the average marks per city with `GROUP BY`.
- Export the table back to a CSV file.

---

[Back to the project index](../README.md)
