"""
The four import styles shown with the math module, and a demonstration
of why "from module import *" is risky: it quietly replaces the built-in
pow function.

Run: python 01_import_styles.py
"""

# Style 1: import the module and use its name as a prefix.
import math
print("import math            ->", math.sqrt(49), math.pi)

# Style 2: import with a shorter alias.
import math as m
print("import math as m       ->", m.sqrt(49), m.floor(2.9))

# Style 3: import only the names you need.
from math import sqrt, ceil
print("from math import sqrt  ->", sqrt(49), ceil(2.1))

# You can rename a single function as well.
from math import factorial as fact
print("factorial as fact      ->", fact(6))

# The module object itself can be inspected.
print("module name:", math.__name__)
print("same module twice?", math is m)

# Style 4: import everything. Watch the built-in pow change its behaviour.
print()
print("built-in pow(2, 3) ->", pow(2, 3), type(pow(2, 3)).__name__)
from math import *
print("after 'from math import *', pow(2, 3) ->", pow(2, 3), type(pow(2, 3)).__name__)
print("The name pow now refers to math.pow, and nothing warned us.")
