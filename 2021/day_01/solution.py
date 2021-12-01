def parse_data(path="input.data"):
    with open(path) as fobj:
        return [int(row) for row in fobj]


def depth_measurement_increases(measurements):
    return sum(map(int.__lt__, measurements, measurements[1:]))


def window_sums(measurements, window_size=3):
    return [
        sum(window) for window in zip(*(measurements[i:] for i in range(window_size)))
    ]


def solution_01(path="input.data"):
    return depth_measurement_increases(parse_data(path))


def solution_02(path="input.data"):
    return depth_measurement_increases(window_sums(parse_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
