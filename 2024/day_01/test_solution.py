from solution import solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 11),
        ("input.data", 2192892),
    ],
)
def test_solution_01(inp: str, exp: int) -> None:
    assert solution_01(inp) == exp


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 31),
        ("input.data", 22962826),
    ],
)
def test_solution_02(inp: str, exp: int) -> None:
    assert solution_02(inp) == exp
