from collections import defaultdict
from graphlib import TopologicalSorter
from typing import Mapping

Graph = Mapping[str, set[str]]


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


def topological_order(graph: Graph) -> tuple:
    return tuple(TopologicalSorter(invert_graph(graph)).static_order())


def count_path(graph: Graph, topo_order, source, destination) -> int:
    ways = defaultdict(int)
    ways[source] = 1
    for node in topo_order:
        for ng in graph[node]:
            ways[ng] += ways[node]
    return ways[destination]


def solution_01(path: str = "input.data") -> int:
    graph = parse_data(path)
    return count_path(graph, topological_order(graph), "you", "out")


def solution_02(path: str = "input.data") -> int:
    graph = parse_data(path)
    topo_order = topological_order(graph)
    sf = count_path(graph, topo_order, "svr", "fft")
    fd = count_path(graph, topo_order, "fft", "dac")
    do = count_path(graph, topo_order, "dac", "out")

    res = sf * fd * do
    return res


if __name__ == "__main__":
    from pprint import pprint

    # pprint(solution_02("test_02.data"))
    pprint(solution_01("input.data"))
