from functools import reduce
from operator import mul


def parse_data(path: str = "input.data") -> list[tuple[int, int]]:
    with open(path) as fobj:
        time, distance = fobj.read().split("\n")
        return list(zip(map(int, time.split()[1:]), map(int, distance.split()[1:])))


def parse_data_part2(path: str = "input.data") -> tuple[int, int]:
    with open(path) as fobj:
        time, distance = fobj.read().split("\n")
        return int("".join(time.split()[1:])), int("".join(distance.split()[1:]))


def wins(race: tuple[int, int]) -> int:
    time, distance = race
    return sum(i * (time - i) > distance for i in range(time))


def solution_01(path: str = "input.data") -> int:
    return reduce(mul, map(wins, parse_data(path)))


def solution_02(path: str = "input.data") -> int:
    return wins(parse_data_part2(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
