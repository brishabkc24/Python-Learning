"""
Demonstrates checking whether a file exists with pathlib and os.path, the
basic pathlib operations, and the three common file errors:
FileNotFoundError, FileExistsError and PermissionError.
Run: python 04_paths_and_errors.py
Creates output_pathlib.txt next to this script.
"""

import os
import stat
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"

# Two ways to check whether a file exists.
text_file = DATA_DIR / "sample_text.txt"
print("pathlib exists() :", text_file.exists())
print("os.path.exists() :", os.path.exists(text_file))
print("Missing file     :", (DATA_DIR / "missing.txt").exists())

# pathlib basics: join with "/", read and write in one call, name parts.
note_file = HERE / "output_pathlib.txt"
note_file.write_text("Written with pathlib.\n", encoding="utf-8")
print("read_text():", note_file.read_text(encoding="utf-8").strip())
print("name  :", note_file.name)
print("stem  :", note_file.stem)
print("suffix:", note_file.suffix)

# FileNotFoundError: reading a file that is not there.
try:
    open(DATA_DIR / "missing.txt", encoding="utf-8")
except FileNotFoundError:
    print("Error: missing.txt does not exist")

# FileExistsError: mode "x" refuses to overwrite an existing file.
try:
    open(note_file, "x", encoding="utf-8")
except FileExistsError:
    print("Error: output_pathlib.txt already exists, mode x refused")

# PermissionError: writing to a file that is read-only.
os.chmod(note_file, stat.S_IREAD)          # make the file read-only
try:
    open(note_file, "w", encoding="utf-8")
except PermissionError:
    print("Error: no permission to write output_pathlib.txt")
os.chmod(note_file, stat.S_IREAD | stat.S_IWRITE)   # make it writable again
