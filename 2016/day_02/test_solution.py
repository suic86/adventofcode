import pytest

from solution import decode_alnum_code, decode_digit, solution_01, solution_02


@pytest.mark.parametrize(
    "instruction,starting_position,digit,new_position",
    [
        ("ULL", (1, 1), "1", (0, 0)),
        ("RRDDD", (0, 0), "9", (2, 2)),
        ("LURDL", (2, 2), "8", (1, 2)),
        ("UUUUD", (1, 2), "5", (1, 1)),
    ],
)
def test_decode_digit(instruction, starting_position, digit, new_position):
    assert decode_digit(instruction, starting_position) == (digit, new_position)


@pytest.mark.parametrize(
    "instruction,starting_position,digit,new_position",
    [
        ("ULL", (0, 2), "5", (0, 2)),
        ("RRDDD", (0, 2), "D", (2, 4)),
        ("LURDL", (2, 4), "B", (2, 3)),
        ("UUUUD", (2, 3), "3", (2, 1)),
    ],
)
def test_decode_alnum_code(instruction, starting_position, digit, new_position):
    assert decode_alnum_code(instruction, starting_position) == (digit, new_position)


def test_solution_01():
    assert solution_01() == 48584


def test_solution_02():
    assert solution_02() == "563B6"
