def read_data(path="input.data"):
    with open(path) as fobj:
        for module in fobj:
            yield module


def fuel(weight):
    return weight // 3 - 2


def total_fuel(module_weight):
    fuel_weight = fuel(module_weight)
    total = 0
    while fuel_weight > 0:
        total += fuel_weight
        fuel_weight = fuel(fuel_weight)
    return total


def solution_01(path="input.data"):
    return sum(map(fuel, map(int, read_data(path))))


def solution_02(path="input.data"):
    return sum(map(total_fuel, map(int, read_data())))


if __name__ == "__main__":
    print(solution_01())
    print(solution_02())
