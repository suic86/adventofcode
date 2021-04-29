from solution import look_and_say, solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, 11),
        (11, 21),
        (21, 1211),
        (1211, 111221),
        (111221, 312211),
    ],
)
def test_look_and_say(number, expected):
    assert int(look_and_say(str(number))) == expected


def test_solution_01():
    assert solution_01() == 329356


@pytest.mark.slow
def test_solution_02():
    assert solution_02() == 4666278
