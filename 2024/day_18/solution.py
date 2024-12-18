from collections import defaultdict
from heapq import heappop, heappush
from operator import itemgetter


class UnreachableExit(Exception):
    pass


def parse_data(path="input.data"):
    with open(path) as fobj:
        return [tuple(map(int, line.split(","))) for line in map(str.strip, fobj)]


def shortest_path_length(
    invalid: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> int:
    sx, sy = start
    ex, ey = end
    pq = []

    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0
    heappush(pq, (dist[(sx, sy)], sx, sy))
    visited = set()

    while pq:
        l, x, y = heappop(pq)
        visited.add((x, y))
        if x == ex and y == ey:
            return l
        for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
            if sx <= (nx := x + dx) <= ex and sy <= (ny := y + dy) <= ey:
                n = (nx, ny)
                if n in invalid or n in visited:
                    continue
                if (nl := l + 1) < dist[n]:
                    dist[n] = nl
                    heappush(pq, (nl, nx, ny))
    raise UnreachableExit("Endpoint not reachable.")


def start_end(data: list[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = min(map(itemgetter(0), data)), min(map(itemgetter(1), data))
    end = max(map(itemgetter(0), data)), max(map(itemgetter(1), data))
    return start, end


def solution_01(path="input.data", size: int = 1024) -> int:
    data = parse_data(path)[:size]
    return shortest_path_length(data, *start_end(data))


def solution_02(path="input.data") -> tuple[int, int]:
    data = parse_data(path)
    res = (-1, 1)
    start, end = start_end(data)
    while data:
        try:
            shortest_path_length(data, start, end)
            return res
        except UnreachableExit:
            res = data.pop()
    return res


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
