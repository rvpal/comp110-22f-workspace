"""A document for dictionary utility functions."""

__author__ = "730471791"


def invert(values: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    for key in values:
        x: int = 0
        for lookup in values:
            if values[key] == values[lookup]:
                x += 1
        if x > 1:
            raise KeyError
    inverted: dict[str, str] = dict()
    for key in values:
        inverted[values[key]] = key
    return inverted


def favorite_color(color_index: dict[str, str]) -> str:
    """Given a dictionary of favorite colors, returns the most frequent color."""
    if color_index == {}:
        return "No color given."
    color_counts: dict[str, int] = dict()
    for key in color_index:
        x: int = 0
        for lookup in color_index:
            if color_index[key] == color_index[lookup]:
                x += 1
        color_counts[color_index[key]] = x
    y: str = ""
    z: int = 0
    for key in color_counts:
        if color_counts[key] > z:
            z = color_counts[key]
            y = key
    return y


def count(items: list[str]) -> dict[str, int]:
    """Counts the number of times a certain value appears in a list and returns a dictionary of items and their counts."""
    counts: dict[str, int] = dict()
    for i in items:
        number: int = 0
        for j in items:
            if i == j:
                number += 1
        if i not in counts:
            counts[i] = number
    return counts