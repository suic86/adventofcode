from solution import solution_01, solution_02, is_valid, parse_data
from functools import cache

import pytest


@cache
def ordering():
    return parse_data("test.data")[0]


@pytest.mark.parametrize(
    "update,valid",
    [
        ([75, 47, 61, 53, 29], True),
        ([97, 61, 53, 29, 13], True),
        ([75, 29, 13], True),
        ([75, 97, 47, 61, 53], False),
        ([61, 13, 29], False),
        ([97, 13, 75, 29, 47], False),
    ],
)
def test_is_valid(update: list[int], valid: bool) -> None:
    assert is_valid(update, ordering()) == valid


@pytest.mark.parametrize(
    "path,expected",
    [("test.data", 143), ("input.data", 6242)],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 0),
        ("input.data", 0),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
