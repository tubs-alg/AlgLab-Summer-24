import itertools
from typing import List, Optional, Tuple

import networkx as nx
from pysat.solvers import Solver as SATSolver


class HamiltonianCycleModel:
    def __init__(self, graph: nx.Graph) -> None:
        self.graph = graph
        self.solver = SATSolver("Minicard")
        self.assumptions = []
        # TODO: Implement me!


    def solve(self) -> Optional[List[Tuple[int, int]]]:
        """
        Solves the Hamiltonian Cycle Problem. If a HC is found,
        its edges are returned as a list.
        If the graph has no HC, 'None' is returned.
        """
        # TODO: Implement me!
