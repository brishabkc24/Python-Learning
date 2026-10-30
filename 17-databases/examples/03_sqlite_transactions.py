"""Transactions: rollback() undoes uncommitted changes; with connection: commits or rolls back for you.

Run: python 03_sqlite_transactions.py
Creates the file 03_sqlite_transactions.db next to this script. The file is
removed at the start of every run, so running it again gives the same output.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("03_sqlite_transactions.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY, balance INTEGER)")
cursor.executemany("INSERT INTO accounts VALUES (?, ?)", [("Aarav", 500), ("Sita", 300)])
connection.commit()


def show_balances(title):
    cursor.execute("SELECT name, balance FROM accounts ORDER BY name")
    print(f"{title}: {cursor.fetchall()}")


show_balances("Start")

# A change that is not committed can be undone with rollback().
cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE name = 'Aarav'")
show_balances("After the uncommitted update")
connection.rollback()
show_balances("After rollback()")


def transfer(sender, receiver, amount):
    # Using the connection as a context manager: if the block finishes
    # normally the changes are committed; if an error is raised they are
    # rolled back. The connection stays open afterwards.
    with connection:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
        cursor.execute("SELECT balance FROM accounts WHERE name = ?", (sender,))
        if cursor.fetchone()[0] < 0:
            raise ValueError(f"{sender} does not have {amount}")
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))


transfer("Aarav", "Sita", 200)
show_balances("After a good transfer")

try:
    transfer("Sita", "Aarav", 5000)
except ValueError as error:
    print("Transfer failed:", error)
show_balances("After the failed transfer")

connection.close()
