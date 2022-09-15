"""Implement an example list utility function."""


def contains(needle: str, haystack: list) -> bool:
    """Determines if a list of values contains a string value."""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False

