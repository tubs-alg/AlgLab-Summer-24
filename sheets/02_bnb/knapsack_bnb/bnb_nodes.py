import typing
from enum import Enum
from typing import Optional

from .instance import Instance
from .relaxation import BranchingDecisions, FractionalSolution, RelaxationSolver


class NodeStatus(Enum):
    """
    Status of a node in the search tree.
    """

    FEASIBLE = "Feasible"
    INFEASIBLE = "Infeasible"
    ENQUEUED = "Enqueued"
    PRUNED = "Pruned"
    BRANCHED = "Branched"
    UNKNOWN = "Unknown"


class BnBNode:
    """
    Represent a node relaxed_soluattributes  with in the branch-and-bound search tree.
    """

    def __init__(
        self,
        relaxed_solution: FractionalSolution,
        branching_decisions: BranchingDecisions,
        depth: int,
        node_id: int,
        parent_id: Optional[int] = None,
    ) -> None:
        self.relaxed_solution = relaxed_solution
        self.branching_decisions = branching_decisions
        self.depth = depth
        self.node_id = node_id
        self.parent_id = parent_id
        self.status: NodeStatus = NodeStatus.UNKNOWN

    def __lt__(self, other: "BnBNode") -> bool:
        """
        Compare two nodes based on their node IDs.
        """
        return self.node_id < other.node_id

    def __eq__(self, __value: object) -> bool:
        """
        Check if this node is equal to another object.
        """
        return isinstance(__value, BnBNode) and self.node_id == __value.node_id


class NodeFactory:
    """
    Create nodes for the search tree.
    """

    def __init__(
        self,
        instance: Instance,
        relaxation: RelaxationSolver,
        on_new_node: typing.Callable[[BnBNode], None],
    ) -> None:
        self._node_id_counter = 0
        self.instance = instance
        self.relaxation = relaxation
        self.on_new_node = on_new_node

    def create_root(self) -> BnBNode:
        """
        Create and return the root node of the search tree
        """
        root = BnBNode(
            self.relaxation.solve(
                self.instance, BranchingDecisions(len(self.instance.items))
            ),
            BranchingDecisions(len(self.instance.items)),
            0,
            self._node_id_counter,
        )
        self._node_id_counter += 1
        self.on_new_node(root)
        return root

    def create_child(
        self, parent: BnBNode, branching_decisions: BranchingDecisions
    ) -> BnBNode:
        """
        Create a child node for each decision branch of the given parent node.
        """
        child = BnBNode(
            self.relaxation.solve(self.instance, branching_decisions),
            branching_decisions,
            parent.depth + 1,
            self._node_id_counter,
            parent_id=parent.node_id,
        )
        self._node_id_counter += 1
        self.on_new_node(child)
        return child

    def num_nodes(self) -> int:
        """
        Number of nodes created so far.
        """
        return self._node_id_counter
