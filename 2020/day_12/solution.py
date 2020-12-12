#!/usr/bin/env python
from re import compile
from collections import deque


PARSER = compile(r"(?P<direction>[NSEWLRF])(?P<distance>\d+)")


def read_data(path="input.data"):
    with open(path) as source_file:
        return list(map(parse_action, source_file))


def parse_action(instruction):
    direction, distance = PARSER.fullmatch(instruction.rstrip()).groups()
    return direction, int(distance)


def solution_01(path="input.data"):
    # directions
    ds = "ESWN"
    # distances
    s = [0, 0, 0, 0]
    # direction pointer
    p = 0
    for d, v in read_data(path):
        if d in ds:
            s[ds.index(d)] += v
        elif d == "F":
            s[p] += v
        elif d == "R":
            p = (p + (v % 360) // 90) % 4
        elif d == "L":
            p = (p - (v % 360) // 90) % 4
    return abs(s[0] - s[2]) + abs(s[1] - s[3])


def solution_02(path="input.data"):
    # directions
    ds = "ESWN"
    # view point
    wp = deque([10, 0, 0, 1])
    # distances
    s = [0, 0, 0, 0]

    for d, v in read_data(path):
        if d in ds:
            wp[ds.index(d)] += v
        elif d == "R":
            wp.rotate((v % 360) // 90)
        elif d == "L":
            wp.rotate(-(v % 360) // 90)
        elif d == "F":
            s = [i + j * v for i, j in zip(s, wp)]
    return abs(s[0] - s[2]) + abs(s[1] - s[3])


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
