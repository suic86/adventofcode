#!/usr/bin/env python3
from collections import deque


def read_data(path="input.data"):
    with open(path) as source_file:
        return list(map(int, map(str.rstrip, source_file)))


def contains_sum(data, given_sum):
    return any((given_sum - e) in data[i + 1 :] for i, e in enumerate(data))


def first_non_matching(data, preamble_size=25):
    return next(
        number
        for i, number in enumerate(data[preamble_size:])
        if not contains_sum(data[i : preamble_size + i], number)
    )


def subarray_with_given_sum(array, given_sum):
    subarray = deque()
    current_sum = 0
    for i in array:
        current_sum += i
        subarray.append(i)
        if current_sum > given_sum:
            while current_sum > given_sum and subarray:
                current_sum -= subarray.popleft()
                if current_sum == given_sum:
                    break
        if current_sum == given_sum:
            return list(subarray)
    return []


def solution_01(path="input.data"):
    return first_non_matching(read_data(path))


def solution_02(path="input.data"):
    data = read_data(path)
    subarray = subarray_with_given_sum(data, first_non_matching(data))
    return min(subarray) + max(subarray)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02", solution_02())
