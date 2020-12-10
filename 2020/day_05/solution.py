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
        return list(fobj)


def seats(path="input.data"):
    return map(seat, read_data(path))


def solution_01():
    return max(seats())


def solution_02():
    return missing_seat(seats())


if __name__ == "__main__":
    print(solution_01())
    print(solution_02())
