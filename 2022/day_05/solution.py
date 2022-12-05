from collections import defaultdict
from itertools import takewhile
from re import compile


def parse_stacks(stacks_data):
    stacks = defaultdict(list)
    for row in reversed(stacks_data[:-1]):
        for stack, crate in enumerate(row[1::4], start=1):
            if crate != " ":
                stacks[stack].append(crate)
    return stacks


def parse_moves(moves_data):
    moves_parser = compile(r"\d+").findall
    return [list(map(int, moves_parser(move))) for move in moves_data]


def parse_data(path="input.data"):
    with open(path) as fobj:
        data = (line.rstrip("\n") for line in fobj)
        stacks = parse_stacks(list(takewhile(lambda line: line != "", data)))
        moves = parse_moves(data)
    return stacks, moves


def solution_01(path="input.data"):
    stacks, moves = parse_data(path)
    for (c, f, t) in moves:
        for _ in range(c):
            if not f:
                continue
            stacks[t].append(stacks[f].pop())
    return "".join(v[-1] for _, v in sorted(stacks.items()))


def solution_02(path="input.data"):
    stacks, moves = parse_data(path)
    for (c, f, t) in moves:
        if not f:
            continue
        stacks[t].extend(stacks[f][-c:])
        stacks[f] = stacks[f][:-c]
    return "".join(v[-1] for _, v in sorted(stacks.items()))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
