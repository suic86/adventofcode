def parse_data(path):
    with open(path) as f:
        return list(map(str.rstrip, f))


def traverse(data, right_step, down_step):
    h_size, v_size = len(data[0]), len(data)
    h, v = 0, 0
    while v < v_size:
        yield data[v][h % h_size]
        h += right_step
        v += down_step


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
