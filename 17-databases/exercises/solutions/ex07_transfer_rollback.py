"""Move money between two accounts inside a transaction so that a failed transfer leaves both balances unchanged. Creates ex07_bank.db next to this file."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("ex07_bank.db")
DB_FILE.unlink(missing_ok=True)

connection = sqlite3.connect(DB_FILE)
connection.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY, balance INTEGER)")
with connection:
    connection.executemany("INSERT INTO accounts VALUES (?, ?)", [("Priya", 1000), ("Rohan", 200)])


def balances():
    return connection.execute("SELECT name, balance FROM accounts ORDER BY name").fetchall()


def transfer(sender, receiver, amount):
    # If anything inside this block raises, the with statement rolls back
    # every change made in the block; otherwise it commits them.
    with connection:
        connection.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
        remaining = connection.execute(
            "SELECT balance FROM accounts WHERE name = ?", (sender,)).fetchone()[0]
        if remaining < 0:
            raise ValueError(f"{sender} has only {remaining + amount}, cannot send {amount}")
        connection.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))


print("Start:", balances())

transfer("Priya", "Rohan", 300)
print("After sending 300:", balances())

try:
    transfer("Rohan", "Priya", 900)
except ValueError as error:
    print("Failed:", error)
print("After the failed transfer:", balances())

connection.close()
