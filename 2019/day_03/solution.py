Wire = dict[tuple[int, int], int]


def parse_row(row: str) -> list[tuple[str, int]]:
    return [(d, int("".join(l))) for d, *l in row.split(",")]


def parse_wires(path: str) -> tuple[Wire, Wire]:
    rows = 0
    with open(path) as fobj:
        rows = list(map(parse_row, fobj))

    if len(rows) != 2:
        raise ValueError(f"Invalid number of wires: {len(rows)} (required: 2).")

    ws: list[dict[tuple[int, int], int]] = []
    directions = {"D": (0, 1), "U": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for row in rows[:2]:
        s = 0
        w = {}
        x = y = 0
        for d, l in row:
            dx, dy = directions[d]
            for _ in range(l):
                s += 1
                x += dx
                y += dy
                if (x, y) not in w:
                    w[(x, y)] = s
        ws.append(w)
    return ws[0], ws[1]


def solution_01(path: str = "input.data") -> int:
    w1, w2 = parse_wires(path)
    return min(abs(x) + abs(y) for x, y in set(w1) & set(w2))


def solution_02(path: str = "input.data") -> int:
    w1, w2 = parse_wires(path)
    return min(w1[t] + w2[t] for t in set(w1) & set(w2))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 01: {solution_02()}")
