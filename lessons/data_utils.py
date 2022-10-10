"""Some helpful utility functions for working with CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str,str]] = list()
    
    # Open the file. 
    file_handle = open(filename, "r", encoding="utf8")

    # Read the file. 
    csv_reader = DictReader(file_handle)

    # Read each row of the csv and append it as a dictionary to the result. 
    for row in csv_reader:
        result.append(row)

    # Close the file when we are done to free resources. 
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