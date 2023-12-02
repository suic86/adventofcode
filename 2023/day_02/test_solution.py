import pytest

from solution import parse_game, solution_01, solution_02


def test_parse_line():
    assert parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        "id": 1,
        "blue": 6,
        "red": 4,
        "green": 2,
    }


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 8),
        ("input.data", 2265),
    ],
)
def test_solution_01(path, expected):
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 2286),
        ("input.data", 64097),
    ],
)
def test_solution_02(path, expected):
    assert solution_02(path) == expected
