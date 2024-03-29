"""
This module contains test cases for the MultiKnapsackSolver class in solver.py.
It tests the correctness of the solution returned by the solver for different instances.
"""

import json
import os

from _alglab_utils import CHECK, main, mandatory_testcase
from solution import Instance, MultiKnapsackSolver, Solution

INSTANCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instances")


def solve_instance_and_check_solution(filename: str, solution_score: int):
    instance = None
    with open(os.path.join(INSTANCE_DIR, filename)) as f:
        jdata = json.load(f)
        instance = Instance.from_dict(jdata)
    multi_knapsack = MultiKnapsackSolver(instance)
    solution = multi_knapsack.solve()

    CHECK(isinstance(solution, Solution), "The solution must be of type 'list'.")
    CHECK(solution is not None, "The solution is None!")
    CHECK(
        len(solution.knapsacks) == len(instance.capacities),
        f"The solution list must contain a list of items for each knapsack! The solution has {len(solution.knapsacks)} knapsacks, but the instance has {len(instance.capacities)} knapsacks.",
    )

    # count occurrences of each item
    for i, item in enumerate(instance.items):
        if occurrences := [
            j for j, knapsack in enumerate(solution) if item in knapsack
        ]:
            CHECK(
                len(occurrences) == 1,
                f"Item {i} occurs in more than one knapsack! Specifically, in knapsacks nr {occurrences}!",
            )

    # check capacity constraint and solution score
    score = 0
    for (j, knapsack), capacity in zip(
        enumerate(solution.knapsacks), instance.capacities
    ):
        used_capacity = sum(item.weight for item in knapsack)
        CHECK(
            used_capacity <= capacity,
            f"'Knapsack {j}'s capacity was exceeded! ({used_capacity}/{capacity})",
        )
        score += sum(item.value for item in knapsack)

    CHECK(
        score == solution_score,
        f"The score of the returned solution is not the optimal one! {score} != {solution_score}",
    )


@mandatory_testcase(max_runtime_s=30)
def instance_1():
    solve_instance_and_check_solution("10i_1k.json", 1270)


@mandatory_testcase(max_runtime_s=30)
def instance_2():
    solve_instance_and_check_solution("20i_5k.json", 88)


@mandatory_testcase(max_runtime_s=30)
def instance_3():
    solve_instance_and_check_solution("50i_5k.json", 416)


@mandatory_testcase(max_runtime_s=30)
def instance_4():
    solve_instance_and_check_solution("75i_6k.json", 557)


@mandatory_testcase(max_runtime_s=60)
def instance_5():
    solve_instance_and_check_solution("10000i_1k.json", 157452)


if __name__ == "__main__":
    main()
