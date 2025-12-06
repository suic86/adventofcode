from math import prod
from typing import Sequence


def parse_data(
    path: str = "input.data", righttoleft: bool = False
) -> tuple[list[str], list[list[int]]]:
    with open(path) as fp:
        *numbers, operators = fp

    # identifies column boundaries by operators
    column_widths = [i for i, o in enumerate(operators) if o in "+*"]
    column_widths.append(len(operators))
    operators = operators.split()

    assert (
        len(operators) == len(column_widths) - 1
    ), f"Invalid operators: {', '.join(op for op in operators if op not in '+*')}"

    # split numbers into columns and transpose
    numbers = zip(
        *(
            [ns[i : j - 1] for i, j in zip(column_widths, column_widths[1:])]
            for ns in numbers
        )
    )

    # parse numbers
    if righttoleft:
        numbers = [[int("".join(n)) for n in zip(*column)][::-1] for column in numbers]
    else:
        # top to bottom
        numbers = [list(map(int, column)) for column in numbers]

    return operators, numbers


def evaluate(operators: list[str], numbers: Sequence) -> int:
    result = 0
    for op, nums in zip(operators, numbers):
        if op == "+":
            result += sum(nums)
        elif op == "*":
            result += prod(nums)
        else:
            raise ValueError(f"Invalid operation: '{op}'.")
    return result


def solution_01(path: str = "input.data") -> int:
    return evaluate(*parse_data(path, righttoleft=False))


def solution_02(path: str = "input.data") -> int:
    return evaluate(*parse_data(path, righttoleft=True))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
