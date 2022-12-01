import pytest

from solution import parse_data, solution_01, solution_02


def test_parse_data():
    parsed = [
        [
            1000,
            2000,
            3000,
        ],
        [
            4000,
        ],
        [
            5000,
            6000,
        ],
        [
            7000,
            8000,
            9000,
        ],
        [10000],
    ]
    assert parse_data("test.data") == parsed


@pytest.mark.parametrize(
    "source,calories",
    [
        ("test.data", 24000),
        ("input.data", 69528),
    ],
)
def test_solution_01(source, calories):
    assert solution_01(source) == calories


@pytest.mark.parametrize(
    "source,calories",
    [
        ("test.data", 45000),
        ("input.data", 206152),
    ],
)
def test_solution_02(source, calories):
    assert solution_02(source) == calories
