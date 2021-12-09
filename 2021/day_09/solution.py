from functools import reduce
from heapq import nlargest
from operator import mul


def load_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, row.strip())) for row in fobj]


def low_points(data):
    height = len(data)
    width = len(data[0])
    adjacents = (1, 0), (0, 1), (-1, 0), (0, -1)
    result = []
    for r, row in enumerate(data):
        for c, column in enumerate(row):
            min_adjacent = min(
                data[r + dr][c + dc]
                for dr, dc in adjacents
                if 0 <= r + dr < height and 0 <= c + dc < width
            )
            if column < min_adjacent:
                result.append([(r, c), column])
    return result


def basin_sizes(data):
    height = len(data)
    width = len(data[0])
    adjacents = (1, 0), (0, 1), (-1, 0), (0, -1)
    sizes = []
    for low_point, _ in low_points(data):
        stack = [low_point]
        visited = set()
        while stack:
            r, c = stack.pop()
            for dr, dc in adjacents:
                adjacent = r + dr, c + dc
                if 0 <= adjacent[0] < height and 0 <= adjacent[1] < width:
                    if adjacent not in visited and data[adjacent[0]][adjacent[1]] != 9:
                        visited.add(adjacent)
                        stack.append(adjacent)
        sizes.append(len(visited))
    return sizes


def solution_01(path="input.data"):
    return sum(height + 1 for _, height in low_points(load_data(path)))


def solution_02(path="input.data"):
    return reduce(mul, nlargest(3, basin_sizes(load_data(path))), 1)


if __name__ == "__main__":
    print(f"Solution 01 {solution_01('input.data')}")
    print(f"Solution 02 {solution_02('input.data')}")
