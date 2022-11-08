"""Magic methods."""

from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y arguments."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Represent object as a string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called.")
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Add two points."""
        print("__add__ was called.")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def scale(self, factor: float) -> Point:
        """Scale Point's attributes by factor."""
        return Point(self.x * factor, self.y * factor)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])