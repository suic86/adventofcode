from solution import floor, first_time_basement, solution_01, solution_02
import pytest


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
