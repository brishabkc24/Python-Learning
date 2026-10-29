"""
The shapes package: area and perimeter helpers for circles and rectangles.
Importing the package makes circle_area and rectangle_area available
directly as shapes.circle_area and shapes.rectangle_area.
"""

from shapes.circle import circle_area
from shapes.rectangle import rectangle_area

__all__ = ["circle_area", "rectangle_area"]
