from collections import defaultdict
from heapq import heappop, heappush


def load_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, row.strip())) for row in fobj]


def scaled_grid_value(data, row, column):
    height, width = len(data), len(data[0])

    dr, gr = divmod(row, height)
    dc, gc = divmod(column, width)

    value = data[gr][gc] + dr + dc
    while value > 9:
        value -= 9
    return value


def dijkstra_with_heap(graph, scale=1):
    # Adaptation of https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e
    height = len(graph) * scale
    width = len(graph[0]) * scale

    top_left = (0, 0)
    bottom_right_corner = (height - 1, width - 1)

    def adjacents(node):
        r, c = node
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (0 <= r + dr < height) and (0 <= c + dc < width):
                yield r + dr, c + dc

    visited = set()
    priority_queue = []
    dist = defaultdict(lambda: float("inf"))
    dist[top_left] = 0
    heappush(priority_queue, (0, top_left))

    while priority_queue:
        _, node = heappop(priority_queue)
        visited.add(node)

        for adjacent in adjacents(node):
            if adjacent in visited:
                continue
            weight = scaled_grid_value(graph, adjacent[0], adjacent[1])
            new_risk = dist[node] + weight
            if adjacent == bottom_right_corner:
                return new_risk
            if new_risk < dist[adjacent]:
                dist[adjacent] = new_risk
                heappush(priority_queue, (new_risk, adjacent))


def solution_01(path="input.data"):
    data = load_data(path)
    return dijkstra_with_heap(data)


def solution_02(path="input.data"):
    data = load_data(path)
    return dijkstra_with_heap(data, scale=5)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
