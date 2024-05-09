import gurobipy as gp
import networkx as nx  # noqa: F401
from data_schema import Instance, Solution
from gurobipy import GRB  # noqa: F401



class MiningRoutingSolver:
    def __init__(self, instance: Instance) -> None:
        self.map = instance.map
        self.budget = instance.budget
        self.model = gp.Model()
        self.model.Params.nonConvex = 0  # Throw an error if the model is non-convex
        # TODO: Implement me!

    def solve(self) -> Solution:
        """
        Calculate the optimal solution to the problem.
        Returns the "flow" as a list of tuples, each tuple with two entries:
            - The *directed* edge tuple. Both entries in the edge should be ints, representing the ids of locations.
            - The throughput/utilization of the edge, in goods per hour
        """
        # TODO: implement me!

        # run this function to check if your model is really linear.
        # otherwise, you will likely run into performance issues.
        _check_linear(self.model)
