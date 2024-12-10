from collections import defaultdict


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(list(map(int, row)) for row in map(str.rstrip, fobj))


def score(y: int, x: int, tm: list[list[int]], part2=False) -> int:
    stack = [(y, x, 0)]
    h, w = len(tm), len(tm[0])
    nines = defaultdict(int)
    neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while stack:
        y, x, n = stack.pop()
        if n == 9:
            nines[(y, x)] += 1
            continue
        for dy, dx in neighbours:
            if (
                0 <= (nx := x + dx) < w
                and 0 <= (ny := y + dy) < h
                and tm[ny][nx] == n + 1
            ):
                stack.append((ny, nx, n + 1))
    return sum(nines.values()) if part2 else len(nines)


def solution(path: str, part2: bool = False) -> int:
    tm = parse_data(path)
    return sum(
        score(y, x, tm, part2)
        for y, row in enumerate(tm)
        for x, col in enumerate(row)
        if col == 0
    )


def solution_01(path: str = "input.data") -> int:
    return solution(path)


def solution_02(path="input.data"):
    return solution(path, part2=True)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
