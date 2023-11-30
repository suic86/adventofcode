import pytest

from solution import (
    LBOUND,
    UBOUND,
    check_part_01,
    check_part_02,
    solution_01,
    solution_02,
)


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("111111", True),
        ("223450", False),
        ("123789", False),
    ],
)
def test_check_part_01(inp: str, exp: bool) -> None:
    assert check_part_01(inp) == exp


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("112233", True),
        ("123444", False),
        ("111122", True),
    ],
)
def test_check_part_02(inp: str, exp: bool) -> None:
    assert check_part_02(inp) == exp


def test_solution_01() -> None:
    assert solution_01(lbound=LBOUND, ubound=UBOUND) == 1790


def test_solution_02() -> None:
    assert solution_02(lbound=LBOUND, ubound=UBOUND) == 1790
