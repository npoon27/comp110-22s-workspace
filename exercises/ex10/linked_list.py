"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730523706"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Return the data of a given Node stored at a given index."""
    i: int = 0
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if i == index:
            return head.data
            i += 1
        else:
            return value_at(head.next, index + 1)


def max(head: Optional[Node]) -> int:
    """Return the maximum data value in the given linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is None:
            return head.data
        else:
            if max(head.next) < head.data:
                return head.data
            else:
                return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Given a list of items return a linked list of Nodes with the same values in the same order."""
    i: int = 0
    if items == []:
        return None
    else:
        if i == len(items):
            return None
        else:
            linked_list = Node(items[0], None)
            linked_list.next = Node(items[1], None)
            linked_list.next.next = Node(items[2], None)
        return linked_list


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Return a new linked list of Nodes with each value being the values of the given linked list scaled by the given scaling factor."""
    if head is None:
        return None
    else:
        if head.next is None:
            return Node(head.data * factor, None)
        else:
            return Node(head.data * factor, scale(head.next, factor))