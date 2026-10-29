"""
OrderedDict: move_to_end, popitem(last=False), and equality that depends
on order. Used here to keep a short "recently opened files" list where
the most recent item is always at the end.

Run: python 04_ordereddict.py
"""

from collections import OrderedDict

recent_files = OrderedDict()
LIMIT = 3


def open_file(name):
    """Record that a file was opened, keeping only the last LIMIT names."""
    if name in recent_files:
        recent_files.move_to_end(name)      # already listed: make it newest
    else:
        recent_files[name] = True
        if len(recent_files) > LIMIT:
            oldest, _ = recent_files.popitem(last=False)
            print("   dropped oldest:", oldest)
    print("opened", name, "->", list(recent_files))


open_file("notes.txt")
open_file("report.docx")
open_file("budget.xlsx")
open_file("notes.txt")        # moves to the end, nothing dropped
open_file("photo.png")        # report.docx is now the oldest and goes

print()
# move_to_end with last=False sends a key to the front.
recent_files.move_to_end("photo.png", last=False)
print("photo.png moved to the front:", list(recent_files))

print()
# Equality: OrderedDict cares about order, dict does not.
first = OrderedDict([("a", 1), ("b", 2)])
second = OrderedDict([("b", 2), ("a", 1)])
print("OrderedDict equal?", first == second)
print("dict equal?", dict(first) == dict(second))

# A plain dict keeps insertion order too (since Python 3.7).
plain = {}
plain["z"] = 1
plain["a"] = 2
print("plain dict order:", list(plain))
