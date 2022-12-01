"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730471791"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the Node at a given index."""
    if head is None:
        raise ValueError("value_at cannot be called with None")
    if index == 0:
        return head.data
    elif isinstance(head.next, Node):
        return value_at(head.next, index - 1)
    else:
        raise IndexError("Index is out of bounds on the list.")


def max(head: Node) -> int:
    """Returns the maximum data value in a linked-list."""
    if head is None:
        raise ValueError("max cannot be called with None")
    if head.next is None:
        return head.data
    if head.data > max(head.next):
        return head.data
    else:
        return max(head.next)


def linkify(values: list[int]) -> Optional[Node]:
    """Uses values of a list for data values in a linked list."""
    if len(values) > 0:
        return Node(values[0], linkify(values[1:]))
    else:
        return None


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new linked list with the data values scaled up by a factor."""
    if head is None:
        return None
    return Node(head.data * factor, scale(head.next, factor))
