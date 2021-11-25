from solution import (
    calculate_checksum,
    evenly_divisible_result,
    solution_01,
    solution_02,
)

import pytest

SPREADSHEET_01 = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8],
]

SPREADSHEET_02 = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]


def test_calculate_checksum():
    assert calculate_checksum(SPREADSHEET_01) == 18


@pytest.mark.parametrize("inp,exp", list(zip(SPREADSHEET_02, (4, 3, 2))))
def test_evenly_divisible_result(inp, exp):
    assert evenly_divisible_result(inp) == exp


def test_solution_01():
    assert solution_01() == 43074


def test_solution_02():
    assert solution_02() == 280
