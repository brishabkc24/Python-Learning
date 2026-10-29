"""Exercise 6: keep the three most recently used keys in an OrderedDict."""

from collections import OrderedDict

LIMIT = 3
recent = OrderedDict()

for item in ["a", "b", "c", "a", "d", "b"]:
    if item in recent:
        recent.move_to_end(item)
    else:
        recent[item] = True
        if len(recent) > LIMIT:
            recent.popitem(last=False)
    print(item, "->", list(recent))
