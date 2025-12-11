from collections import defaultdict, deque
from typing import Callable, Mapping

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
    constraint: Callable[[list[str]], bool] | None = None,
) -> int:
    if s in visited:
        return 0

    visited.add(s)
    current_path.append(s)

    if s == e:
        visited.remove(s)
        current_path.pop()
        print(current_path)
        return constraint is None or constraint(current_path)

    paths = sum(dfs(g, n, e, visited, current_path, constraint) for n in g[s])

    current_path.pop()
    visited.remove(s)
    return paths


def simple_paths(
    graph: Graph,
    start_node: str,
    end_node: str,
    constraint: Callable[[list[str]], bool] | None = None,
) -> int:
    current_path = []
    visited = set()
    return dfs(
        graph, start_node, end_node, visited, current_path, constraint=constraint
    )


def invert_graph(graph: Graph):
    inverted = defaultdict(set)
    for k, v in graph.items():
        for e in v:
            inverted[e].add(k)
    return inverted


def count_path(graph: Graph, source, destination) -> int:
    from pprint import pprint

    in_degree = {k: len(v) for k, v in graph.items()}
    for n in set.union(*graph.values()) - set(in_degree):
        in_degree[n] = 0

    pprint(in_degree)
    pprint(graph)
    q = deque()
    for k, v in in_degree.items():
        if v == 0:
            q.append(k)

    top_order = []
    while q:
        node = q.popleft()
        top_order.append(node)
        for ng in graph[node]:
            in_degree[ng] -= 1
            if in_degree[ng] == 0:
                q.append(ng)

    ways = defaultdict(int)
    ways[source] = 1
    for node in top_order:
        for ng in graph[node]:
            ways[ng] += ways[node]

    return ways[destination]


def solution_01(path: str = "input.data") -> int:
    graph = parse_data(path)
    return count_path(graph, "you", "out")


def solution_02(path: str = "input.data") -> int:
    graph = parse_data(path)
    return simple_paths(
        graph, "svr", "out", constraint=lambda path: "fft" in path and "dac" in path
    )


if __name__ == "__main__":
    from pprint import pprint

    # pprint(solution_02("test_02.data"))
    pprint(solution_01("test.data"))
