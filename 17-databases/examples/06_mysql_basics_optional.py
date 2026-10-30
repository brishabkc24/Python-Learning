"""OPTIONAL: connect to a MySQL server, create a database and a table, insert and read rows.

Needs a running MySQL server and the package: pip install mysql-connector-python
Run: python 06_mysql_basics_optional.py
Set the environment variables MYSQL_USER and MYSQL_PASSWORD to your own
login; otherwise the placeholders root / your_password are used.
"""

import os

try:
    import mysql.connector
except ImportError:
    raise SystemExit("mysql-connector-python is not installed. "
                     "Run: pip install mysql-connector-python")

HOST = "localhost"
USER = os.environ.get("MYSQL_USER", "root")
PASSWORD = os.environ.get("MYSQL_PASSWORD", "your_password")

try:
    connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
except mysql.connector.Error as error:
    raise SystemExit(f"Could not connect to MySQL on {HOST}: {error}")

cursor = connection.cursor()

# Databases and tables are created with ordinary SQL statements.
cursor.execute("CREATE DATABASE IF NOT EXISTS learning_db")
cursor.execute("USE learning_db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        city VARCHAR(50),
        marks INT
    )
""")

# MySQL uses %s as the placeholder, not ? as in sqlite3.
students = [("Aarav Sharma", "Kathmandu", 85), ("Sita Rai", "Pokhara", 92)]
cursor.executemany("INSERT INTO students (name, city, marks) VALUES (%s, %s, %s)", students)
connection.commit()
print(f"Inserted {cursor.rowcount} rows.")

cursor.execute("SELECT id, name, city, marks FROM students ORDER BY id")
for student_id, name, city, marks in cursor.fetchall():
    print(f"{student_id}. {name} from {city}: {marks}")

cursor.close()
connection.close()
print("Connection closed.")
