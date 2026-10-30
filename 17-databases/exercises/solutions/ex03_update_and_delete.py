"""Raise the price of one product by 10 percent, delete the cheapest, and report rowcount and the remaining count. Creates ex03_update_delete.db next to this file."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("ex03_update_delete.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)",
                   [("Notebook", 120.0), ("Pen", 25.5), ("Backpack", 1500.0), ("Eraser", 10.0)])
connection.commit()


def count_products():
    cursor.execute("SELECT COUNT(*) FROM products")
    return cursor.fetchone()[0]


print("Products before:", count_products())

cursor.execute("UPDATE products SET price = price * 1.10 WHERE name = ?", ("Notebook",))
connection.commit()
print("Rows updated:", cursor.rowcount)

cursor.execute("SELECT price FROM products WHERE name = ?", ("Notebook",))
print(f"Notebook now costs {cursor.fetchone()[0]:.2f}")

cursor.execute("DELETE FROM products WHERE price = (SELECT MIN(price) FROM products)")
connection.commit()
print("Rows deleted:", cursor.rowcount)

print("Products after:", count_products())
connection.close()
