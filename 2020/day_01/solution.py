def read_data():
    with open("./input.data") as f:
        return list(map(int, f))


def solution_01():
    data = set(read_data())
    for e in data:
        if (d := 2020 - e) in data:
            return e * d
    raise ValueError("Invalid data")


def _solution_02():
    # Caveats:
    # - Works only with distinct entries
    # - Can't detect cases when a + a + b == 2020 or a + a + a == 2020
    from functools import reduce
    from itertools import combinations
    from operator import mul

    data = set(read_data())
    return next(reduce(mul, t) for t in combinations(data, 3) if sum(t) == 2020)


def solution_02():
    data = sorted(read_data())
    for i, e1 in enumerate(data):
        for j, e2 in enumerate(data[i + 1 :], i + 1):
            for e3 in data[j + 1 :]:
                if e1 + e2 + e3 == 2020:
                    return e1 * e2 * e3
    raise ValueError("Invalid data")


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
