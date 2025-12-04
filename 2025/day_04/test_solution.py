import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize("path,expected", [("test.data", 13), ("input.data", 1533)])
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize("path,expected", [("test.data", 43), ("input.data", 9206)])
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
