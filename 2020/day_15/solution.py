from collections import defaultdict


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().rstrip().split(",")))


def solution(init, index):
    if index < len(init):
        return init[index - 1]

    indices = defaultdict(list)

    for i, n in enumerate(init):
        indices[n].append(i)

    for i in range(len(init), index):
        idx = indices[n]
        n = len(idx) != 1 and int.__rsub__(*idx[-2:]) or 0
        indices[n].append(i)
    return n


def solution_01(init=None):
    if init is None:
        init = read_data()
    return solution(init, 2020)


def solution_02(init=None):
    if init is None:
        init = read_data()
    return solution(init, 30000000)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
