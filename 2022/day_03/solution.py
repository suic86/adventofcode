from string import ascii_letters

PRIORITY = {e: i for i, e in enumerate(ascii_letters, start=1)}


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def detect_character(sack):
    length = len(sack)
    return (set(sack[: length // 2]) & set(sack[length // 2 :])).pop()


def group_sacks(sacks):
    return zip(*[iter(sacks)] * 3)


def detect_badge(group):
    return set.intersection(*map(set, group)).pop()


def solution_01(path="input.data"):
    return sum(map(PRIORITY.get, map(detect_character, parse_data(path))))


def solution_02(path="input.data"):
    return sum(map(PRIORITY.get, map(detect_badge, group_sacks(parse_data(path)))))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
