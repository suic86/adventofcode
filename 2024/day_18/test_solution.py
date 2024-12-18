import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,size,expected",
    [
        ("test.data", 12, 22),
        ("input.data", 1024, 326),
    ],
)
def test_solution_01(path, size, expected) -> None:
    assert solution_01(path, size) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", (6, 1)),
        ("input.data", (18, 62)),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
