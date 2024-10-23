from collections import Counter
from functools import reduce
from itertools import groupby
from operator import mul, sub


def read_data(path):
    with open(path) as fobj:
        return list(map(int, fobj))


def solution_01(path="input.data"):
    adapters = sorted(read_data(path))
    diff_counts = Counter({1: 0, 3: 0})
    diff_counts[adapters[0]] += 1
    diff_counts.update(map(sub, adapters[1:], adapters))
    # + 1 is "own device joltage"
    return diff_counts[1] * (diff_counts[3] + 1)


def solution_02(path="input.data"):
    data = sorted(read_data(path) + [0])
    differences = map(sub, data[1:], data)
    groups_of_ones = (sum(1 for _ in g) for k, g in groupby(differences) if k == 1)
    coefficients = {1: 1, 2: 2, 3: 4, 4: 7}
    return reduce(mul, map(coefficients.get, groups_of_ones))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
