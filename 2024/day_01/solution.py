from collections import Counter
from operator import sub


def parse_data(path="input.data"):
    with open(path) as fobj:
        ls, rs = [], []
        for l, r in map(str.split, fobj):
            ls.append(int(l))
            rs.append(int(r))
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
