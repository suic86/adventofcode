import pytest

from solution import houses, parse_input, solution_01, solution_02


@pytest.mark.parametrize(
    "moves,expected",
    [
        [">", [(0, 0), (1, 0)]],
        ["^>v<", [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]],
        ["^v^", [(0, 0), (0, 1), (0, 0), (0, 1)]],
    ],
)
def test_houses(moves, expected):
    assert list(houses(moves)) == expected


@pytest.mark.parametrize(
    "moves,expected",
    [
        [">", 2],
        ["^>v<", 4],
        ["^v^v^v^v^v", 2],
    ],
)
def test_solution_01_sample_input(moves, expected):
    assert solution_01(moves) == expected


@pytest.mark.parametrize(
    "moves,expected",
    [
        ["^>", 3],
        ["^>v<", 3],
        ["^v^v^v^v^v", 11],
    ],
)
def test_solution_02_sample_input(moves, expected):
    assert solution_02(moves) == expected


def test_solution_01():
    assert solution_01(parse_input()) == 2592


def test_solution_02():
    assert solution_02(parse_input()) == 2360
