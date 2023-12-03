from itertools import product
from re import compile
from typing import Generator

RGX = compile(r"\d+")
Part = tuple[int, int, int, int]
Schema = list[str]


def load_data(path: str = "input.data") -> Schema:
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def symbols(schema: Schema) -> set[tuple[int, int]]:
    return {
        (y, x)
        for y, r in enumerate(schema)
        for x, c in enumerate(r)
        if not c.isdigit() and c != "."
    }


def gears(schema: Schema) -> set[tuple[int, int]]:
    return {(y, x) for y, r in enumerate(schema) for x, c in enumerate(r) if c == "*"}


def adjacents(y: int, x: int) -> Generator[tuple[int, int], None, None]:
    return ((y + dy, x + dx) for dy, dx in product((-1, 0, 1), repeat=2) if dx or dy)


def find_part_numbers(schema: Schema) -> list[int]:
    rgx = RGX
    ss = symbols(schema)
    parts: list[int] = []
    for y, r in enumerate(schema):
        for m in rgx.finditer(r):
            for x in range(m.start(), m.end()):
                if any(map(ss.__contains__, adjacents(y, x))):
                    parts.append(int(m.group(0), base=10))
                    break
    return parts


def find_parts(schema: Schema) -> list[Part]:
    rgx = RGX
    return [
        (i, m.start(), m.end(), int(m.group(0)))
        for i, r in enumerate(schema)
        for m in rgx.finditer(r)
    ]


def sum_of_gear_ratios(schema: Schema) -> int:
    parts = find_parts(schema)
    result = 0

    for gy, gx in gears(schema):
        ps = []
        for py, pxs, pxe, v in parts:
            if py - gy < -1:
                continue
            if py - gy > 1:
                break
            for y, x in adjacents(gy, gx):
                if y != py:
                    continue
                if pxs <= x < pxe:
                    ps.append(v)
                    break
        if len(ps) == 2:
            result += ps[0] * ps[1]

    return result


def solution_01(path: str = "input.data") -> int:
    return sum(find_part_numbers(load_data(path)))


def solution_02(path: str = "input.data") -> int:
    return sum_of_gear_ratios(load_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
