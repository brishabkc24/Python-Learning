"""The four CRUD operations: Create, Read, Update, Delete, plus executemany.

Run: python 02_sqlite_crud.py
Creates the file 02_sqlite_crud.db next to this script. The file is
removed at the start of every run, so running it again gives the same output.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("02_sqlite_crud.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        stock INTEGER
    )
""")

# Create: executemany() runs the same INSERT once per tuple in the list.
products = [
    ("Notebook", 120.0, 50),
    ("Pen", 25.5, 200),
    ("Backpack", 1500.0, 8),
    ("Calculator", 850.0, 15),
]
cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products)
connection.commit()


def show_all(title):
    print(title)
    cursor.execute("SELECT id, name, price, stock FROM products ORDER BY price DESC")
    for product_id, name, price, stock in cursor.fetchall():
        print(f"  {product_id}  {name:<11} {price:>8.2f}  stock {stock}")


# Read
show_all("All products, most expensive first:")

# Update: rowcount tells how many rows were changed.
cursor.execute("UPDATE products SET price = ? WHERE name = ?", (30.0, "Pen"))
connection.commit()
print(f"Updated {cursor.rowcount} row(s).")

# Delete
cursor.execute("DELETE FROM products WHERE stock < ?", (10,))
connection.commit()
print(f"Deleted {cursor.rowcount} row(s).")

show_all("After the update and delete:")

# Aggregates: COUNT and AVG work on the remaining rows.
cursor.execute("SELECT COUNT(*), AVG(price) FROM products")
count, average_price = cursor.fetchone()
print(f"{count} products left, average price {average_price:.2f}")

connection.close()
