"""Dictionary related utility functions."""

__author__ = "730471791"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = list()
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns the all column values for a particular column."""
    result: list[str] = list()
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        values = column_values(row_table, column)
        result[column] = values
    return result


def head(columns: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a column based 'table' that only has the first N rows."""
    for key in columns:
        if N >= len(columns[key]):
            return columns
    result: dict[str, list[str]] = dict()
    for key in columns:
        N_list: list[str] = list()
        for i in range(N):
            N_list.append(columns[key][i])
        result[key] = N_list
    return result


def select(column_table: dict[str, list[str]], column_list: list[str]) -> dict[str, list[str]]:
    """Produce a column table with only a subset of the columns."""
    result: dict[str, list[str]] = dict()
    for i in column_list:
        result[i] = column_table[i]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column tables into one big column table."""
    result: dict[str, list[str]] = dict()
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        if key in result:
            for i in table_two[key]:
                result[key].append(i)
        else:
            result[key] = table_two[key]
    return result


def count(items: list[str]) -> dict[str, int]:
    """Counts the number of times a certain value appears in a list and returns a dictionary of items and their counts."""
    result: dict[str, int] = dict()
    for i in items:
        if i not in result:
            result[i] = 0
        result[i] += 1
    return result