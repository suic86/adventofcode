import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 36),
        ("input.data", 778),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 81),
        ("input.data", 1925),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
