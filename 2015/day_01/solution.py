def floor(moves):
    return moves.count("(") - moves.count(")")


def first_time_basement(moves):
    floor = 0
    for i, m in enumerate(moves, start=1):
        floor = floor + (1 if m == "(" else -1)
        if floor == -1:
            return i
    raise ValueError("Invalid input. Floor not found.")


def solution_01(path="input.data"):
    with open(path) as fobj:
        return floor(fobj.read())


def solution_02(path="input.data"):
    with open(path) as fobj:
        return first_time_basement(fobj.read())


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 01:", solution_02())
