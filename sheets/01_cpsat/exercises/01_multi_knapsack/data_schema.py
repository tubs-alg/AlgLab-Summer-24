from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, model_validator


class Item(BaseModel):
    """
    A class representing an item with a value and weight.
    """

    value: int
    weight: int
    id: UUID = Field(default_factory=uuid4, alias="_id")

    class Config:
        frozen = True


class Instance(BaseModel):
    """
    A class representing an instance of the multi-knapsack problem.
    """

    items: List[Item] = Field("A list of the items to be packed into the knapsacks.")
    capacities: List[int] = Field(
        "A list of the knapsack capacities. The first capacity is for the first knapsack, the second capacity for the second knapsack, and so on. It implicitly defines the number of knapsacks."
    )

    @classmethod
    def from_dict(cls, data: dict) -> "Instance":
        capacities = [t["capacity"] for t in data["knapsacks"]]
        assert data["num_knapsacks"] == len(capacities), "The instance is invalid!"
        items = [Item(**t) for t in data["items"]]
        assert data["num_items"] == len(items)
        return cls(items=items, capacities=capacities)


class Solution(BaseModel):
    """
    A class representing a solution to the multi-knapsack problem.
    """

    knapsacks: List[List[Item]] = Field(
        description="A list of lists of items, representing the items in each knapsack. The first list represents the items in the first knapsack, the second list the items in the second knapsack, and so on."
    )

    # Some basic model validation to make sure there are no trivial errors.
    @model_validator(mode="after")
    def _items_only_in_one_knapsack(self):
        """
        Ensure that each item is only in one knapsack.
        """
        already_packed_items = set()
        for knapsack in self.knapsacks:
            for item in knapsack:
                assert (
                    item.id not in already_packed_items
                ), f"Item {item.id} is in more than one knapsack!"
                already_packed_items.add(item.id)
        return self
