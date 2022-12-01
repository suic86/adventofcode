def parse_data(path="input.data"):
    with open(path) as fobj:
        return [
            [int(calories.strip()) for calories in elf.split()]
            for elf in fobj.read().split("\n\n")
        ]


def solution_01(path="input.data"):
    return max(map(sum, parse_data(path)))


def solution_02(path="input.data"):
    return sum(sorted(map(sum, parse_data(path)))[-3:])


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
