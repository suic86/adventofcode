from re import compile


def parse_data(path="input.data"):
    parse_line = compile(r"\d+").findall
    with open(path) as fobj:
        return [list(map(int, parse_line(line))) for line in fobj]


def full_overlap(assignment):
    a, b, c, d = assignment
    return (a <= c and b >= d) or (c <= a and d >= b)


def any_overlap(assignment):
    a, b, c, d = assignment
    return (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d)


def solution_01(path="input.data"):
    return sum(map(full_overlap, parse_data(path)))


def solution_02(path="input.data"):
    return sum(map(any_overlap, parse_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
