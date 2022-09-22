"""A document for more list utility functions."""

__author__ = "730471791"


def only_evens(int_list: list[int]) -> list[int]:
    """Returns a list of evens from a list of even and odds."""
    even_list: list[int] = list()
    for i in int_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns a combined list from two lists."""
    combined_list: list[int] = list()
    for i in list_one:
        combined_list.append(i)
    for i in list_two:
        combined_list.append(i)
    return combined_list


def sub(int_list: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of a list given indices."""
    subset: list[int] = list()
    if len(int_list) == 0 or start > len(int_list) or end <= 0:
        return subset
    if end > len(int_list):
        end = len(int_list)
    if start < 0:
        start = 0
    while start < end:
        subset.append(int_list[start])
        start += 1
    return subset