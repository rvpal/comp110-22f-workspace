"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730471791"


class Simpy:
    values: list[float]

    def __init__(self, values: list):
        """Constructor function for Simpy class."""
        self.values = values

    def __repr__(self) -> str:
        """Returns a string representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, fill: float, repeat: int) -> None:
        """Fills in the values attribute with a repeated amount of floats."""
        self.values = []
        for i in range(repeat):
            self.values.append(fill)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Like the built in range function, but for floats."""
        assert step != 0.0
        self.values = []
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        elif start > stop:
            assert step < 0.0
            while start > stop:
                self.values.append(start)
                start += step