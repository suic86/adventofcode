from re import compile


def parse_data(path="input.data"):
    parse_line = compile(r"\d+").findall
    with open(path) as fobj:
        return [list(map(int, parse_line(line))) for line in fobj]


def full_overlap(assignment):
    s1, e1, s2, e2 = assignment
    return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)


def any_overlap(assignment):
    s1, e1, s2, e2 = assignment
    # no overlap:
    #       s1--e1
    # s2--e2      s2--e2
    return not (e2 < s1 or e1 < s2)


def solution_01(path="input.data"):
    return sum(map(full_overlap, parse_data(path)))


def solution_02(path="input.data"):
    return sum(map(any_overlap, parse_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
