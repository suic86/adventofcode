#!/usr/bin/env python3
def parse_data(path):
    with open(path) as f:
        return list(map(str.rstrip, f))


def gen(size):
    while True:
        for i in range(size):
            yield i


def s_gen(size, step):
    g = gen(size)
    while True:
        yield next(g)
        for _ in range(step - 1):
            next(g)


def traverse(data, right_step, down_step):
    size = len(data[0])
    for i, r in zip(s_gen(size=size, step=right_step), data[::down_step]):
        yield r[i]


def count_trees(data, right_step, down_step):
    is_tree = "#".__eq__
    return sum(map(is_tree, traverse(data, right_step, down_step)))


def solution_01(path):
    return count_trees(parse_data(path), right_step=3, down_step=1)


def solution_02(path):
    result = 1
    data = parse_data(path)
    for right_step, down_step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= count_trees(data, right_step, down_step)
    return result


if __name__ == "__main__":
    print(solution_01("input.data"))
    print(solution_02("input.data"))
