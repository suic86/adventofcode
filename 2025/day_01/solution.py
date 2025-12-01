def parse_data(path: str = "input.data") -> list[tuple[str, int]]:
    with open(path) as fp:
        return [(d, int("".join(v))) for d, *v in map(str.rstrip, fp)]


def solution_01(path: str = "input.data") -> int:
    r = 50
    nv = 0
    for d, v in parse_data(path):
        if d == "R":
            r += v
        elif d == "L":
            r -= v
        else:
            raise ValueError("Invalid rotation")
        r %= 100
        if r == 0:
            nv += 1
    return nv


def solution_02(path: str = "input.data") -> int:
    r = 50
    nv = 0

    for d, v in parse_data(path):
        for _ in range(v):
            if d == "R":
                r += 1
            elif d == "L":
                r -= 1
            else:
                raise ValueError("Invalid rotation")
            r %= 100
            if r == 0:
                nv += 1
    return nv


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
