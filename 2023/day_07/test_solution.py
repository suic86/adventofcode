import pytest

from solution import Hand, parse_data, solution_01, solution_02


def test_parse_data() -> None:
    assert parse_data("test.data") == [
        Hand("32T3K", 765),
        Hand("T55J5", 684),
        Hand("KK677", 28),
        Hand("KTJJT", 220),
        Hand("QQQJA", 483),
    ]


@pytest.mark.parametrize(
    "path,expected", [("test.data", 6440), ("input.data", 248812215)]
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected", [("test.data", 5905), ("input.data", 250057090)]
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
