from itertools import starmap


def parse_input(path="input.data"):
    with open(path) as fobj:
        for line in map(str.rstrip, fobj):
            yield map(int, line.split("x"))


def wrapping_paper(*sides):
    l, w, h = sorted(sides)
    return (2 * l * w + 2 * w * h + 2 * h * l) + l * w


def ribbon(*sides):
    l, w, h = sorted(sides)
    return 2 * l + 2 * w + l * w * h


def solution_01(path="input.data"):
    return sum(starmap(wrapping_paper, parse_input(path)))


def solution_02(path="input.data"):
    return sum(starmap(ribbon, parse_input(path)))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
