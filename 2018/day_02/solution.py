from collections import Counter
from itertools import combinations


def read_data():
    with open("input.data") as source_file:
        return list(map(str.rstrip, source_file))


def solution_01():
    two, three = 0, 0
    for cnt in map(Counter, read_data()):
        two += 2 in cnt.values()
        three += 3 in cnt.values()
    return two * three


def is_similar(ids):
    return sum(c1 != c2 for c1, c2 in zip(*ids)) == 1


def solution_02():
    return "".join(
        c1
        for c1, c2 in zip(
            *next(ids for ids in combinations(read_data(), 2) if is_similar(ids))
        )
        if c1 == c2
    )


if __name__ == "__main__":
    print("Solution_01:", solution_01())
    print("Solution_02:", solution_02())
