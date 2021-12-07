from statistics import median


def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().strip().split(",")))


def sum_of_arithmetic_series(n):
    return (n * (n + 1)) // 2


def solution_01(path="input.data"):
    crabs = load_data(path)
    optimal_position = median(crabs)
    return sum(abs(crab - optimal_position) for crab in crabs)


def solution_02(path="input.data"):
    crabs = load_data(path)
    return min(
        sum(sum_of_arithmetic_series(abs(crab - position)) for crab in crabs)
        for position in range(min(crabs), max(crabs) + 1)
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
