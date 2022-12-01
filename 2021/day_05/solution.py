from collections import defaultdict
from re import findall


def load_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, findall(r"\d+", row))) for row in fobj]


def draw_lines(lines, diagonals=False):
    covered = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        # vertical line
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            for i in range(y1, y2 + 1):
                covered[(i, x1)] += 1

        # horizontal line
        if y1 == y2:
            x1, x2 = sorted((x1, x2))
            for i in range(x1, x2 + 1):
                covered[(y1, i)] += 1

        if not diagonals:
            continue

        # diagonal
        if abs(y2 - y1) == abs(x2 - x1):
            dx = -1 if x1 > x2 else 1
            dy = -1 if y1 > y2 else 1
            for p in zip(range(y1, y2 + 1 * dy, dy), range(x1, x2 + 1 * dx, dx)):
                covered[p] += 1
    return covered


def solution_01(path="input.data"):
    return sum(p > 1 for p in draw_lines(load_data(path), diagonals=False).values())


def solution_02(path="input.data"):
    return sum(p > 1 for p in draw_lines(load_data(path), diagonals=True).values())


if __name__ == "__main__":
    print(solution_01("input.data"))
    print(solution_02("input.data")[0])
