from re import compile

PARSER = compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_data(parser=PARSER):
    with open("input.data") as f:
        return parser.findall(f.read())


def solution_01():
    return sum(int(l) <= p.count(c) <= int(u) for l, u, c, p in parse_data())


def solution_02():
    return sum(
        (p[int(f) - 1] == c) ^ (p[int(s) - 1] == c) for f, s, c, p in parse_data()
    )


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
