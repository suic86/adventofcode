def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def solution_01(path="input.data"):
    m = parse_data(path)
    h, w = len(m), len(m[0])
    dy, dx = (-1, 0)
    ps = set()
    gy, gx = next((y, x) for y, r in enumerate(m) for x, c in enumerate(r) if c == "^")
    ps.add((gy, gx))
    while (0 <= gy + dy < h) and (0 <= gx + dx < w):
        if m[gy + dy][gx + dx] == "#":
            dy, dx = dx, -dy
        gy += dy
        gx += dx
        ps.add((gy, gx))
    return len(ps)


def solution_02(path="input.data"):
    return -1


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
