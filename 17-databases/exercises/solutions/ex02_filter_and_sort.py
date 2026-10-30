"""Insert products with executemany, then select those above 100 sorted by price and the two cheapest with LIMIT. Creates ex02_products.db next to this file."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("ex02_products.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")

products = [("Notebook", 120.0), ("Pen", 25.5), ("Backpack", 1500.0),
            ("Calculator", 850.0), ("Eraser", 10.0)]
cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
connection.commit()

print("Products above 100, most expensive first:")
cursor.execute("SELECT name, price FROM products WHERE price > ? ORDER BY price DESC", (100,))
for name, price in cursor.fetchall():
    print(f"  {name:<11} {price:>8.2f}")

print("Two cheapest products:")
cursor.execute("SELECT name, price FROM products ORDER BY price LIMIT 2")
for name, price in cursor.fetchall():
    print(f"  {name:<11} {price:>8.2f}")

connection.close()
