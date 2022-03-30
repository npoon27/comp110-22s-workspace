"""Dictionary related utility functions."""

__author__ = "730523706"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Create a comlumn-based table with the first n given rows of data."""
    result: dict[str, list[str]] = {}
    if n >= len(column_table):
        return column_table
    for columns in column_table:
        row_values: list[str] = []
        i: int = 0
        while i < n:
            row_values.append(column_table[columns][i])
            i += 1
        result[columns] = row_values
    return result


def select(given_table: dict[str, list[str]], wanted_columns: list[str]) -> dict[str, list[str]]:
    """Create a new column-based table with a specific subset of columns from given table."""
    result: dict[str, list[str]] = {}
    for columns in wanted_columns:
        if columns in given_table:
            result[columns] = given_table[columns]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Crate a new column-based table by combining two column-based tables."""
    result: dict[str, list[str]] = {}
    for columns in table_one:
        result[columns] = table_one[columns]
    for columns in table_two:
        if columns in result:
            result[columns] += table_two[columns]
        else:
            result[columns] = table_two[columns]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts how many times a value appears in a list."""
    result: dict[str, int] = {}
    for x in values:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


def combine(dictionary: dict[str, int], keys: list[str]) -> int:
    """Combines values in a dictionary of the given list of keys."""
    result: int = 0
    for x in keys:
        if x in dictionary:
            result += dictionary[x]
    return result