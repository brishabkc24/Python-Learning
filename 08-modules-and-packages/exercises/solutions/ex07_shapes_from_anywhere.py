"""Exercise 7: add the examples folder to sys.path so the shapes package can be imported from here."""

import sys
from pathlib import Path

EXAMPLES_DIR = Path(__file__).resolve().parents[2] / "examples"
sys.path.append(str(EXAMPLES_DIR))

import shapes

print("Added to sys.path:", EXAMPLES_DIR.name)
print("Circle area, radius 5:", round(shapes.circle_area(5), 2))
print("Rectangle area, 7 x 3:", shapes.rectangle_area(7, 3))
