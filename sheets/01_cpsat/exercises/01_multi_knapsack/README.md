# Exercise: Multi-Knapsack

![Symbol Image](./.assets/dalle-multiknapsack.png)

The multi-knapsack problem, which is like managing several knapsacks at once,
can be understood by thinking about it in terms of trucks and cargo. Imagine you
have a bunch of different trucks, each with a specific weight limit, and you
have a variety of different cargo items to load onto these trucks. These cargo
items not only have different weights but also carry a specific value associated
with them.

The goal is to figure out the best way to distribute the cargo among the trucks
so that you make the most efficient use of the available space in each truck
while maximizing the total value of the loaded cargo. In other words, you want
to optimize the arrangement to get the most valuable items into each truck
without exceeding the weight limit of any truck. Of course, it is not always
possible to pack all cargo items into the available trucks, so the problem also
involves deciding which items should be left behind. This problem can be
encountered in various scenarios where you have limited resources and items with
different sizes and values, such as warehouse inventory management, task
scheduling, or resource allocation, and the key challenge is to make the most
valuable use of the available space and resources.

## Tasks

### Mathematical Model

The mathematical model for the basic Knapsack problem can be written as follows:

$$\max \sum_{i \in I} v_i x_i$$

$$\text{s.t.} \sum_{i \in I} w_i x_i \leq C$$

$$\forall i\in I: x_i \in \{0,1\}$$

Here, we have the items $I$, each $i\in I$ having a value $v_i$ and a weight
$w_i$. The capacity of the knapsack is $C$. We create a variable $x_i$ for each
item $i$ that indicates whether the item is in the knapsack ($x_i=1$) or not
($x_i=0$).

1. Generalize it to the Multi-Knapsack problem. What are the variables? What is
   the objective? What are the constraints? Assume that $k$ is the number of
   Knapsacks $K$, and $C_i$ is the capacity of Knapsack $i\in K$.

_You can write your answer directly in this markdown file or refer to a separate
file here._

<!-- ADD YOUR ANSWER HERE -->

### Implementation of a Solver in CP-SAT

Next, we want to solve the problem using CP-SAT. This problem is actually
NP-hard, so the larger instances will take a few seconds to solve.

1. Check out `data_schema.py` to see how instance and solution data is
   structured.
2. Implement a solver in `solution.py` by extending the given class.
3. Do a quick test on a small instance by running `python3 verify.py instance_1`
   in the terminal.
4. Verify your final implementation by running `python3 verify.py` in the
   terminal. If a specific instance is failing, you can run it with all the
   output visible by running it as in the previous step.

## References

- [The Knapsack Problem on Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
- [pydantic](https://docs.pydantic.dev/latest/): Make yourself familiar with the
  abilities of `pydantic` to ensure valid data. While there are many similar
  libraries, including Python's own `dataclasses`, `pydantic` is a very popular
  choice for data validation and serialization in industry.
- [CP-SAT Primer](https://github.com/d-krupke/cpsat-primer): A primer by us for
  CP-SAT.
- [pre-commit](https://pre-commit.com/): We have set up a pre-commit
  configuration for you that you can use to quickly pretty up and check your
  code. You can install it by running `pip install pre-commit` and then
  `pre-commit run --all-files` to run it on all files in your repository.
- [Git LFS](https://git-lfs.com/): The instances are stored using Git LFS. You
  may need to install it as otherwise the instances will be empty and result in
  an error.
