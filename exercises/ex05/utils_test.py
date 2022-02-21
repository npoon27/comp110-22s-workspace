"""EX05 - `list` Utility Functions - Test to see if the fuctions from 'utils' are working properly."""

__author__ = "730523706"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test to see if the only_evens function works for an empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_odds() -> None:
    """Test to see if the only_evens function works for a list of only odds numbers."""
    numbers: list[int] = [1, 5, 3]
    assert only_evens(numbers) == []


def test_only_evens_evens() -> None:
    """Test to see if the only_evens function works for a list of only even numbers."""
    numbers: list[int] = [2, 4, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_short() -> None:
    """Test to see if the only_evens function works with a short list of both odd and even numbers."""
    numbers: list[int] = [1, 2, 3]
    assert only_evens(numbers) == [2]


def test_only_evens_long() -> None:
    """Test to see if the only_evens function works with a long list of both odd and even numbers."""
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(numbers) == [2, 4, 6, 8, 10]


def test_sub_usbale() -> None:
    """Test to see if the sub funtion works with a usable list and boundaries."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_negative_start() -> None:
    """Test to see if the sub funtion works with a usable list and a negative starting index."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -1, 3) == [10, 20, 30]


def test_sub_large_ending_index() -> None:
    """Test to see if the sub funtion works with a usable list and an ending index greater than the legnth of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 6) == [20, 30, 40]


def test_sub_usable_starting_from_zero() -> None:
    """Test to see if the sub funtion works with a usable list and boundaries starting from the 0 index."""
    a_list: list[int] = [1, 4, 67, 27, 99, 35, 73]
    assert sub(a_list, 0, 5) == [1, 4, 67, 27, 99]


def test_concat_empty() -> None:
    """Test to see if the concat funtion works with two empty lists."""
    l_one: list[int] = []
    l_two: list[int] = []
    assert concat(l_one, l_two) == []


def test_concat_list_one() -> None:
    """Test to see if the concat funtion works when list one has elements and list two is empty."""
    l_one: list[int] = [1, 2, 3, 4, 5]
    l_two: list[int] = []
    assert concat(l_one, l_two) == [1, 2, 3, 4, 5]


def test_concat_list_two() -> None:
    """Test to see if the concat funtion works when list two has elements and list one is empty."""
    l_one: list[int] = []
    l_two: list[int] = [10, 9, 8, 7, 6]
    assert concat(l_one, l_two) == [10, 9, 8, 7, 6]


def test_concat_both_lists() -> None:
    """Test to see if the concat funtion works when both lists have elements."""
    l_one: list[int] = [1, 2, 3, 4, 5]
    l_two: list[int] = [10, 9, 8, 7, 6]
    assert concat(l_one, l_two) == [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]


def test_concat_usable() -> None:
    """Test to see if the concat funtion works when both lists have elements and the lists are different sizes."""
    l_one: list[int] = [30, 2, 32, 40, 18]
    l_two: list[int] = [90, 74, 12, 35, 62, 27]
    assert concat(l_one, l_two) == [30, 2, 32, 40, 18, 90, 74, 12, 35, 62, 27]