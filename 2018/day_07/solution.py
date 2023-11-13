from collections import defaultdict
from copy import deepcopy
from heapq import heapify, heappop, heappush

Graph = dict[str, set[str]]


def load_data(path: str = "input.data") -> Graph:
    with open(path) as fobj:
        graph = defaultdict(set)
        for line in map(str.strip, fobj):
            # Step C must be finished before step A can begin.
            #      f                              t
            _, f, *_, t, _, _ = line.split()
            graph[t].add(f)
    return graph


def tsort(graph: Graph) -> str:
    # don't mutate the input
    g = deepcopy(graph)
    # see: https://en.wikipedia.org/wiki/Topological_sorting#Kahn%27s_algorithm
    l = []
    # set nodes without incomming edges
    s = list(set.union(*g.values()) - set(g))
    # use heap to keep lexicographical order
    heapify(s)

    while s:
        n = heappop(s)
        l.append(n)

        for m in list(g):
            if n in g[m]:
                g[m].remove(n)
                if not g[m]:
                    heappush(s, m)
                    del g[m]

    if g:
        raise ValueError("Graph has a cycle.")

    return "".join(l)


def construction_time(steps: Graph, workers=5, default_duration=60) -> int:
    # don't mutate the input
    dependencies = deepcopy(steps)
    # steps with do dependencies
    available = list(set.union(*dependencies.values()) - set(dependencies))

    # use heap to keep lexicographical order
    heapify(available)

    finished = set()
    total_time = 0
    ws: dict[str, int] = {}
    duration = lambda t: ord(t) - ord("A") + 1 + default_duration

    # assign available steps to idle workers
    for _ in range(workers - len(ws)):
        if not available:
            break
        t = heappop(available)
        ws[t] = duration(t)

    while dependencies or ws:
        # do work
        for k in list(ws):
            ws[k] -= 1
            if ws[k] == 0:
                finished.add(k)
                del ws[k]

        # update available steps
        for k in list(dependencies):
            dependencies[k] -= finished
            if not dependencies[k]:
                del dependencies[k]
                heappush(available, k)

        # assign available steps to idle workers
        for _ in range(workers - len(ws)):
            if not available:
                break
            t = heappop(available)
            ws[t] = duration(t)

        total_time += 1
    return total_time


def solution_01(path="input.data") -> str:
    return tsort(load_data(path))


def solution_02(path="input.data") -> int:
    return construction_time(load_data(path), workers=5)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
