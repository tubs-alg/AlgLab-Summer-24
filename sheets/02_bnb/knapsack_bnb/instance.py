import typing

from pydantic import BaseModel


class Item(BaseModel):
    """
    Represents an item with a weight and a value for the knapsack problem.
    """

    weight: int
    value: int


class Instance(BaseModel):
    """
    Represents an instance with a list of items and capacity of the knapsack problem.
    """

    items: typing.List[Item]
    capacity: int
