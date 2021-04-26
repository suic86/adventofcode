from hashlib import md5
from itertools import count


PUZZLE_INPUT = "iwrupvqb"


def advent_coin(key, zeroes=5):
    zeroes = "0" * zeroes
    return next(
        i for i in count() if md5(f"{key}{i}".encode()).hexdigest().startswith(zeroes)
    )


def solution_01():
    return advent_coin(PUZZLE_INPUT, zeroes=5)


def solution_02():
    return advent_coin(PUZZLE_INPUT, zeroes=6)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
