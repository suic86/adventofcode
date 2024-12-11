from functools import cache


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().strip().split()))


@cache
def blink(stone, count):
    if count == 0:
        return 1
    count -= 1
    if stone == 0:
        return blink(1, count)
    if len(s := str(stone)) % 2 == 1:
        return blink(stone * 2024, count)
    else:
        l = len(s) // 2
        return blink(int(s[:l]), count) + blink(int(s[l:]), count)


def solution_01(path="input.data"):
    return sum(blink(stone, 25) for stone in parse_data(path))


def solution_02(path="input.data"):
    return sum(blink(stone, 75) for stone in parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
