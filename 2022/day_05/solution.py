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


def top_crates(stacks):
    return "".join(v[-1] for _, v in sorted(stacks.items()))


def solution(path="input.data", reverse=True):
    stacks, moves = parse_data(path)
    for c, f, t in moves:
        stacks[t].extend(reversed(stacks[f][-c:]) if reverse else stacks[f][-c:])
        stacks[f] = stacks[f][:-c]
    return top_crates(stacks)


def solution_01(path="input.data"):
    return solution(path)


def solution_02(path="input.data"):
    return solution(path, reverse=False)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
