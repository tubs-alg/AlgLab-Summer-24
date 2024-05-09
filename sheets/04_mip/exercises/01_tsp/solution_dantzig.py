"""
Implement the Dantzig-Fulkerson-Johnson formulation for the TSP.
"""

import typing

import gurobipy as gp
import networkx as nx


def _check_linear(model: gp.Model):
    # check if model has quadratic terms
    if model.NumQConstrs > 0:
        raise ValueError(
            "The model uses quadratic constraints (multiplying variables), which are less efficient. All exercises can be solved with linear constraints."
        )
    if model.NumQNZs > 0:
        raise ValueError(
            "The model uses quadratic terms (multiplying variables) in the objective, which are less efficient. All exercises can be solved with linear terms."
        )


class GurobiTspSolver:
    """
    IMPLEMENT ME!
    """

    def __init__(self, G: nx.Graph):
        """
        G is a weighted networkx graph, where the weight of an edge is stored in the
        "weight" attribute. It is strictly positive.
        """
        self.graph = G
        assert (
            G.number_of_edges() == G.number_of_nodes() * (G.number_of_nodes() - 1) / 2
        ), "Invalid graph"
        assert all(
            weight > 0 for _, _, weight in G.edges.data("weight", default=None)
        ), "Invalid graph"
        self._model = gp.Model()
        # TODO: Implement me!

    def get_lower_bound(self) -> float:
        """
        Return the current lower bound.
        """
        # TODO: Implement me!

    def get_solution(self) -> typing.Optional[nx.Graph]:
        """
        Return the current solution as a graph.
        """
        # TODO: Implement me!

    def get_objective(self) -> typing.Optional[float]:
        """
        Return the objective value of the last solution.
        """
        # TODO: Implement me!

    def solve(self, time_limit: float, opt_tol: float = 0.001) -> None:
        """
        Solve the model and return the objective value and the lower bound.
        """
        # Set parameters for the solver.
        self._model.Params.LogToConsole = 1
        self._model.Params.TimeLimit = time_limit
        self._model.Params.nonConvex = 0  # Throw an error if the model is non-convex
        self._model.Params.lazyConstraints = 1
        self._model.Params.MIPGap = (
            opt_tol  # https://www.gurobi.com/documentation/11.0/refman/mipgap.html
        )

        # ...
        # TODO: Implement me!
        _check_linear(self._model)
