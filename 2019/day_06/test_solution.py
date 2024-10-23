import pytest

from solution import parse_data, solution_01, solution_02

PARSED_TEST_DATA = {
    "COM": {"B"},
    "B": {"C", "G"},
    "C": {"D"},
    "D": {"E", "I"},
    "E": {"F", "J"},
    "G": {"H"},
    "J": {"K"},
    "K": {"L"},
}


def test_parse_data() -> None:
    assert parse_data("test.data") == PARSED_TEST_DATA


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 42),
        ("input.data", 130681),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path=path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_02.data", 4),
        ("input.data", 313),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path=path) == expected
