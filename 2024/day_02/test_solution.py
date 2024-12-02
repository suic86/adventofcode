from solution import solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 2),
        ("input.data", 510),
    ],
)
def test_solution_01(inp, exp):
    assert solution_01(inp) == exp


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 4),
        ("input.data", 553),
    ],
)
def test_solution_02(inp, exp):
    assert solution_02(inp) == exp
