import pytest
from solution import advent_coin, solution_01, solution_02


@pytest.mark.parametrize("key,expected", (["abcdef", 609043], ["pqrstuv", 1048970]))
def test_advent_coin(key, expected):
    assert advent_coin(key) == expected


def test_solution_01():
    assert solution_01() == 346386


@pytest.mark.slow()
def test_solution_02():
    assert solution_02() == 9958218
