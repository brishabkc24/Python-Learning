"""Circle helpers for the shapes package."""

import math


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


def circle_perimeter(radius):
    """Return the perimeter (circumference) of a circle."""
    return 2 * math.pi * radius
