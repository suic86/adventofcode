from operator import sub
from collections import Counter


def parse_data(path="input.data"):
    with open(path) as fobj:
        ls, rs = [], []
        for line in map(str.rstrip, fobj):
            l, r = map(int, line.split())
            ls.append(l)
            rs.append(r)
        return ls, rs


def solution_01(path="input.data") -> int:
    ls, rs = parse_data(path)
    return sum(map(abs, map(sub, sorted(ls), sorted(rs))))


def solution_02(path="input.data") -> int:
    ls, rs = parse_data(path)
    cs = Counter(rs)
    return sum(l * cs.get(l, 0) for l in ls)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
