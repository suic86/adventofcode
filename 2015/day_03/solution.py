from itertools import chain


def parse_input(path="input.data"):
    with open(path) as fobj:
        return fobj.read().rstrip()


def houses(moves):
    xs = {">": 1, "<": -1, "^": 0, "v": 0}
    ys = {">": 0, "<": 0, "^": 1, "v": -1}
    x = y = 0
    yield x, y
    for move in moves:
        x += xs[move]
        y += ys[move]
        yield x, y


def solution_01(moves):
    return len(set(houses(moves)))


def solution_02(moves):
    return len(set(chain(houses(moves[::2]), houses(moves[1::2]))))


if __name__ == "__main__":
    print("Solution 01:", solution_01(parse_input()))
    print("Solution 02:", solution_02(parse_input()))
