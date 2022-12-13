from functools import reduce
from operator import mul


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def visible_trees(grid):
    h = len(grid)
    w = len(grid[0])
    edges = 2 * h + 2 * w - 4
    visible = 0
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            v = grid[r][c]
            visible += (
                max(grid[r][:c]) < v  # from up
                or max(grid[r][c + 1 :]) < v  # from down
                or max(grid[i][c] for i in range(r)) < v  # from left
                or max(grid[i][c] for i in range(r + 1, h)) < v  # from right
            )
    return edges + visible


def compute_view(v, rng):
    res = 0
    for e in rng:
        res += 1
        if e >= v:
            break
    return res


def max_scenic_score(grid):
    h = len(grid)
    w = len(grid[0])
    return max(
        reduce(
            mul,
            (
                compute_view(grid[r][c], direction)
                for direction in [
                    grid[r][c + 1 :],  # right
                    reversed(grid[r][:c]),  # left
                    (grid[i][c] for i in range(r - 1, -1, -1)),  # up
                    (grid[i][c] for i in range(r + 1, h)),  # down
                ]
            ),
        )
        for r in range(1, h - 1)
        for c in range(1, w - 1)
    )


def solution_01(path="input.data"):
    return visible_trees(parse_data(path))


def solution_02(path="input.data"):
    return max_scenic_score(parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
