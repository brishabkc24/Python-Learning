"""A small StudentDB class that hides the SQL behind add, list, update and delete methods.

Run: python 05_student_db_class.py
Creates the file 05_student_db.db next to this script. The file is removed
at the start of every run, so running it again gives the same output.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("05_student_db.db")
DB_FILE.unlink(missing_ok=True)


class StudentDB:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                marks INTEGER
            )
        """)

    def add(self, name, marks):
        with self.connection:       # commits for us
            cursor = self.connection.execute(
                "INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
        return cursor.lastrowid     # the id SQLite gave the new row

    def list_all(self):
        cursor = self.connection.execute("SELECT id, name, marks FROM students ORDER BY id")
        return cursor.fetchall()

    def update_marks(self, student_id, marks):
        with self.connection:
            cursor = self.connection.execute(
                "UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
        return cursor.rowcount      # 1 if a row was changed, 0 if the id is unknown

    def delete(self, student_id):
        with self.connection:
            cursor = self.connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        return cursor.rowcount

    def close(self):
        self.connection.close()


def show(db, title):
    print(title)
    for student_id, name, marks in db.list_all():
        print(f"  {student_id}. {name:<14} {marks}")


db = StudentDB(DB_FILE)
db.add("Aarav Sharma", 85)
sita_id = db.add("Sita Rai", 92)
db.add("Bikash Thapa", 67)
show(db, "After adding three students:")

print("Rows updated:", db.update_marks(sita_id, 95))
print("Rows updated:", db.update_marks(99, 50))
print("Rows deleted:", db.delete(1))
show(db, "After the update and delete:")

db.close()
