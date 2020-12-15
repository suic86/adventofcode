import pytest

from itertools import islice
from solution import gen_solution, solution_01


def test_solution_01_gen():
    result = [
        0,
        3,
        6,
        0,
        3,
        3,
        1,
        0,
        4,
        0,
        2,
        0,
        2,
        2,
        1,
        8,
    ]
    assert list(islice(gen_solution([0, 3, 6]), 16)) == result


@pytest.mark.parametrize(
    "init,expected",
    [
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_solution_01_test_data(init, expected):
    assert solution_01(init) == expected


def test_solution_01_input_data():
    assert solution_01() == 929


@pytest.mark.slow
@pytest.mark.parametrize(
    "init,expected",
    [
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([2, 1, 3], 3544142),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ],
)
def test_solution_02_test_data(init, expected):
    assert solution_01(init) == expected


@pytest.mark.slow
def test_solution_02_input_data():
    assert solution_02() == 16671510
