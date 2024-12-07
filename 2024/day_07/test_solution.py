from solution import solution_01, solution_02, is_valid, parse_line, is_valid_02

import pytest


@pytest.mark.parametrize(
    "line,valid",
    [
        ("190: 10 19", True),
        ("3267: 81 40 27", True),
        ("83: 17 5", False),
        ("156: 15 6", False),
        ("7290: 6 8 6 15", False),
        ("161011: 16 10 13", False),
        ("192: 17 8 14", False),
        ("21037: 9 7 18 13", False),
        ("292: 11 6 16 20", True),
    ],
)
def test_is_valid(line, valid):
    assert is_valid(*parse_line(line)) == valid


@pytest.mark.parametrize(
    "line,valid",
    [
        ("1351: 2 597 1 78 78 1", True),
        ("581225299324: 81 75 1 2 91 876 6 1 24", True),
        ("885836: 8 850 4 5 2 27 704 58 9", False),
        ("3333672: 9 76 9 6 8 9 1 1 8 8 1 9", False),
        ("2048596: 560 8 8 64 3 9 2 2 5 41 2", False),
        ("34492227: 9 7 993 77 7 3", False),
    ],
)
def test_is_valid_02(line, valid):
    assert is_valid_02(*parse_line(line)) == valid


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 3749),
        ("input.data", 3119088655389),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


# @pytest.mark.skip
@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 11387),
        ("input.data", 264184041398847),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
