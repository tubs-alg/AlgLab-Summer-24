# Exercise: k-centers using a SAT-solver

### 01. Vertex K-Centers

![Vertex K-Centers](./.figures/dalle-kcentre.png)

Formally, the
[Vertex K-Center Problem](https://en.wikipedia.org/wiki/Vertex_k-center_problem)
involves a weighted undirected graph $G=(V,E)$ where $V$ represents vertices (or
nodes) and $E$ represents edges (or connections between nodes). Each edge
$vw=wv \in E$ has a metric weight $d_{vw}$, which is the distance or cost
associated with that connection.

To visualize this in a practical scenario, think of a network of cities
(vertices) connected by roads (edges). Each road has a specific travel distance
or cost (these are the metric weights $d_{vw}$). In this graph, every two cities
are either directly connected via a street/edge, or there exists a (shortest)
path via some other cities. In these cases, we define $d_{vw}$ to be the length
of the shortest path $SP(v,w)$.

Given a positive integer $k$, the challenge is to select a subset of cities
$C \subseteq V$ such that the number of cities in $C$ does not exceed $k$ (i.e.,
$|C| \leq k$). The aim is to place service centers in these selected cities in a
way that minimizes the maximum distance any city is from its nearest service
center.

In simpler terms, your goal is to ensure that each city is as close as possible
to a service center, given that you can only build a limited number $k$ of these
centers. The optimal solution is the set of cities where these centers should be
built so that the farthest any city is from a center is as short as possible.

This problem is a classic example in the field of mathematical optimization and
has practical applications in areas like urban planning and logistics.

## Tasks

### Task 1: Mathematical Model

You should start by formulating the problem mathematically before you start
coding.

1. Model the problem of deciding if there is a solution for a given parameter
   $k$ with objective value at most $c$ as a SAT problem (with cardinality
   constraints). Assume that $d_{vw}$ is the travel distance between $v,w$.

_You can write your answer directly in this markdown file or refer to a separate
file here._

<!-- ADD YOUR ANSWER HERE -->

### Task 2: Implementation of a Solver using a card-SAT-solver

The input of the solvers will be weighted networkx graphs.

1. Implement a heuristic which you could use to get an upper bound on the
   objective value.
2. Implement a solver that can give you a feasible solution for some upper bound
   $l$, i.e., a set $C\subseteq V, |C|\leq k$ for which every city $v\in V$ has
   a center $c\in C$ within distance $d_{vc}\leq l$, or prove that no such set
   $C$ exists.
3. Implement an exact solver for the problem by efficiently searching for the
   smallest feasible $l$ and returning the corresponding $C$. You find a code
   structure in `solution.py`. You can verify your implementation by running
   `python3 verify.py` in the terminal.

*Hint: You may find [`shortest_path_length`](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html#networkx.algorithms.shortest_paths.generic.shortest_path_length) useful.*

## References

- [A peek inside SAT Solvers - Jon Smock](https://www.youtube.com/watch?v=d76e4hV1iJY):
  The most important aspects of SAT solvers in half an hour.
- [networkx](https://networkx.org/documentation/stable/reference/algorithms/index.html):
  The inputs of the solvers will be weighted networkx graphs.
- [pysat](https://pysathq.github.io/): The SAT solver library we will use.
- [Propositional Calculus](https://en.wikipedia.org/wiki/Propositional_calculus):
  You should already know propositional calculus from your studies in logic.
- [SAT Solvers](https://en.wikipedia.org/wiki/SAT_solver): Wikipedia article on
  SAT solvers.
- [2hr Lecture on SAT Solving by Armin Biere](https://www.youtube.com/watch?v=Emhg0uZnbNg):
  For those who want to dive deeper into the topic.
- [4.5hr Lecture on SAT Solving by Armin Biere](https://www.youtube.com/watch?v=II2RhzwYszQ&list=PLgKuh-lKre12GSaYimhmuTsD-l41VsGQI&index=10):
  For those who want to dive even deeper into the topic.
- [History of SAT Solving - Armin Biere](https://www.youtube.com/live/DU44Y9Pt504?si=D4686hn6mi1E1Ml8):
  For those, who are interested in the historical development of SAT solvers. As
  computer science is a very fast moving field, it is always good to know how
  young the field of SAT solving actually is.
- [Facility Location Problem](https://en.wikipedia.org/wiki/Optimal_facility_location)
- [Git LFS](https://git-lfs.com/): The instances are stored using Git LFS. You
  may need to install it as otherwise the instances will be empty and result in
  an error.
