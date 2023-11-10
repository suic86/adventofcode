from solution import parse_data, solution_01, solution_02

import pytest

PARSED_DATA = [
    (1, 1, 3, 4, 4),
    (2, 3, 1, 4, 4),
    (3, 5, 5, 2, 2),
]


def test_parse_data() -> None:
    assert parse_data("test.data") == PARSED_DATA


@pytest.mark.parametrize("source,expected", [("test.data", 4), ("input.data", 111326)])
def test_solution_01(source: str, expected: int) -> None:
    assert solution_01(path=source) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test.data", 3),
        ("input.data", 1019),
    ],
)
def test_solution_02(source: str, expected: int) -> None:
    assert solution_02(path=source) == expected
