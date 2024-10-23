from solution import load_data, position, position_with_aim, solution_01, solution_02

import pytest

TEST_PATH = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]


def test_load_data():
    assert load_data("test.data") == TEST_PATH


def test_position():
    assert position(TEST_PATH) == (15, 10)


def test_position_with_aim():
    assert position_with_aim(TEST_PATH) == (15, 60)


@pytest.mark.parametrize(
    "data_source,expected_position",
    [
        ("test.data", 150),
        ("input.data", 1813801),
    ],
)
def test_solution_01(data_source, expected_position):
    assert solution_01(data_source) == expected_position


@pytest.mark.parametrize(
    "data_source,expected_position",
    [
        ("test.data", 900),
        ("input.data", 1960569556),
    ],
)
def test_solution_02(data_source, expected_position):
    assert solution_02(data_source) == expected_position
