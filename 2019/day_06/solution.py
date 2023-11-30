from collections import defaultdict, deque

Digraph = dict[str, set[str]]


def parse_data(path: str = "input.data") -> Digraph:
    graph: dict[str, set[str]] = defaultdict(set)
    with open(path) as fobj:
        for line in map(str.strip, fobj):
            i, j = line.split(")")
            graph[i].add(j)
    return graph


def count_orbits(graph: Digraph) -> int:
    roots = set(graph) - set.union(*graph.values())
    if len(roots) != 1:
        raise ValueError("Invalid input. `graph` has multiple roots.")

    # use DFS to assign the number of orbits (== distance from the root) to each object
    root = roots.pop()
    orbits = {root: 0}
    stack = [root]
    visited: set[str] = set()

    while stack:
        node = stack.pop()
        for a in graph[node] - visited:
            stack.append(a)
            orbits[a] = orbits[node] + 1
        visited.add(node)
    return sum(orbits.values())


def shortest_path_length(graph: Digraph) -> int:
    # convert to undirected graph
    for n in list(graph):
        for a in graph[n]:
            graph[a].add(n)

    # use BFS to find the shortest distance
    queue: deque[tuple[str, int]] = deque([("YOU", 0)])
    visited: set[str] = set()

    while queue:
        node, distance = queue.popleft()
        # [Distance b]etween the objects they are orbiting - not between YOU and SAN.
        if "SAN" in graph[node]:
            return distance - 1
        for a in graph[node] - visited:
            queue.append((a, distance + 1))
        visited.add(node)

    raise ValueError("YOU and SAN are not connected.")


def solution_01(path: str = "input.data") -> int:
    return count_orbits(parse_data(path))


def solution_02(path: str = "input.data") -> int:
    return shortest_path_length(parse_data(path))
