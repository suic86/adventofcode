import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 55312),
        ("input.data", 224529),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 65601038650482),
        ("input.data", 266820198587914),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
