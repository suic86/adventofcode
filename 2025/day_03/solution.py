def parse_data(path="input.data") -> list[str]:
    with open(path) as fp:
        return list(map(str.strip, fp))


def max_joltage(bank: str, size: int = 2) -> int:
    to_remove = len(bank) - size
    stack = []

    for battery in bank:
        while stack and to_remove > 0 and stack[-1] < battery:
            stack.pop()
            to_remove -= 1
        stack.append(battery)

    return int("".join(stack[:size]))


def solution_01(path="input.data") -> int:
    return sum(map(max_joltage, parse_data(path)))


def solution_02(path="input.data") -> int:
    return sum(max_joltage(bank, 12) for bank in parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
