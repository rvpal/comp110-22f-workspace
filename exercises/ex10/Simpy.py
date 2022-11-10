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

    def sum(self) -> float:
        """Adds up the items in the values attribute."""
        result: float = 0.0
        for i in self.values:
            result += i
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the add operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the equality operator."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the greater than operator."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads the subscription operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            assert len(rhs) == len(self.values)
            result: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result