from itertools import chain, starmap


def parse_data(path="input.data") -> list[tuple[int, ...]]:
    with open(path) as fobj:
        return [tuple(map(int, line.split())) for line in map(str.strip, fobj)]


def read_by_columns(rows: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    first, second, third = [], [], []
    for row in rows:
        f, s, t = row
        first.append(f)
        second.append(s)
        third.append(t)

    return list(
        chain.from_iterable(zip(*[iter(x)] * 3) for x in (first, second, third))
    )


def is_triangle(a: int, b: int, c: int) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def solution_01(path="input.data") -> int:
    return sum(starmap(is_triangle, parse_data(path)))


def solution_02(path="input.data") -> int:
    return sum(starmap(is_triangle, read_by_columns(parse_data(path))))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
