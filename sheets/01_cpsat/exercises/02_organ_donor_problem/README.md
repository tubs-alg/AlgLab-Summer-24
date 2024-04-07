# Exercise: Maximizing the Number of Crossover Transplantations

![Symbol Image](./.assets/dalle-transpl.png)

Organ transplantation is a critical, life-saving medical intervention for
patients facing end-stage organ failure. However, one of the most challenging
aspects is finding compatible donors. In many cases, family members or friends
are willing to donate but are incompatible with the intended recipient, making
the direct transplantation impossible. Traditional waiting lists can be long and
come with an increasing risk of the recipient's condition worsening, or even
fatal outcomes.

Crossover or paired transplantation programs offer an innovative solution to
this urgent problem. Crossover transplantations involve pairs of patients and
their willing but incompatible donor(s). Each pair of patient and donor is
offered a "deal": If the donor donates an organ to a different, compatible
patient, their associated patient will receive a donation from another,
compatible donor. By considering multiple donor-recipient pairs, these programs
create an opportunity for cross-matching, thereby maximizing the number of
compatible and successful transplantations. Not only does this expand the donor
pool, but it also significantly reduces the waiting time for recipients. Given
the life-and-death nature of organ transplantation, optimizing this process has
immediate and profound implications: it can save lives, improve the quality of
life for recipients, and make efficient use of available medical resources.

In the following, a _donor-recipient pair_ refers to a pair of related patient
and donor, who are incompatible. Thus, the donor is willing to donate their
organ to another patient in exchange for a compatible organ for their family
member or friend. Please note that multiple donors can register for the same
patient, so there might exist multiple pairs for each recipient. Still, only one
of the associated donors will make a donation in those cases.

**Objective:** Given a set of donor-recipient pairs with certain compatibility
parameters, your task is to maximize the number of successful crossover
transplantations.

**Input:**

- A list of $n$ donor-recipient pairs, labeled
  $(d_1, r_1), (d_2, r_2), \ldots, (d_n, r_n)$. The set of donors is
  $D = \{d_1, d_2, \ldots, d_n\}$ and the set of recipients is
  $R = \{r_1, r_2, \ldots, r_n\}$. Recipients can occur more than once, e.g.,
  $r_1=r_3$, but donors will only appear once, i.e.,
  $\forall i\not= j: d_i\not=d_j$.
- A compatibility function $f: D\times R \rightarrow \mathbb{B}$ where
  $f(d_i, r_j)$ is 1 if $d_i\in D$ is compatible with $r_j\in R$ and 0
  otherwise.

**Constraints:**

1. A donor can only donate once.
2. A recipient can only receive one organ.
3. A donor is only willing to donate if their recipient receives an organ. A
   family member of a patient is willing to donate only if their family member
   receives another organ in exchange (the donor of any another pair donates it
   to them).

## Tasks

### Mathematical Model

The first step should always be to create a concrete mathematical model that
leaves no room for interpretation. Try to model it already as close to the
capabilities of CP-SAT as possible. This means that you should try to focus on
Boolean variables and linear constraints.

1. Provide a mathematical model for the problem. What are the variables? What is
   the objective? What are the constraints?

_You can write your answer directly in this markdown file or refer to a separate
file here._

<!-- ADD YOUR ANSWER HERE -->

### Implementation of a Solver in CP-SAT

2. Implement a solver for the problem using CP-SAT. You find a small code
   framework under `solution_basic.py` that you have to extend. The data is
   given to you via a database. Verify your solver by running the tests with
   `python3 verify_basic.py`. There's also a simple solution visualizer, which
   might help you debug your model. Run it using `python3 visualization.py`.

3. The surgeries usually have to be performed in parallel such that no donor can
   change their mind. As there are usually only a few ORs, there is a limit on
   how many surgeries can be performed at the same time. To incorporate this
   into your model, you need to restrict the size of each exchange cycle.
   Implement a new solver in `solver_small_cycles.py` that allows cycles of size *at most* 3 (i.e., 3 transplantations) and verify it using
   `python3 verify_small_cycles.py`.

## References

- [Mathematical Modelling](https://www.gurobi.com/resources/math-programming-modeling-basics/):
  A crash-course in mathematical modelling.
- [pydantic](https://docs.pydantic.dev/latest/): Make yourself familiar with the
  abilities of `pydantic` to ensure valid data. While there are many similar
  libraries, including Python's own `dataclasses`, `pydantic` is a very popular
  choice for data validation and serialization in industry.
- You may find useful algorithms for preprocessing in
  [networkx](https://networkx.org/documentation/stable/reference/algorithms/index.html).
- [CP-SAT Primer](https://github.com/d-krupke/cpsat-primer): A primer by us for
  CP-SAT.
- [pre-commit](https://pre-commit.com/): We have set up a pre-commit
  configuration for you that you can use to quickly pretty up and check your
  code. You can install it by running `pip install pre-commit` and then
  `pre-commit run --all-files` to run it on all files in your repository.
- [Git LFS](https://git-lfs.com/): The instances are stored using Git LFS. You
  may need to install it as otherwise the instances will be empty and result in
  an error.
