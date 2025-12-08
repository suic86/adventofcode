from collections import defaultdict
from functools import cache
from math import prod


def parse_data(path="input.data"):
    with open(path) as fp:
        return frozenset(
            tuple(map(int, line.split(","))) for line in map(str.strip, fp)
        )


def distance_squared(t1, t2):
    return sum((c1 - c2) ** 2 for c1, c2 in zip(t1, t2))


@cache
def shortest_distances(boxes):
    distances = defaultdict(list)

    for b1 in boxes:
        for b2 in boxes:
            if b1 != b2:
                distances[distance_squared(b1, b2)].append((b1, b2))
    return distances


def connected_components(graph):
    vertices = set(graph)
    visited = set()
    components = []

    while True:
        vertices -= visited
        if not vertices:
            break
        component = set()
        stack = [vertices.pop()]
        while stack:
            c = stack.pop()
            if c in visited:
                continue
            component.add(c)
            visited.add(c)
            stack += graph[c]
        components.append(component)
    return components


def solution_01(path="input.data", shortest_n=1000, top_n=3):
    boxes = parse_data(path)
    distances = shortest_distances(boxes)
    graph = defaultdict(set)
    for d in sorted(distances)[:shortest_n]:
        b1, b2 = distances[d][0]
        graph[b1].add(b2)
        graph[b2].add(b1)
    return prod(sorted(map(len, connected_components(graph)), reverse=True)[:top_n])


def solution_02(path="input.data"):
    boxes = parse_data(path)
    box_count = len(boxes)
    distances = shortest_distances(boxes)

    graph = defaultdict(set)

    def is_one_circuit(graph):
        return len(graph) == box_count and len(connected_components(graph)) == 1

    for d in sorted(distances):
        b1, b2 = distances[d][0]
        graph[b1].add(b2)
        graph[b2].add(b1)
        if is_one_circuit(graph):
            return b1[0] * b2[0]

    raise ValueError("Invalid input.")


if __name__ == "__main__":
    print(f"Solution 01: {solution_01('input.data')}")
    print(f"Solution 02: {solution_02('input.data')}")
