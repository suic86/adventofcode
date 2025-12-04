def parse_data(path="input.data") -> list[list[str]]:
    with open(path) as fp:
        return list(map(list, fp))


def accessible(data: list[list[str]]) -> set[tuple[int, int]]:
    height = len(data)
    width = len(data[0])
    adjacents = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    result = set()
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col != "@":
                continue
            ok = 0
            for dr, dc in adjacents:
                if 0 <= (ar := r + dr) < height and 0 <= (ac := c + dc) < width:
                    ok += data[ar][ac] == "@"
            if ok < 4:
                result.add((r, c))
    return result


def solution_01(path="input.data") -> int:
    return len(accessible(parse_data(path)))


def solution_02(path="input.data") -> int:
    data = parse_data(path)
    total = 0
    while True:
        acs = accessible(data)
        if len(acs) == 0:
            break
        total += len(acs)
        for r, c in acs:
            data[r][c] = "."
    return total


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
