import pytest
from solution import depth_measurement_increases, solution_01, solution_02

MEASUREMENTS = [
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


@pytest.mark.parametrize("windows_size,expected", [(1, 7), (3, 5)])
def test_depth_measurement_increases(windows_size, expected):
    assert depth_measurement_increases(MEASUREMENTS, windows_size) == expected


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
