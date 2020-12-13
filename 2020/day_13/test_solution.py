import pytest
from solution import read_data, solution_01, solution_02


def test_read_data():
    assert read_data("test_solution_01.data") == (
        939,
        [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)],
    )


@pytest.mark.parametrize(
    "source,expected", [("test_solution_01.data", 295), ("input.data", 296)]
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.timeout(1)
def test_solution_02_test_data():
    solution = solution_02(path="test_solution_01.data")
    assert solution == 1068781


def test_solution_02_input_data():
    assert solution_02(path="input.data") == 535296695251210
