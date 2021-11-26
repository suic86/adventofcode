from solution import steps_to_escape, solution_01, solution_02

import pytest


def test_steps_to_escape():
    assert steps_to_escape([0, 3, 0, 1, -3]) == 5


def test_steps_to_escape_second_part():
    assert steps_to_escape([0, 3, 0, 1, -3], second_part=True) == 10


def test_solution_01():
    assert solution_01() == 356945


@pytest.mark.slow
def test_solution_02():
    assert solution_02() == 28372145
