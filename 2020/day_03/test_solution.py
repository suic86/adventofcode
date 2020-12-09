import pytest
from solution import count_trees, parse_data, solution_01, solution_02


def test_solution_01():
    assert solution_01("test.data") == 7
    assert solution_01("input.data") == 151


def test_solution_02():
    assert solution_02("test.data") == 336


@pytest.mark.parametrize(
    "right_step,down_step,expected",
    [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)],
)
def test_count_trees(right_step, down_step, expected):
    test_data = parse_data("test.data")
    assert count_trees(test_data, right_step, down_step) == expected
