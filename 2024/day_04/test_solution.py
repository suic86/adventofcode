import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize("path,expected", [("test.data", 18), ("input.data", 2414)])
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize("path,expected", [("test.data", 9), ("input.data", 1871)])
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
