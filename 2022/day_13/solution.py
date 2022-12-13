from functools import cmp_to_key
from itertools import zip_longest


def parse_data(path="input.data", part_02=False):
    with open(path) as fobj:
        if part_02:
            return [eval(line) for line in map(str.strip, fobj) if line != ""]
        return [
            tuple(map(eval, pair.split("\n")))
            for pair in fobj.read().strip().split("\n\n")
        ]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    for l, r in zip_longest(left, right):
        # left side is run out of items
        if l is None:
            return -1
        # right side is run out of items
        if r is None:
            return 1

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            elif l > r:
                return 1

        if isinstance(l, int):
            l = [l]
        elif isinstance(r, int):
            r = [r]

        if isinstance(l, list) and isinstance(r, list):
            res = compare(l, r)
            if res != 0:
                return res
    return 0


def solution_01(path="input.data"):
    return sum(i for i, p in enumerate(parse_data(path), start=1) if compare(*p) == -1)


def solution_02(path="input.data"):
    sorted_packets = sorted(
        parse_data(path, part_02=True) + [[[2]], [[6]]], key=cmp_to_key(compare)
    )
    decoder_key = 1
    for i, packet in enumerate(sorted_packets, start=1):
        if packet in ([[2]], [[6]]):
            decoder_key *= i
    return decoder_key


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 01: {solution_01()}")
