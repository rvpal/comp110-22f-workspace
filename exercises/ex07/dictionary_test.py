"""A program to test dictionary utility functions."""

__author__ = "730471791"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Tests an edge case for invert."""
    with pytest.raises(KeyError):
        xs: dict[str, str] = {
            "Hello": "Hi",
            "Hi": "Hello",
            "Goodbye": "Hello"
        }
        invert(xs)


def test_invert_edge_two() -> None:
    """Tests another edge case for invert."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_case_one() -> None:
    """Tests a use case for invert."""
    xs: dict[str, str] = {
        "Go away": "Hello",
        "Too bad": "I'm sad",
        "Too good": "I'm happy",
        "Bye then": "Biden"
    }
    assert invert(xs) == {
        "Hello": "Go away",
        "I'm sad": "Too bad",
        "I'm happy": "Too good",
        "Biden": "Bye then"
    }


def test_invert_case_two() -> None:
    """Tests another use case for invert."""
    xs: dict[str, str] = {"No": "Yes"}
    assert invert(xs) == {"Yes": "No"}


def test_favorite_color_edge() -> None:
    """Tests an edge case for favorite_color."""
    xs: dict[str, str] = {
        "Logan": "Blue",
        "Ranbir": "Blue",
        "Bob": "Yellow",
        "Timmy": "Yellow"
    }
    assert favorite_color(xs) == "Blue"


def test_favorite_color_edge_two() -> None:
    """Tests another edge case for favorite_color."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == "No color given."


def test_favorite_color_case_one() -> None:
    """Tests a use case for favorite_color."""
    xs: dict[str, str] = {
        "Logan": "Pink",
        "Ranbir": "Yellow",
        "Teach": "Yellow"
    }
    assert favorite_color(xs) == "Yellow"


def test_favorite_color_case_two() -> None:
    """Tests another use case for favorite color."""
    xs: dict[str, str] = {
        "Mark": "Blue",
        "Marc": "Black",
        "Marco": "Blue",
        "Marques": "Yellow",
        "Marck": "Blue"
    }
    assert favorite_color(xs) == "Blue"


def test_count_edge() -> None:
    """Tests an edge case for count."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_case_one() -> None:
    """Tests a use case for count."""
    xs: list[str] = ["Ranbir", "Ranbir", "Ranbir", "Logan", "Logan", "Bob", "Bob", "Bob", "Bob", "Bob"]
    assert count(xs) == {"Ranbir": 3, "Logan": 2, "Bob": 5}


def test_count_case_two() -> None:
    """Tests another edge case for sub."""
    xs: list[str] = {"Bob"}
    assert count(xs) == {"Bob": 1}
