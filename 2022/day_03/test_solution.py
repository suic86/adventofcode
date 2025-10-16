import pytest
from solution import detect_character, solution_01, solution_02


@pytest.mark.parametrize(
    "sack,character",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_detect_character(sack, character):
    assert detect_character(sack) == character


def test_solution_01_test_data():
    assert solution_01("test.data") == 157


def test_solution_01():
    assert solution_01() == 7863


def test_solution_02_test_data():
    assert solution_02("test.data") == 70


def test_solution_02():
    assert solution_02() == 2488
