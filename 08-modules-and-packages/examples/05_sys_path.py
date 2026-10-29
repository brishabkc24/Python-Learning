"""
Where Python looks for modules: print sys.path, show where a standard
library module was loaded from, and add a folder to the search path at
run time. The printed paths depend on your computer.

Run: python 05_sys_path.py
"""

import sys
from pathlib import Path

print("Python searches these folders, in order:")
for position, folder in enumerate(sys.path):
    print(" ", position, folder if folder else "(current folder)")

print()
print("The first entry is this script's own folder:")
print(" ", Path(sys.path[0]).name)

# Where did a standard library module come from?
import random
print()
print("random was loaded from:", Path(random.__file__).parent.name, "folder")

# A module that does not exist anywhere on sys.path cannot be imported.
print()
print("is 'greetings' importable from here?", "greetings" in sys.modules or Path(sys.path[0], "greetings.py").exists())

# Adding a folder: the parent of this file's folder, as an example.
extra_folder = str(Path(__file__).resolve().parent.parent)
sys.path.append(extra_folder)
print("added to sys.path:", Path(extra_folder).name)
print("entries now:", len(sys.path))
