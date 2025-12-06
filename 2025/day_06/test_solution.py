import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 4277556),
        ("input.data", 5552221122013),
    ],
)
def test_solution_01(path, expected):
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 3263827),
        ("input.data", 11371597126232),
    ],
)
def test_solution_02(path, expected):
    assert solution_02(path) == expected
