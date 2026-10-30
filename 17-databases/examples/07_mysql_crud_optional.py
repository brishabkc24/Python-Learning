"""OPTIONAL: CRUD on a MySQL table with %s placeholders (create, read, update, delete).

Needs a running MySQL server and the package: pip install mysql-connector-python
Run: python 07_mysql_crud_optional.py   (run 06_mysql_basics_optional.py first)
Set MYSQL_USER and MYSQL_PASSWORD to your own login; otherwise the
placeholders root / your_password are used.
"""

import os

try:
    import mysql.connector
except ImportError:
    raise SystemExit("mysql-connector-python is not installed. "
                     "Run: pip install mysql-connector-python")

USER = os.environ.get("MYSQL_USER", "root")
PASSWORD = os.environ.get("MYSQL_PASSWORD", "your_password")

try:
    connection = mysql.connector.connect(
        host="localhost", user=USER, password=PASSWORD, database="learning_db")
except mysql.connector.Error as error:
    raise SystemExit(f"Could not connect to MySQL: {error}")

cursor = connection.cursor()


def show_all(title):
    print(title)
    cursor.execute("SELECT id, name, marks FROM students ORDER BY id")
    for student_id, name, marks in cursor.fetchall():
        print(f"  {student_id}. {name}: {marks}")


# Create
cursor.execute("INSERT INTO students (name, city, marks) VALUES (%s, %s, %s)",
               ("Bikash Thapa", "Lalitpur", 67))
connection.commit()
show_all("After insert:")

# Update
cursor.execute("UPDATE students SET marks = %s WHERE name = %s", (70, "Bikash Thapa"))
connection.commit()
print(f"Updated {cursor.rowcount} row(s).")

# Read with a condition
cursor.execute("SELECT name FROM students WHERE marks >= %s", (70,))
print("Marks 70 or more:", [name for (name,) in cursor.fetchall()])

# Delete
cursor.execute("DELETE FROM students WHERE name = %s", ("Bikash Thapa",))
connection.commit()
print(f"Deleted {cursor.rowcount} row(s).")
show_all("After delete:")

cursor.close()
connection.close()
