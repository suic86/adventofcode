from collections import defaultdict
from typing import Mapping

Graph = Mapping[str, set[str]]


def parse_data(path: str = "input.data") -> Graph:
    data = defaultdict(set)
    with open(path) as fp:
        for line in map(str.strip, fp):
            n, a = line.split(": ")
            data[n] = data[n].union(set(a.split()))
    return data


def dfs(
    g: Graph,
    s: str,
    e: str,
    visited: set[str],
    current_path: list[str],
    simple_paths: set[tuple],
) -> None:
    if s in visited:
        return

    visited.add(s)
    current_path.append(s)

    if s == e:
        simple_paths.add(tuple(current_path))
        visited.remove(s)
        current_path.pop()
        return

    for n in g[s]:
        dfs(g, n, e, visited, current_path, simple_paths)

    current_path.pop()
    visited.remove(s)


def simple_paths(graph: Graph, start_node: str, end_node: str) -> set[tuple]:
    paths = set()
    current_path = []
    visited = set()
    dfs(graph, start_node, end_node, visited, current_path, paths)
    return paths


def solution_01(path: str = "input.data") -> int:
    graph = parse_data(path)
    ps = simple_paths(graph, "you", "out")
    return len(ps)


def solution_02(path: str = "input.data") -> int:
    graph = parse_data(path)
    ps = simple_paths(graph, "svr", "fft")
    return sum("dac" in path and "fft" in path for path in ps)


if __name__ == "__main__":
    from pprint import pprint

    pprint(solution_01("input.data"))
