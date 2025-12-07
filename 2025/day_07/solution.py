from collections import defaultdict


def parse_data(path: str = "input.data"):
    with open(path) as fp:
        return list(map(str.strip, fp))


def solution_01(path: str = "input.data") -> int:
    lines = parse_data(path)
    beams = {lines[0].find("S")}
    splits = 0

    def split_beam(splitter):
        beams.remove(splitter)
        if (left := splitter - 1) not in beams:
            beams.add(left)
        if (right := splitter + 1) not in beams:
            beams.add(right)

    for line in lines[1:]:
        splitters = [i for i, e in enumerate(line) if e == "^"]
        splits += len(splitters)
        for splitter in splitters:
            if splitter not in beams:
                splits -= 1
                continue
            split_beam(splitter)

    return splits


def invert_graph(graph):
    inverted = defaultdict(set)
    for k, v in graph.items():
        for e in v:
            inverted[e].add(k)
    return inverted


def solution_02(path: str = "input.data") -> int:
    lines = parse_data(path)
    start = lines[0].find("S")
    beams = {start}
    graph = defaultdict(set)
    graph[(0, start)] = set()

    def split_beam(splitter, line_index):
        beams.remove(splitter)
        left, right = splitter - 1, splitter + 1
        beams.add(left)
        beams.add(right)
        graph[(line_index - 1, splitter)].add((line_index, left))
        graph[(line_index - 1, splitter)].add((line_index, right))

    for i, line in enumerate(lines[1:], start=1):
        splitters = [i for i, e in enumerate(line) if e == "^"]
        for beam in beams - set(splitters):
            graph[(i - 1, beam)].add((i, beam))
        for splitter in splitters:
            if splitter in beams:
                split_beam(splitter, i)

    graph = invert_graph(graph)
    incoming_paths = {}
    for i in range(1, len(lines)):
        for k, v in graph.items():
            if k[0] != i:
                continue
            n = 0
            for e in v:
                if e not in incoming_paths:
                    incoming_paths[e] = len(graph[e]) if e in graph else 1
                n += incoming_paths[e]
            incoming_paths[k] = n
    return sum(v for (line, _), v in incoming_paths.items() if line == len(lines) - 1)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
