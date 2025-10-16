import pytest
from solution import (
    additional_copies,
    addtional_card_counts,
    parse_data,
    parse_line,
    points,
    solution_01,
    solution_02,
)


def test_parse_line() -> None:
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    parsed = {
        "id": 1,
        "wn": set(map(int, "41 48 83 86 17".split())),
        "mn": list(map(int, "83 86  6 31 17  9 48 53".split())),
    }
    assert parse_line(line) == parsed


@pytest.mark.parametrize(
    "card,value",
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
    ],
)
def test_points(card: str, value: int) -> None:
    assert points(parse_line(card)) == value


def test_additional_cards() -> None:
    cards = parse_data("test.data")
    assert additional_copies(cards) == {
        1: [2, 3, 4, 5],
        2: [3, 4],
        3: [4, 5],
        4: [5],
        5: [],
        6: [],
    }


def test_additional_card_counts() -> None:
    cards = parse_data("test.data")
    assert addtional_card_counts(cards) == {
        1: 15,
        2: 7,
        3: 4,
        4: 2,
        5: 1,
        6: 1,
    }


@pytest.mark.parametrize("path,expected", [("test.data", 13), ("input.data", 26346)])
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize("path,expected", [("test.data", 30), ("input.data", 8467762)])
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
