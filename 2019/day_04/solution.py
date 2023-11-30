from itertools import groupby

LBOUND = 147981
UBOUND = 691423


def check_part_01(n: str) -> bool:
    return (
        all(i <= j for i, j in zip(n, n[1:]))
        and sum(i == j for i, j in zip(n, n[1:])) >= 1
    )


def check_part_02(n: str) -> bool:
    return all(i <= j for i, j in zip(n, n[1:])) and any(
        len(list(v)) == 2 for _, v in groupby(n)
    )


def solution_01(lbound: int = LBOUND, ubound: int = UBOUND) -> int:
    return sum(map(check_part_01, map(str, range(lbound, ubound + 1))))


def solution_02(lbound: int = LBOUND, ubound: int = UBOUND) -> int:
    return sum(map(check_part_02, map(str, range(lbound, ubound + 1))))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
