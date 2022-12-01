def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj))


def depth_measurement_increases(measurements, window_size=1):
    return sum(map(int.__lt__, measurements, measurements[window_size:]))


def solution_01(path="input.data"):
    return depth_measurement_increases(parse_data(path))


def solution_02(path="input.data"):
    return depth_measurement_increases(parse_data(path), window_size=3)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
