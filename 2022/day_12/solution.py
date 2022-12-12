from collections import deque


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def shortest_path_length(grid, end, start=("S",)):
    h, w = len(grid), len(grid[0])

    mapping = {"E": "z", "S": "a"}

    def adjacents(r, c, v, d):
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            nv = grid[nr][nc]
            if ord(v) - ord(mapping.get(nv, nv)) < 2:
                yield nr, nc, nv, d + 1

    visited = set()
    queue = deque([(*end, "z", 0)])
    while queue:
        r, c, v, d = queue.popleft()
        visited.add((r, c))
        for r, c, v, d in adjacents(r, c, v, d):
            if v in start:
                return d
            if (r, c) in visited:
                continue
            visited.add((r, c))
            queue.append((r, c, v, d))
    raise ValueError("Distance not found.")


def solution(path="input.data", start="S"):
    grid = parse_data(path)
    end = None
    for i, r in enumerate(grid):
        if "E" in r:
            end = [i, r.find("E")]
            break
    if end is None:
        return ValueError("End location not found.")
    return shortest_path_length(grid, end, start)


def solution_01(path="input.data"):
    return solution(path)


def solution_02(path="input.data"):
    return solution(path, start=("S", "a"))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
