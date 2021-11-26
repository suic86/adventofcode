import pytest


from solution import (
    redistribute,
    steps_to_infinite_loop,
    cycles_between_same_states,
    solution_01,
    solution_02,
)


@pytest.mark.parametrize(
    "before,after",
    [
        ([0, 2, 7, 0], [2, 4, 1, 2]),
        ([2, 4, 1, 2], [3, 1, 2, 3]),
        ([3, 1, 2, 3], [0, 2, 3, 4]),
        ([0, 2, 3, 4], [1, 3, 4, 1]),
        ([1, 3, 4, 1], [2, 4, 1, 2]),
    ],
)
def test_redistribute(before, after):
    assert redistribute(before) == after


def test_steps_to_infinite_loop():
    assert steps_to_infinite_loop([0, 2, 7, 0]) == 5


def test_cycles_between_same_states():
    assert cycles_between_same_states([0, 2, 7, 0]) == 4


def test_solution_01():
    assert solution_01() == 12841


def test_solution_02():
    assert solution_02() == 8038
