"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730523706"


class Simpy:
    values: list[float]

    def __init__(self, given_values: list[float]):
        """Initializes the given values into a newly constucted Simpy object."""
        self.values = given_values

    def __str__(self) -> str:
        """Produces a string representation of the list of values."""
        return f"Stimpy({self.values})"

    def fill(self, float_value: float, n: int) -> None:
        """Fills in an empty Simpy object with a float that repeats n amount of times in the list."""
        fill_list: list[float] = []
        while n > 0:
            fill_list.append(float_value)
            n -= 1
        self.values = fill_list
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in an empty Simpy object with values that range from start to stop inceasing each value by step."""
        assert step != 0.0
        arange_list: list[float] = [start]
        while start != stop:
            start += step
            arange_list.append(start)
        arange_list.pop(len(arange_list) - 1)
        self.values = arange_list

    def sum(self) -> float:
        """Adds up all the elements of a Simpy values list into one float."""
        s: float = sum(self.values)
        return s
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add the elements of one Simpy object to the elements of another Simpy object or to the same float."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                new_simpy.values.append(self.values[i])
                new_simpy.values[i] += rhs.values[i]
                i += 1
            return new_simpy
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                new_simpy.values.append(self.values[i] + rhs)
                i += 1
            return new_simpy

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise the elements of one Simpy object to the power of the elements of another Simpy object accordingly or to the same float."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                new_simpy.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return new_simpy
        if isinstance(rhs, float):
            for x in self.values:
                new_simpy.values.append(x ** rhs)
            return new_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Crate a list of bools to see if the corresponding elements of two Simpy objects are equal or if a float is equal to the elements of a Simpy object."""
        bool_list: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
                i += 1
            return bool_list
        if isinstance(rhs, float):
            for x in self.values:
                if x == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Crate a list of bools to see if the corresponding elements of a Simpy objects is greater than another objects elements or if the elements of a Simpy object is greater than a float."""
        bool_list: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
                i += 1
            return bool_list
        if isinstance(rhs, float):
            for x in self.values:
                if x > rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Give the element at a certain index(rhs) of the Simpy object or a Simpy object of the elements that correspond with True values of a mask."""
        if isinstance(rhs, int):
            x: float = self.values[rhs]
            return x
        else:
            assert len(self.values) == len(rhs)
            subscript: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    subscript.values.append(self.values[i])
                i += 1
            return subscript