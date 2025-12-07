import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 21),
        ("input.data", 1490),
    ],
)
def test_solution_01(path: str, expected: int):
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 40),
        ("input.data", 3806264447357),
    ],
)
def test_solution_02(path: str, expected: int):
    assert solution_02(path) == expected
