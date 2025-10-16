import pytest
from solution import first_time_basement, floor, solution_01, solution_02


@pytest.mark.parametrize(
    "moves,result",
    [
        ("(())", 0),
        ("(((", 3),
        ("))(((((", 3),
        ("())", -1),
        (")))", -3),
    ],
)
def test_moves(moves, result):
    assert floor(moves) == result


@pytest.mark.parametrize(
    "moves,result",
    [
        ("())", 3),
        ("()()())", 7),
    ],
)
def test_first_time_basement(moves, result):
    assert first_time_basement(moves) == result


def test_solution_01():
    assert solution_01() == 280


def test_solution_02():
    assert solution_02() == 1797
