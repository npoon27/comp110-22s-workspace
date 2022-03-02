"""EX06 - Dictionary Functions - Testing the functions from 'dictionary.py' to make sure they work correctly."""

__author__ = "730523706"

from exercises.ex06.dictionary import count, invert, favorite_color


def test_invert_empty() -> None:
    """Test to see if the invert function works for an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_single() -> None:
    """Test to see if the invert function works for a single key and value dictionary."""
    test_dict: dict[str, str] = {'dog': 'food'}
    assert invert(test_dict) == {'food': 'dog'}


def test_invert_long_dict() -> None:
    """Test to see if the invert function works for a long usable dictionary."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None:
    """Test to see if the favorite_color function works with an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_single() -> None:
    """Test to see if the favorite_color function works with a single pair dictionary."""
    test_dict: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color_usable() -> None:
    """Test to see if the favorite_color function works with a full dictionary."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_same_frequency() -> None:
    """Test to see if the favorite_color function works with colors showing up with the same frequency."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Nick": "yellow", "Kris": "blue"}
    assert favorite_color(test_dict) == "yellow"


def test_count_empty() -> None:
    """Test to see if the count function works for an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_single_words() -> None:
    """Test to see if the count function works for a list of words that show up once."""
    test_list: list[str] = ["go", "tar", "heels"]
    assert count(test_list) == {"go": 1, "tar": 1, "heels": 1}


def test_count_usable() -> None:
    """Test to see if the count function works for a full list of usable words that show up once or more than."""
    test_list: list[str] = ["go", "tar", "heels", "go", "heels", "go"]
    assert count(test_list) == {"go": 3, "tar": 1, "heels": 2}