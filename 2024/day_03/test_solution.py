import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,exp",
    [
        ("test_01.data", 161),
        ("input.data", 170807108),
    ],
)
def test_solution_01(path: str, exp: int) -> None:
    assert solution_01(path) == exp


@pytest.mark.parametrize(
    "path,exp",
    [
        ("test_02.data", 48),
        ("input.data", 74838033),
    ],
)
def test_solution_02(path: str, exp: int) -> None:
    assert solution_02(path) == exp
