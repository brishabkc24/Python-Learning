"""Write a NotesDB class with add, list_all, search and delete methods around a SQLite table. Creates ex06_notes.db next to this file."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("ex06_notes.db")
DB_FILE.unlink(missing_ok=True)


class NotesDB:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)")

    def add(self, text):
        with self.connection:
            cursor = self.connection.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        return cursor.lastrowid

    def list_all(self):
        return self.connection.execute("SELECT id, text FROM notes ORDER BY id").fetchall()

    def search(self, word):
        # LIKE with % on both sides finds the word anywhere in the text.
        return self.connection.execute(
            "SELECT id, text FROM notes WHERE text LIKE ? ORDER BY id", (f"%{word}%",)).fetchall()

    def delete(self, note_id):
        with self.connection:
            cursor = self.connection.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        return cursor.rowcount

    def close(self):
        self.connection.close()


notes = NotesDB(DB_FILE)
notes.add("Buy milk and eggs")
notes.add("Finish the Python exercises")
notes.add("Call the Python study group")

print("All notes:")
for note_id, text in notes.list_all():
    print(f"  {note_id}. {text}")

print("Notes containing 'Python':")
for note_id, text in notes.search("Python"):
    print(f"  {note_id}. {text}")

print("Deleted:", notes.delete(1))
print("Deleted:", notes.delete(1))
print("Notes left:", len(notes.list_all()))
notes.close()
