def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.split, fobj))


def first_part(round):
    values = {"X": 1, "Y": 2, "Z": 3}
    op, me = round
    val = values[me]
    if round in [["A", "X"], ["B", "Y"], ["C", "Z"]]:
        return val + 3
    if round in [["A", "Z"], ["B", "X"], ["C", "Y"]]:
        return val
    else:
        return val + 6


def second_part(round):
    outcomes = {"X": 0, "Y": 3, "Z": 6}
    values = {"X": 1, "Y": 2, "Z": 3}
    op, me = round
    return (
        outcomes[me]
        + values[
            {
                "X": {"A": "Z", "B": "X", "C": "Y"},  # lose
                "Y": {"A": "X", "B": "Y", "C": "Z"},  # draw
                "Z": {"A": "Y", "B": "Z", "C": "X"},  # win
            }[me][op]
        ]
    )


def total_score(strategy, compute_score):
    return sum(map(compute_score, strategy))


def solution_01(path="input.data"):
    return total_score(parse_data(path), first_part)


def solution_02(path="input.data"):
    return total_score(parse_data(path), second_part)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
