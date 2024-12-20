from collections import defaultdict
from heapq import heappop, heappush


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def best_path(maze: list[str], start: tuple[int, int], end: tuple[int, int]) -> int:
    sy, sx = start
    ey, ex = end
    h, w = len(maze), len(maze[0])
    in_maze = lambda y, x: 0 <= y < h and 0 <= x < w

    pq = []
    score = defaultdict(lambda: float("inf"))
    score[(sy, sx, 0, 1)] = 0
    heappush(pq, (score[(sy, sx, 0, 1)], sy, sx, 0, 1))
    visited = set()

    while pq:
        s, y, x, dy, dx = heappop(pq)
        visited.add((y, x, dy, dx))
        if x == ex and y == ey:
            return s
        if not in_maze(y, x) or maze[y][x] == "#":
            continue
        if (ns := s + 1) < score[((ny := y + dy), (nx := x + dx), dy, dx)]:
            score[(ny, nx, dy, dx)] = ns
            heappush(pq, (ns, ny, nx, dy, dx))
        for ndy, ndx in [(dx, -dy), (-dx, dy)]:
            if (ns := s + 1000) < score[(y, x, ndy, ndx)]:
                score[(y, x, ndy, ndx)] = ns
                heappush(pq, (ns, y, x, ndy, ndx))
    raise ValueError("Unreachable endpoint.")


def tiles(maze: list[str], start: tuple[int, int], end: tuple[int, int]) -> int:
    sy, sx = start
    ey, ex = end
    h, w = len(maze), len(maze[0])
    in_maze = lambda y, x: 0 <= y < h and 0 <= x < w

    pq = []
    score = defaultdict(lambda: float("inf"))
    score[(sy, sx, 0, 1)] = 0
    prev = defaultdict()
    heappush(pq, (score[(sy, sx, 0, 1)], sy, sx, 0, 1))
    visited = set()

    while pq:
        s, y, x, dy, dx = heappop(pq)
        visited.add((y, x, dy, dx))
        if x == ex and y == ey:
            n = 0
            t = end
            while True:
                if t not in prev:
                    return n
                n += 1
                t = prev[t]
        if not in_maze(y, x) or maze[y][x] == "#":
            continue
        if (ns := s + 1) < score[((ny := y + dy), (nx := x + dx), dy, dx)]:
            score[(ny, nx, dy, dx)] = ns
            prev[(ny, nx)] = (y, x)
            heappush(pq, (ns, ny, nx, dy, dx))
        for ndy, ndx in [(dx, -dy), (-dx, dy)]:
            if (ns := s + 1000) < score[(y, x, ndy, ndx)]:
                score[(y, x, ndy, ndx)] = ns
                heappush(pq, (ns, y, x, ndy, ndx))
    raise ValueError("Unreachable endpoint.")


def start_end(maze: list[str]):
    e = s = None
    for y, line in enumerate(maze):
        if e and s:
            break
        if "E" in line:
            e = (y, line.index("E"))
        if "S" in line:
            s = (y, line.index("S"))
    return s, e


def solution_01(path="input.data"):
    maze = parse_data(path)
    return best_path(maze, *start_end(maze))


def solution_02(path="input.data"):
    maze = parse_data(path)
    return tiles(maze, *start_end(maze))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
