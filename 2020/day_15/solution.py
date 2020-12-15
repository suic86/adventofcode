from itertools import islice


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().rstrip().split(",")))


def gen_solution(init):
    numbers = init[:]
    indices = {n: [i] for i, n in enumerate(numbers)}

    for i, n in enumerate(init):
        yield n

    while True:
        i += 1
        if n not in indices:
            indices[n] = [i]
            n = 0
        elif len(indices[n]) == 1:
            if 0 not in indices:
                indices[0] = []
            indices[0].append(i)
            indices[n] = indices[n][-2:]
            n = 0
        elif len(indices[n]) >= 2:
            a, b = indices[n][-2:]
            n = b - a
            if n not in indices:
                indices[n] = []
            indices[n].append(i)
            indices[n] = indices[n][-2:]
        yield n


def solution_01(init=None):
    if init is None:
        init = read_data()
    return list(islice(gen_solution(init), 2020))[-1]


def solution_02(init=None):
    if init is None:
        init = read_data()
    return list(islice(gen_solution(init), 30000000))[-1]


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
