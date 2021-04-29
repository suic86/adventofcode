from itertools import groupby

PUZZLE_INPUT = 3113322113


def look_and_say(number: str):
    return "".join(f"{sum(1 for _ in v)}{k}" for k, v in groupby(number))


def apply_n_times(n, number=PUZZLE_INPUT):
    result = str(PUZZLE_INPUT)
    for _ in range(n):
        result = look_and_say(result)
    return result


def solution_01():
    return len(apply_n_times(40))


def solution_02():
    return len(apply_n_times(50))


if __name__ == "__main__":
    print("Solution 1:", solution_01())
    print("Solution 2:", solution_02())
