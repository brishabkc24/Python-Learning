"""
Student Management System
=========================
A menu-driven program that keeps student records in an SQLite database,
students.db, next to this script. On the first run the table is filled
from the repository file datasets/students.csv. A Student class holds one
record and a StudentDB class does all the database work.

Run: python student_management.py

Sample session:
    Choose (1-7): 6
    How many top students? 3
    ID  Name                 Age  City          Marks  Grade
    9   Kiran Adhikari       22   Bhaktapur     95     A
    ...
"""

import csv
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "students.db"
# parents[2] is the repository root: student-management -> 19-projects -> root
CSV_FILE = Path(__file__).resolve().parents[2] / "datasets" / "students.csv"

MENU = "\n1. Add  2. List all  3. Search  4. Update marks  5. Delete  6. Top students  7. Quit"


class Student:
    """One student record."""

    def __init__(self, student_id, name, age, city, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    @property
    def grade(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        if self.marks >= 60:
            return "C"
        if self.marks >= 40:
            return "D"
        return "F"

    def __str__(self):
        return f"{self.student_id:<3} {self.name:<20} {self.age:<4} {self.city:<13} {self.marks:<6} {self.grade}"


class StudentDB:
    """All reading and writing of the students table."""

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS students ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, "
            "age INTEGER, city TEXT, marks INTEGER)"
        )
        self.connection.commit()

    def count(self):
        return self.connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]

    def seed_from_csv(self, csv_path):
        """Copy the rows of the CSV file into the table (used once, on first run)."""
        with open(csv_path, newline="", encoding="utf-8") as file:
            rows = [(row["name"], int(row["age"]), row["city"], int(row["marks"]))
                    for row in csv.DictReader(file)]
        self.connection.executemany(
            "INSERT INTO students (name, age, city, marks) VALUES (?, ?, ?, ?)", rows)
        self.connection.commit()
        return len(rows)

    def add(self, name, age, city, marks):
        cursor = self.connection.execute(
            "INSERT INTO students (name, age, city, marks) VALUES (?, ?, ?, ?)",
            (name, age, city, marks))
        self.connection.commit()
        return cursor.lastrowid

    def _fetch(self, sql, parameters=()):
        rows = self.connection.execute(sql, parameters).fetchall()
        return [Student(*row) for row in rows]

    def all(self):
        return self._fetch("SELECT id, name, age, city, marks FROM students ORDER BY id")

    def search(self, name_part):
        return self._fetch("SELECT id, name, age, city, marks FROM students "
                           "WHERE name LIKE ? ORDER BY id", (f"%{name_part}%",))

    def top(self, how_many):
        return self._fetch("SELECT id, name, age, city, marks FROM students "
                           "ORDER BY marks DESC LIMIT ?", (how_many,))

    def update_marks(self, student_id, marks):
        """Return True if a row was changed, False if the id does not exist."""
        cursor = self.connection.execute(
            "UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
        self.connection.commit()
        return cursor.rowcount == 1

    def delete(self, student_id):
        cursor = self.connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.connection.commit()
        return cursor.rowcount == 1

    def close(self):
        self.connection.close()


def ask_int(prompt, lowest, highest):
    """Ask until the user types a whole number between lowest and highest."""
    while True:
        answer = input(prompt).strip()
        try:
            value = int(answer)
        except ValueError:
            print("Please type a whole number.")
            continue
        if lowest <= value <= highest:
            return value
        print(f"Please enter a value from {lowest} to {highest}.")


def print_table(students):
    if not students:
        print("No students found.")
        return
    print(f"{'ID':<3} {'Name':<20} {'Age':<4} {'City':<13} {'Marks':<6} Grade")
    for student in students:
        print(student)


def main():
    db = StudentDB(DB_FILE)
    if db.count() == 0:
        added = db.seed_from_csv(CSV_FILE)
        print(f"First run: loaded {added} students from {CSV_FILE.name}.")
    print(f"Student Management ({db.count()} students in {DB_FILE.name})")

    while True:
        print(MENU)
        choice = input("Choose (1-7): ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            if name == "":
                print("The name cannot be empty.")
                continue
            age = ask_int("Age: ", 5, 100)
            city = input("City: ").strip()
            marks = ask_int("Marks (0-100): ", 0, 100)
            new_id = db.add(name, age, city, marks)
            print(f"Added {name} with id {new_id}.")
        elif choice == "2":
            print_table(db.all())
        elif choice == "3":
            print_table(db.search(input("Name contains: ").strip()))
        elif choice == "4":
            student_id = ask_int("Student id: ", 1, 1_000_000)
            marks = ask_int("New marks (0-100): ", 0, 100)
            print("Updated." if db.update_marks(student_id, marks) else f"No student with id {student_id}.")
        elif choice == "5":
            student_id = ask_int("Student id to delete: ", 1, 1_000_000)
            print("Deleted." if db.delete(student_id) else f"No student with id {student_id}.")
        elif choice == "6":
            print_table(db.top(ask_int("How many top students? ", 1, 100)))
        elif choice == "7":
            db.close()
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
