from collections import defaultdict


def parse_data(path="input.data"):
    ordering = defaultdict(set)
    updates = []
    separator = False
    with open(path) as fobj:
        for line in map(str.strip, fobj):
            if not line:
                separator = True
                continue
            if not separator:
                x, y = map(int, line.split("|"))
                ordering[x].add(y)
            else:
                updates.append(list(map(int, line.split(","))))
    return ordering, updates


def is_valid(update: list[int], ordering: dict[int, set[int]]) -> bool:
    for i, p in enumerate(update[:-2]):
        if set(update[i + 1 :]) - ordering[p]:
            return False
    return not (set(update[:-1]) & ordering[update[-1]])


def solution_01(path="input.data"):
    ordering, updates = parse_data(path)
    total = 0
    for update in updates:
        if is_valid(update, ordering):
            total += update[len(update) // 2]
    return total


def solution_02(path="input.data"):
    return -1


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
    print(parse_data("test.data"))
