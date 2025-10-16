import pytest
from solution import convert, seat, solution_01, solution_02


@pytest.mark.parametrize(
    "code,number",
    [
        ("RLR", 5),
        ("FBFBBFF", 44),
    ],
)
def test(code, number):
    assert convert(code) == number


@pytest.mark.parametrize(
    "seat_code,seat_number",
    [
        ("FBFBBFFRLR", 357),
    ],
)
def test_seat(seat_code, seat_number):
    assert seat(seat_code) == seat_number


def test_solution_01():
    assert solution_01() == 987


def test_solution_02():
    assert solution_02() == 603
