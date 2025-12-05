import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 3),
        ("input.data", 874),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 14),
        ("input.data", 348548952146313),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
