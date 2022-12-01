"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730471791"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """An empty linked-list should raise a ValueError."""
    with pytest.raises(ValueError):
        value_at(None, 0)


def test_value_at_range() -> None:
    """An index out of range should raise an IndexError."""
    with pytest.raises(IndexError):
        test: Node = Node(10, Node(20, Node(30, None)))
        value_at(test, 3)


def test_value_at_index() -> None:
    """Should return the data value at a given index."""
    test: Node = Node(10, Node(20, Node(30, None)))
    assert value_at(test, 2) == 30


def test_max_empty() -> None:
    """Should raise a ValueError if empty."""
    with pytest.raises(ValueError):
        max(None)


def test_max_ascending() -> None:
    """Should return max when node data is in ascending order."""
    assert max(Node(10, Node(20, Node(30, None)))) == 30


def test_max_descending() -> None:
    """Should return max when node data is in descending order."""
    assert max(Node(30, Node(20, Node(10, None)))) == 30


def test_max_jumble() -> None:
    """Should return max when node data is jumbled up."""
    assert max(Node(10, Node(30, Node(20, None)))) == 30


def test_max_multiple() -> None:
    """Should return max when there are duplicate values."""
    assert max(Node(10, Node(30, Node(30, None)))) == 30


def test_linkify_one() -> None:
    """Should do it right."""
    items: list[int] = [10, 20, 30, 40]
    assert str(linkify(items)) == "10 -> 20 -> 30 -> 40 -> None"


def test_linkify_two() -> None:
    """Should do it right."""
    items: list[int] = [30, 50]
    assert str(linkify(items)) == "30 -> 50 -> None"


def test_linkify_none() -> None:
    """Should do it right when list is empty."""
    items: list[int] = []
    assert linkify(items) is None


def test_scale_case() -> None:
    """Should scale by factor of 2."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"


def test_scale_edge() -> None:
    """Should return None."""
    assert str(scale(linkify([]), 2)) == "None"