"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730523706"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty linked list should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list will return the data value at the given index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_max_at_empty() -> None:
    """Max of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_at_non_empty() -> None:
    """Max of a non-empty list should return the maximum data value in the linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_at_empty() -> None:
    """Linkify of an empty list should return None."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_at_non_empty() -> None:
    """Linkify of a non-empty list should return a linked list of Nodes with the same value of the given list in the same order."""
    items: list[int] = [1, 2, 3]
    assert linkify(items) == "1 -> 2 -> 3 -> None"


def test_scale_at_empty() -> None:
    """Scale of an empty list should return None."""
    linked_list = Node(1, None)
    assert scale(linked_list, 1) is None


def test_scale_at_non_empty() -> None:
    """Scale of a non-empty list should return a new linked list when the value are the vaslues of the given linked list scaled by the given scalar factor."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert scale(linked_list, 1) == "1 -> 2 -> 3 -> None"