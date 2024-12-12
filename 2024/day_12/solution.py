def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def total_price(m: list[str]) -> int:
    w, h = len(m[0]), len(m)
    visited = set()

    def dfs(t: tuple[int, int], k: str) -> int:
        neighbours = (-1, 0), (0, -1), (0, 1), (1, 0)
        stack = [t]
        perimeter = 0
        area = 0
        while stack:
            t = stack.pop()
            if t in visited:
                continue
            area += 1
            visited.add(t)
            y, x = t
            for dy, dx in neighbours:
                ny, nx = y + dy, x + dx
                if not (0 <= nx < w and 0 <= ny < h) or m[ny][nx] != k:
                    perimeter += 1
                    continue
                stack.append((ny, nx))
        return perimeter * area

    total = 0
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            t = (y, x)
            if t not in visited:
                total += dfs(t, m[y][x])

    return total


def solution_01(path="input.data"):
    return total_price(parse_data(path))


def solution_02(path="input.data"):
    return -1


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
