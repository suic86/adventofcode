from solution import parse_data, solution_01, solution_02

PARSED_STACKS = {
    1: ["Z", "N"],
    2: ["M", "C", "D"],
    3: ["P"],
}

PARSED_MOVES = [
    [1, 2, 1],
    [3, 1, 3],
    [2, 2, 1],
    [1, 1, 2],
]


def test_parse_data_stacks():
    stacks, _ = parse_data("test.data")
    assert stacks == PARSED_STACKS


def test_parse_data_moves():
    _, moves = parse_data("test.data")
    assert moves == PARSED_MOVES


def test_solution_01_test_data():
    assert solution_01("test.data") == "CMZ"


def test_solution_01():
    assert solution_01() == "FCVRLMVQP"


def test_solution_02_test_data():
    assert solution_02("test.data") == "MCD"


def test_solution_02():
    assert solution_02() == "RWLWGJGFD"
