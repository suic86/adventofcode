from functools import reduce
from operator import sub


def parse_data(path: str = "input.data") -> list[list[int]]:
    with open(path) as fobj:
        return [list(map(int, line.split())) for line in map(str.strip, fobj)]


def interpolate(line: list[int]) -> int:
    result = []
    while True:
        result.append(line[-1])
        line = list(map(sub, line[1:], line))
        if not any(line):
            break
    return sum(result)


def interpolate_part_2(line: list[int]) -> int:
    result = []
    while True:
        result.append(line[0])
        line = list(map(sub, line[1:], line))
        if not any(line):
            result.append(0)
            break
    return reduce(int.__rsub__, reversed(result))


def solution_01(path: str = "input.data") -> int:
    return sum(map(interpolate, parse_data(path)))


def solution_02(path: str = "input.data") -> int:
    return sum(map(interpolate_part_2, parse_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
