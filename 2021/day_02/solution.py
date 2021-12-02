def load_data(path="input.data"):
    with open(path) as fobj:
        return [(direction, int(value)) for direction, value in map(str.split, fobj)]


def position(path):
    depth = 0
    horizontal = 0
    for direction, value in path:
        if direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
        elif direction == "forward":
            horizontal += value
        else:
            raise ValueError(f"Invalid direction {direction}.")
    return horizontal, depth


def position_with_aim(path):
    depth = 0
    horizontal = 0
    aim = 0
    for direction, value in path:
        if direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        elif direction == "forward":
            horizontal += value
            depth += aim * value
        else:
            raise ValueError(f"Invalid direction {direction}.")
    return horizontal, depth


def solution_01(path="input.data"):
    return int.__mul__(*position(load_data(path)))


def solution_02(path="input.data"):
    return int.__mul__(*position_with_aim(load_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
