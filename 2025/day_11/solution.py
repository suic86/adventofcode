from collections import defaultdict
from graphlib import TopologicalSorter
from math import prod
from typing import Mapping

Node = str
Graph = Mapping[str, set[Node]]


def invert_graph(graph: Graph) -> Graph:
    inverted = defaultdict(set)
    for k, v in graph.items():
        for e in v:
            inverted[e].add(k)
    return inverted


def parse_data(path: str = "input.data") -> Graph:
    data = defaultdict(set)
    with open(path) as fp:
        for line in map(str.strip, fp):
            n, a = line.split(": ")
            data[n] = data[n].union(a.split())
    return data


def topological_order(graph: Graph) -> list[str]:
    return list(TopologicalSorter(invert_graph(graph)).static_order())


def count_path(
    graph: Graph,
    source: Node,
    destination: Node,
    intermediate: list[Node] | None = None,
) -> int:
    if intermediate is None:
        intermediate = []
    topo_order = topological_order(graph)
    order = sorted([source, destination] + intermediate, key=topo_order.index)

    if order[0] != source or order[-1] != destination:
        return 0

    def ways(source, destination):
        ways = defaultdict(int)
        ways[source] = 1
        for node in topo_order:
            for ng in graph[node]:
                ways[ng] += ways[node]
        return ways[destination]

    return prod(map(ways, order, order[1:]))


def solution_01(path: str = "input.data") -> int:
    graph = parse_data(path)
    return count_path(graph, "you", "out")


def solution_02(path: str = "input.data") -> int:
    graph = parse_data(path)
    return count_path(graph, "svr", "out", ["fft", "dac"])


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
