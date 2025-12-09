from itertools import product


def parse_data(path="input.data"):
    with open(path) as fp:
        return [tuple(map(int, line.split(","))) for line in map(str.strip, fp)]


def solution_01(path="input.data"):
    bricks = parse_data(path)

    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in product(bricks, repeat=2)
    )
