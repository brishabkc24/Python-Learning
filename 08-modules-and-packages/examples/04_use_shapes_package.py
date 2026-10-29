"""
Use the shapes package in the folder next to this file: import the
package, a module inside it, and single functions from a module.

Run from this folder: python 04_use_shapes_package.py
"""

import shapes
from shapes import circle
from shapes.rectangle import rectangle_perimeter

# Names that __init__.py pulled up to package level.
print("circle area (r=2):", round(shapes.circle_area(2), 2))
print("rectangle area (3x4):", shapes.rectangle_area(3, 4))

# A module imported from the package.
print("circle perimeter (r=2):", round(circle.circle_perimeter(2), 2))

# A single function imported from a module inside the package.
print("rectangle perimeter (3x4):", rectangle_perimeter(3, 4))

# The full dotted path always works too.
import shapes.rectangle
print("via full path:", shapes.rectangle.rectangle_area(5, 6))

print()
print("package name:", shapes.__name__)
print("public names:", shapes.__all__)
print("modules loaded from the package:", sorted(name for name in dir(shapes) if name in ("circle", "rectangle")))

# A small table built with the package.
print()
print("radius  area")
for radius in [1, 2, 3]:
    print(str(radius).ljust(7), round(shapes.circle_area(radius), 2))
