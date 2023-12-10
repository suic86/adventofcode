from functools import reduce
from itertools import cycle, islice
from math import lcm
from re import compile


def parse_data(path: str = "input.data") -> tuple[str, dict[str, list[str]]]:
    parser = compile(r"[0-9A-Z]{3}")

    with open(path) as fobj:
        lines = map(str.strip, fobj)
        directions = next(lines)
        graph = {}
        for line in islice(lines, 1, None):
            f, *t = parser.findall(line)
            graph[f] = t
        return directions, graph


def solution_01(path: str = "input.data", start: str = "AAA", end: str = "ZZZ") -> int:
    directions, graph = parse_data(path)
    current = start
    for step, direction in enumerate(cycle(directions), start=1):
        current = graph[current][direction == "R"]
        if current == end:
            return step
    raise ValueError("Invalid input.")


def solution_02(path: str = "input.data") -> int:
    directions, graph = parse_data(path)
    nodes = [node for node in graph if node.endswith("A")]
    steps = []
    for step, direction in enumerate(cycle(directions), start=1):
        n = []
        for node in nodes:
            node = graph[node][direction == "R"]
            if node.endswith("Z"):
                steps.append(step)
            else:
                n.append(node)
        if not nodes:
            break
        nodes = n
    return reduce(lcm, steps)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
