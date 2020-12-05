#!/usr/bin/env python3
from functools import reduce
from operator import xor


def convert(code, tr=str.maketrans("FBLR", "0101")):
    return int(code.translate(tr), 2)


def seat(code):
    row_code, column_code = code[:7], code[7:]
    return 8 * convert(row_code) + convert(column_code)


def missing_seat(seats):
    return reduce(xor, seats)


def read_data(path="input.data"):
    with open(path) as fobj:
        return [line.rstrip() for line in fobj]


def solution_01(path="input.data"):
    return max(map(seat, read_data(path)))


def solution_02(path="input.data"):
    return missing_seat(map(seat, read_data(path)))


if __name__ == "__main__":
    print(solution_01())
