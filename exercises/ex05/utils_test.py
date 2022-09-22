"""A document to test more list utility functions."""

__author__ = "730471791"


from utils import only_evens, concat, sub


def test_only_evens_edge() -> None:
    """Tests an edge case for only_evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_case_one() -> None:
    """Tests a use case for only_evens."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_case_two() -> None:
    """Tests another use case for only_evens."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_case_three() -> None:
    """Tests a third use case for only_evens."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_concat_edge() -> None:
    """Tests an edge case for concat."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_case_one() -> None:
    """Tests a use case for concat."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_case_two() -> None:
    """Tests another use case for concat."""
    xs: list[int] = [-10, 3, 4, 2]
    ys: list[int] = [-5, 1, 5, 9]
    assert concat(xs, ys) == [-10, 3, 4, 2, -5, 1, 5, 9]


def test_sub_edge() -> None:
    """Tests an edge case for sub."""
    xs: list[int] = []
    start: int = 100
    end: int = -5
    assert sub(xs, start, end) == []


def test_sub_edge_two() -> None:
    """Tests another edge case for sub."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    start: int = 100
    end: int = -5
    assert sub(xs, start, end) == []


def test_sub_edge_three() -> None:
    """Tests a third edge case for sub."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    start: int = -1
    end: int = 100
    assert sub(xs, start, end) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_sub_case_one() -> None:
    """Tests a use case for sub."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start: int = 2
    end: int = 4
    assert sub(xs, start, end) == [3, 4]


def test_sub_case_two() -> None:
    """Tests another use case for sub."""
    xs: list[int] = [1, 4, 6, 10]
    start: int = 1
    end: int = 7
    assert sub(xs, start, end) == [4, 6, 10]
