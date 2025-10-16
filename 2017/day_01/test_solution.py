import pytest
from solution import load_data, solution_01, solution_02


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
        ("951484596541141557316984781494999", 1 + 5 + 27),
        (load_data(), 1341),
    ],
)
def test_solution_01(inp, exp):
    assert solution_01(inp) == exp


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
        (load_data(), 1348),
    ],
)
def test_solution_02(inp, exp):
    assert solution_02(inp) == exp
