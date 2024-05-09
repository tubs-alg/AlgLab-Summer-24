import os
import pathlib

import networkx as nx
from _alglab_utils import CHECK, main, mandatory_testcase
from data_schema import Instance
from solution import MiningRoutingSolver

CWD = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
EPS = 0.001


def solve_hc_instance(filepath: str, objective_sol: int):
    with open(filepath) as f:
        instance: Instance = Instance.model_validate_json(f.read())
        mine_lookup = {mine.id: mine for mine in instance.map.mines}

    solver = MiningRoutingSolver(instance)
    solution = solver.solve()
    CHECK(solution is not None, "The returned solution must not be 'None'!")
    solution = solution.flow
    CHECK(len(solution) > 0, "The solution flow must not be empty!")

    flow_graph = nx.DiGraph()

    def find_road(from_: int, to_: int):
        tunnel_set: set = {from_, to_}
        matching_tunnels = [
            tunnel
            for tunnel in instance.map.tunnels
            if {tunnel.location_a, tunnel.location_b} == tunnel_set
        ]
        CHECK(
            len(matching_tunnels) == 1,
            "The solution contains a tunnel that is not part of the given instance!",
        )
        return matching_tunnels[0]

    budget_used = 0.0
    for (u, v), util in solution:
        CHECK(
            isinstance(util, int),
            f"The utilization of a tunnel must be an integer! Current type: {type(util)} ({util})",
        )
        for i in (u, v):
            CHECK(
                i == instance.map.elevator.id or u in mine_lookup.keys(),
                f"Location id '{i}' from solution is not part of the given instance!",
            )
        road = find_road(u, v)
        budget_used += road.reinforcement_costs
        capacity = road.throughput_per_hour
        CHECK(
            util > 0,
            f"Tunnels in the solution must only have positive utilization! However, there is a tunnel with utilization {util}!",
        )
        CHECK(
            util <= capacity,
            f"The capacity of a tunnel was exceeded! (utilization: {util}, capacity: {capacity})",
        )
        flow_graph.add_edge(u, v, capacity=capacity, utilization=util)
    CHECK(
        budget_used <= instance.budget + EPS,
        f"The instance budget was exceeded! (even with granted rounding inaccuracy) {budget_used} > {instance.budget}",
    )
    CHECK(
        instance.map.elevator.id in flow_graph.nodes,
        "The elevator is not connected!",
    )
    CHECK(
        flow_graph.to_undirected().number_of_edges() == flow_graph.number_of_edges(),
        "Roads can only be used in one direction at once!",
    )

    for loc in flow_graph.nodes:
        in_sum = sum(
            d["utilization"] for u, v, d in flow_graph.in_edges(loc, data=True)
        )
        out_sum = sum(
            d["utilization"] for u, v, d in flow_graph.out_edges(loc, data=True)
        )
        if loc == instance.map.elevator.id:
            CHECK(
                out_sum == 0,
                f"No resources must leave the elevator location! Current: {out_sum}",
            )
            CHECK(
                in_sum == objective_sol,
                f"The objective is not optimal! {in_sum} != {objective_sol}",
            )
        else:
            CHECK(
                out_sum <= in_sum + mine_lookup[loc].ore_per_hour,
                f"There is more ore leaving mine {loc} than entering + produced!",
            )


@mandatory_testcase(max_runtime_s=30)
def instance_10():
    solve_hc_instance(CWD / "./instances/instance_10.json", 46)


@mandatory_testcase(max_runtime_s=30)
def instance_20():
    solve_hc_instance(CWD / "./instances/instance_20.json", 83)


@mandatory_testcase(max_runtime_s=30)
def instance_50():
    solve_hc_instance(CWD / "./instances/instance_50.json", 226)


@mandatory_testcase(max_runtime_s=30)
def instance_200():
    solve_hc_instance(CWD / "./instances/instance_200.json", 892)


@mandatory_testcase(max_runtime_s=60)
def instance_500():
    solve_hc_instance(CWD / "./instances/instance_500.json", 2193)


if __name__ == "__main__":
    main()
