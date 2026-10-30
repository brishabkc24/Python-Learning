"""
Demonstrates write(), writelines(), appending with mode "a", and moving
inside a file with seek() and tell().
Run: python 03_writing_and_appending.py
Creates output_log.txt and output_position.txt next to this script.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG_FILE = HERE / "output_log.txt"
POSITION_FILE = HERE / "output_position.txt"

# Mode "w" creates the file, or empties it if it already exists.
with open(LOG_FILE, "w", encoding="utf-8") as file:
    file.write("Program started\n")      # write() takes exactly one string
    file.write("Loading settings\n")     # we must add "\n" ourselves

# Mode "a" adds to the end and never erases what is already there.
# writelines() takes a list of strings and does NOT add newlines.
more_lines = ["Settings loaded\n", "Ready\n"]
with open(LOG_FILE, "a", encoding="utf-8") as file:
    file.writelines(more_lines)

print("Log file now contains:")
with open(LOG_FILE, encoding="utf-8") as file:
    print(file.read(), end="")

# tell() reports the current position, seek() moves it.
# Positions are counted in bytes from the start of the file, and for
# plain English text one character is one byte.
with open(POSITION_FILE, "w", encoding="utf-8") as file:
    file.write("Python is fun")

with open(POSITION_FILE, encoding="utf-8") as file:
    print("Position at start:", file.tell())
    word = file.read(6)
    print("read(6) gave", repr(word), "and moved to position", file.tell())
    file.seek(0)
    print("After seek(0) the position is", file.tell())
    print("Reading everything again:", repr(file.read()))
    file.seek(10)
    print("After seek(10) read() gives:", repr(file.read()))
