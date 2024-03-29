# Exercise: Bottleneck TSP using a SAT-solver

![Symbol Image](./.figures/dalle-btsp.png)

Imagine planning a road trip where you visit a different city each day. Instead
of worrying about the total distance or time of the entire trip, your main
concern is the longest travel time between any two consecutive cities. In other
words, you want to minimize the longest day of driving so that no single day is
too exhausting.

Formally, this scenario is modeled as the Bottleneck Traveling Salesman Problem
(BTSP). Here, you have a weighted graph where the vertices represent cities and
the edges represent roads connecting these cities, each with an associated
travel time or 'weight'. The objective is to find a tour that visits every city
exactly once and returns to the starting city, where the maximum weight of any
edge in the tour (i.e., the longest travel time between any two cities) is
minimized.

An interesting aspect of the BTSP, particularly when optimizing it via
techniques like SAT (Satisfiability Testing), is the limited domain of objective
values. Since the objective value is determined by the weight of the heaviest
edge in the tour, there are at most $n^2$ different objective values in a graph
with $n$ vertices. This is a significant advantage over the classical Traveling
Salesman Problem (TSP), where the objective is to minimize the total length of
the tour, resulting in a much larger range of possible objective values.

This problem is especially relevant in situations where the worst-case scenario
(i.e., the longest leg of the journey) is more critical than the total cost or
length. It's a practical approach in logistics, scheduling, and network design,
where managing the most challenging or expensive part of a route is more
important than minimizing the overall effort or cost.

## Tasks

### Task 1: Hamiltonian Cycle

1. Implement a solver to determine if a given graph contains a Hamiltonian
   cycle. The implementation should be in the file `solution_hamiltonian.py`.
2. Test your implementation by executing the script
   `python3 ./verify_hamiltonian.py`.

**Requirements**: Your solution must employ the Dantzig-Fulkerson-Johnson
formulation for efficiency. This approach requires ensuring that every vertex
subset has at least two exiting edges. Given the impracticality of enumerating
all vertex subsets, your implementation should adopt an iterative refinement
strategy. Start without subset constraints and introduce them progressively for
disconnected components in your solution. Leverage the `nx.connected_components`
function from the `networkx` library to identify connected components within a
graph. Utilize cardinality constraints to mandate the exit of two edges from
each component. This iterative process is expected to converge to a feasible
solution promptly.

## Task 2: Bottleneck Traveling Salesman Problem (BTSP) Solver

1. Develop a solver for obtaining exact solutions to the Bottleneck Traveling
   Salesman Problem (BTSP). The implementation should be in file
   `solution_btsp.py`. The weight of a networkx edge can be queried by
   `graph.edges[e]["weight"]`. By searching for the smallest $t$ with
   $G=(V, \{v,w \mid v,w\in V, weight(v,w)\leq t\})$ is hamiltonian, you can
   find the optimal solution to the BTSP via a binary search on the sorted edge
   weights.
2. Assess your implementation's correctness by running
   `python3 ./verify_btsp.py`.

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
- [Bottleneck Traveling Salesman Problem](https://en.wikipedia.org/wiki/Bottleneck_traveling_salesman_problem)
- [Git LFS](https://git-lfs.com/): The instances are stored using Git LFS. You
  may need to install it as otherwise the instances will be empty and result in
  an error.
