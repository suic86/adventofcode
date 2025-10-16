import pytest
from solution import calculate_distance, calculate_points, solution_01, solution_02


@pytest.mark.parametrize(
    "speed,fly,rest,time,expected",
    [
        (14, 10, 127, 10, 140),
        (16, 11, 162, 10, 160),
        (14, 10, 127, 1000, 1120),
        (16, 11, 162, 1000, 1056),
    ],
)
def test_calculate_distance(speed, fly, rest, time, expected):
    assert calculate_distance(speed, fly, rest, time) == expected


def test_calculate_points():
    reindeers = [(14, 10, 127), (16, 11, 162)]
    assert calculate_points(reindeers, 1000) == 689


def test_solution_01():
    assert solution_01() == 2696


def test_solution_02():
    assert solution_02() == 1084
