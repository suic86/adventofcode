import pytest
from solution import distance, solution_01, solution_02, spiral


@pytest.mark.parametrize(
    "number, expected_spiral",
    [
        (1, [(0, 0)]),
        (2, [(0, 0), (1, 0), (1, 1), (0, 1)]),
    ],
)
def test_spiral(number, expected_spiral):
    assert list(spiral(number)) == expected_spiral


@pytest.mark.parametrize(
    "number,expected_distance",
    [
        (1, 0),
        (12, 3),
        (23, 2),
        (1024, 31),
    ],
)
def test_distance(number, expected_distance):
    assert distance(number) == expected_distance


def test_solution_01():
    assert solution_01() == 419


def test_solution_02():
    assert solution_02() == 295229
