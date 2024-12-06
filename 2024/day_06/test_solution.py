from solution import solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 41),
        ("input.data", 4752),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize("path,expected", [("test.data", 0), ("input.data", 0)])
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
