"""An exercise in list utility functions."""

Author = "730471791"


def all(int_list: list[int], comparison_integer: int) -> bool:
    """Determines whether all the ints in a list are the same as a given int."""
    i: int = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if comparison_integer != int_list[i]:
            return False
        i += 1
    return True


def max(integers: list[int]) -> int:
    """Returns the largest integer given a list of integers."""
    if len(integers) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum_value: int = integers[0]
    while i < len(integers) - 1:
        if maximum_value < integers[i + 1]:
            maximum_value = integers[i + 1]
        i += 1
    return maximum_value


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Returns true if each element in the first list is equal to the corresponding element in the second list."""
    if len(first_list) != len(second_list):
        return False
    i: int = 0
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            return False
        i += 1
    return True