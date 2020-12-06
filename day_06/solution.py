#!/usr/bin/env python3
from functools import reduce


def read_data(path="input.data"):
    data = []
    with open(path) as fobj:
        group = []
        for row in map(str.rstrip, fobj):
            if row:
                group.append(row)
                continue
            data.append(group)
            group = []
        if group:
            data.append(group)
    return data


def solution_01():
    # return sum(len(reduce(set.union, map(set, group))) for group in read_data())
    return sum(len(set().union(*group)) for group in read_data())


def solution_02():
    return sum(len(reduce(set.intersection, map(set, group))) for group in read_data())


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
