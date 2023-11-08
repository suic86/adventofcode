from itertools import permutations
from re import compile


PARSER = compile(r"([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)")


def parse_data(path="input.data"):
    graph = {}
    with open(path) as fobj:
        for line in map(str.strip, fobj):
            if (tokens := PARSER.fullmatch(line)) is None:
                raise ValueError(f"Invalid line: {line}")
            start, destination, distance = tokens.groups()
            graph[(start, destination)] = int(distance)
            graph[(destination, start)] = int(distance)
    return graph


def shortest_or_longest_path(graph, shortest=True):
    cities = set().union(*graph)
    total_distance = lambda path: sum(map(graph.get, zip(path, path[1:])))
    return [max, min][shortest](map(total_distance, permutations(cities, len(cities))))


def solution_01(path="input.data"):
    return shortest_or_longest_path(parse_data(path))


def solution_02(path="input.data"):
    return shortest_or_longest_path(parse_data(path), shortest=False)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
