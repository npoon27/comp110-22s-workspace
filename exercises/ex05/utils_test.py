"""TBD."""

__author__ = "730523706"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_odds() -> None:
    numbers: list[int] = [1, 5, 3]
    assert only_evens(numbers) == []


def test_only_evens_evens() -> None:
    numbers: list[int] = [2, 4, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_short() -> None:
    numbers: list[int] = [1, 2, 3]
    assert only_evens(numbers) == [2]


def test_only_evens_long() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(numbers) == [2, 4, 6, 8, 10]


def test_sub_usbale() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_concat_empty() -> None:
    l_one: list[int] = []
    l_two: list[int] = []
    assert concat(l_one, l_two) == []


def test_concat_list_one() -> None:
    l_one: list[int] = [1, 2, 3, 4, 5]
    l_two: list[int] = []
    assert concat(l_one, l_two) == [1, 2, 3, 4, 5]


def test_concat_list_two() -> None:
    l_one: list[int] = []
    l_two: list[int] = [10, 9, 8, 7, 6]
    assert concat(l_one, l_two) == [10, 9, 8, 7, 6]


def test_concat_both_lists() -> None:
    l_one: list[int] = [1, 2, 3, 4, 5]
    l_two: list[int] = [10, 9, 8, 7, 6]
    assert concat(l_one, l_two) == [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]


def test_concat_usable() -> None:
    l_one: list[int] = [30, 2, 32, 40, 18]
    l_two: list[int] = [90, 74, 12, 35, 62, 27]
    assert concat(l_one, l_two) == [30, 2, 32, 40, 18, 90, 74, 12, 35, 62, 27]