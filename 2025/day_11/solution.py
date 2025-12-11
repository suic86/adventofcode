from collections import defaultdict
from typing import Mapping

Graph = Mapping[str, set[str]]


def parse_data(path: str = "input.data") -> Graph:
    data = defaultdict(set)
    with open(path) as fp:
        for line in map(str.strip, fp):
            n, a = line.split(": ")
            data[n] = data[n].union(set(a.split()))
            for e in a.split():
                data[e].add(n)
    return data


def dfs(
    node: str, dest: str, graph: Graph, visited: set[str], count: list[int]
) -> None:
    if node == dest:
        count[0] += 1
        return
    visited.add(node)
    for ng in graph[node]:
        if ng not in visited:
            dfs(ng, dest, graph, visited, count)

    visited.remove(node)


def solution_01(path: str = "input.data") -> int:
    graph = parse_data(path)
    count = [0]
    visited = set()
    dfs("you", "out", graph, visited, count)
    return count[0]


if __name__ == "__main__":
    from pprint import pprint

    pprint(solution_01("test.data"))
