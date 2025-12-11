import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 5),
        ("input.data", 796),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_02.data", 2),
        ("input.data", -1),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
