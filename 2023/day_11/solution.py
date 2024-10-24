from itertools import combinations


def parse_data(path: str, expansion_factor: int = 2) -> set[tuple[int, int]]:
    with open(path) as fobj:
        gxs = set()
        mx = my = 0
        for y, row in enumerate(fobj):
            for x, col in enumerate(row):
                if col == "#":
                    gxs.add((x, y))
                    mx = max(x, mx)
                    my = max(y, my)

    ecs = set(range(mx)) - {x for (x, _) in gxs}
    ers = set(range(my)) - {y for (_, y) in gxs}

    # to expand a row/column by n, n - 1 rows/columns need to added
    expansion_factor -= 1

    dr = 0
    drs = {}
    for r in range(my + 1):
        if r in ers:
            dr += expansion_factor
        else:
            drs[r] = dr

    dc = 0
    dcs = {}
    for c in range(mx + 1):
        if c in ecs:
            dc += expansion_factor
        else:
            dcs[c] = dc

    return {(x + dcs[x], y + drs[y]) for (x, y) in gxs}


def total_length(path: str, expansion_factor=2) -> int:
    galaxies = parse_data(path, expansion_factor)
    return sum(
        abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in combinations(galaxies, 2)
    )


def solution_01(path: str) -> int:
    return total_length(path, expansion_factor=2)


def solution_02(path: str) -> int:
    return total_length(path, expansion_factor=1_000_000)
