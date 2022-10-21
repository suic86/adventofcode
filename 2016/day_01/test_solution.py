import pytest

from solution import (calculate_distance, first_visited_twice, solution_01,
                      solution_02)


@pytest.mark.parametrize(
    "inp,exp",
    [
        (["R2", "L3"], 5),
        (["R2", "R2", "R2"], 2),
        (["R5", "L5", "R5", "R3"], 12),
    ],
)
def test_calculate_distance(inp, exp):
    assert calculate_distance(inp) == exp


def test_first_visited_twice():
    assert first_visited_twice(["R8", "R4", "R4", "R8"]) == (4, 0)


def test_solution_01():
    assert solution_01() == 243


def test_solution_02():
    assert solution_02() == 142
