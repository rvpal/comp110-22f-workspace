"""An example of vectorized operatoins via operator overloading."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        """Initializes the StrArray object."""
        self.items = items

    def __repr__(self) -> str:
        """String representation of StrArray."""
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> str:
        """Concatonates the values in a StrArray with another string."""
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for i in self.items:
                result.items.append(i + rhs)
        else:
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(b)
print(a + "!")
print(a + b)
print(b + ", " + a + "!!!")
# Line 34 is equivalent to:
print(b.__add__(", ").__add__(a).__add__("!!!"))