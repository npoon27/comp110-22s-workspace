"""TBD."""

__author__ = "730523706"


def only_evens(numbers: list[int]) -> list[int]:
    """Creates a list of the even numbers out of the numbers in the given list."""
    evens: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens


def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Creates a sublist from start_index to end_index (not inclusive) of the given list."""
    sublist: list[int] = []
    i: int = 0
    if len(given_list) == 0 or start_index > len(given_list) or end_index <= 0:
        return sublist
    if start_index < 0:
        start_index = 0
    if end_index > len(given_list) - 1:
        end_index = len(given_list) - 1
    while i >= start_index and i < end_index - 1:
        number: int = given_list[i]
        sublist.append(number)
        i += 1
    return sublist


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Generates a list of numbers that contains the elements of list_one followed by list_two."""
    new_list: list[int] = []
    for x in list_one:
        new_list.append(x)
    for y in list_two:
        new_list.append(y)
    return new_list