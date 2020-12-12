import pytest
from solution import parse_action, solution_01, solution_02


@pytest.mark.parametrize(
    "instruction,action",
    [
        ("F10", ("F", 10)),
        ("N3", ("N", 3)),
        ("F7", ("F", 7)),
        ("R90", ("R", 90)),
        ("F11", ("F", 11)),
    ],
)
def test_parse_action(instruction, action):
    assert parse_action(instruction) == action


@pytest.mark.parametrize(
    "source_file,expected", [("test_solution_01.data", 25), ("input.data", 1687)]
)
def test_solution_01(source_file, expected):
    assert solution_01(source_file) == expected


@pytest.mark.parametrize(
    "source_file,expected", [("test_solution_01.data", 286), ("input.data", 20873)]
)
def test_solution_02(source_file, expected):
    assert solution_02(source_file) == expected
