from re import compile

PARSER = compile(r"\d+")


def load_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, PARSER.findall(row))) for row in fobj]


def calculate_checksum(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)


def evenly_divisible_result(row):
    row = sorted(row)
    for i, d in enumerate(row[:-1]):
        for e in row[i + 1 :]:
            if e % d == 0:
                return e // d
    raise ValueError(f"The row does not contain evenly divisible numbers: {row}.")


def solution_01():
    return calculate_checksum(load_data())


def solution_02():
    return sum(map(evenly_divisible_result, load_data()))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
