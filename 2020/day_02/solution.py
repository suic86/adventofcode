from re import compile

PARSER = compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_data(parser=PARSER):
    with open("input.data") as f:
        return parser.findall(f.read())


def solution_01():
    return sum(int(l) <= p.count(c) <= int(u) for l, u, c, p in parse_data())


def solution_02():
    result = 0
    for f, s, c, p in parse_data():
        try:
            if (p[int(f) - 1], p[int(s) - 1]).count(c) == 1:
                result += 1
        except IndexError:
            pass
    return result


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
