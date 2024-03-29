from typing import List, Tuple

from pydantic import BaseModel, model_validator

"""
Location Types
"""


class Mine(BaseModel):
    id: int
    ore_per_hour: int  # How much ore this Mine can output per hour

    class Config:
        frozen = True


class Elevator(BaseModel):
    id: int

    class Config:
        frozen = True


"""
Rest of Types
"""


class Tunnel(BaseModel):
    location_a: int  # id of one end's location
    location_b: int  # id of other end's location
    throughput_per_hour: int  # How much ore can be transported via that tunnel per hour
    reinforcement_costs: float

    class Config:
        frozen = True

    @model_validator(mode="after")
    def _validate_tunnel(self):
        assert (
            self.location_a != self.location_b
        ), "The tunnel must connect two separate locations!"
        return self


class Map(BaseModel):
    elevator: Elevator
    mines: List[Mine]
    tunnels: List[Tunnel]

    class Config:
        frozen = True

    @model_validator(mode="after")
    def _validate_map(self):
        all_ids = [self.elevator.id] + [m.id for m in self.mines]
        assert len(all_ids) == len(set(all_ids)), "The location ids must be unique!"
        all_ids = set(all_ids)
        assert all(
            t.location_a in all_ids and t.location_b in all_ids for t in self.tunnels
        ), "The tunnels must connect locations with ids known to the instance!"
        return self


class Instance(BaseModel):
    map: Map
    budget: float

    class Config:
        frozen = True


class Solution(BaseModel):
    """
    This class represents the solution to an Instance.
    It holds a list representing the flow of goods.
    Please note that only edges with utilization > 0 are
    listed in the solution.

    The flow list consists of tuples with two entries each:
    1. *Directed* edge (tuple of ids, size two) between two locations,
        representing the direction of travel.
    2. The utilization of that directed edge / tunnel.
    """

    flow: List[Tuple[Tuple[int, int], int]]

    class Config:
        frozen = True

    @model_validator(mode="after")
    def _validate_utilization(self):
        assert all(
            util > 0 for (a, b), util in self.flow
        ), "The solution contains non-utilized edges!"
        return self
