# See: https://www.redblobgames.com/grids/hexagons/#neighbors-cube
CONVERSION = {
    "n": (0, -1, 1),
    "ne": (1, -1, 0),
    "se": (1, 0, -1),
    "s": (0, 1, -1),
    "sw": (-1, 1, 0),
    "nw": (-1, 0, 1),
}

ADJACENTS = list(CONVERSION.values())


def parse_data(path="input.data"):
    with open(path) as fobj:
        return fobj.read().strip().split(",")


def distance(path):
    q, r, s = 0, 0, 0
    for dq, dr, ds in map(CONVERSION.get, path):
        q += dq
        r += dr
        s += ds
    return max(map(abs, (q, r, s)))


def farthest(path):
    q, r, s = 0, 0, 0
    steps = 0
    for dq, dr, ds in map(CONVERSION.get, path):
        q += dq
        r += dr
        s += ds
        if (distance := max(map(abs, (q, r, s)))) > steps:
            steps = distance
    return steps


def solution_01(path="input.data"):
    return distance(parse_data(path))


def solution_02(path="input.data"):
    return farthest(parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
