import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,exp",
    [("test.data", 3), ("input.data", 1026)],
)
def test_solution_01(path: str, exp: int) -> None:
    assert solution_01(path) == exp


@pytest.mark.parametrize(
    "path,exp",
    [("test.data", 6), ("input.data", 5923)],
)
def test_solution_02(path: str, exp: int) -> None:
    assert solution_02(path) == exp
