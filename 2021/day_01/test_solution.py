from solution import depth_measurement_increases, solution_01, solution_02, window_sums

import pytest


def test_depth_measurement_increases():
    measurements = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    assert depth_measurement_increases(measurements) == 7


def test_window_sums():
    measurements = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    expected_sums = [
        607,
        618,
        618,
        617,
        647,
        716,
        769,
        792,
    ]
    assert window_sums(measurements) == expected_sums


@pytest.mark.parametrize(
    "source_data,expected",
    [
        ("test.data", 7),
        ("input.data", 1521),
    ],
)
def test_solution_01(source_data, expected):
    assert solution_01(source_data) == expected


@pytest.mark.parametrize(
    "source_data,expected",
    [
        ("test.data", 5),
        ("input.data", 1543),
    ],
)
def test_solution_02(source_data, expected):
    assert solution_02(source_data) == expected
