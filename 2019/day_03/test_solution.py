import pytest
from solution import parse_row, parse_wires, solution_01, solution_02


@pytest.mark.parametrize(
    "row,parsed",
    [
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            [
                ("R", 75),
                ("D", 30),
                ("R", 83),
                ("U", 83),
                ("L", 12),
                ("D", 49),
                ("R", 71),
                ("U", 7),
                ("L", 72),
            ],
        )
    ],
)
def test_parse_data(row: str, parsed: list[tuple[str, int]]) -> None:
    assert parse_row(row) == parsed


def test_parse_wires() -> None:
    expected = (
        {
            (1, 0): 1,
            (2, 0): 2,
            (3, 0): 3,
            (4, 0): 4,
            (5, 0): 5,
            (6, 0): 6,
            (7, 0): 7,
            (8, 0): 8,
            (8, -1): 9,
            (8, -2): 10,
            (8, -3): 11,
            (8, -4): 12,
            (8, -5): 13,
            (7, -5): 14,
            (6, -5): 15,
            (5, -5): 16,
            (4, -5): 17,
            (3, -5): 18,
            (3, -4): 19,
            (3, -3): 20,
            (3, -2): 21,
        },
        {
            (0, -1): 1,
            (0, -2): 2,
            (0, -3): 3,
            (0, -4): 4,
            (0, -5): 5,
            (0, -6): 6,
            (0, -7): 7,
            (1, -7): 8,
            (2, -7): 9,
            (3, -7): 10,
            (4, -7): 11,
            (5, -7): 12,
            (6, -7): 13,
            (6, -6): 14,
            (6, -5): 15,
            (6, -4): 16,
            (6, -3): 17,
            (5, -3): 18,
            (4, -3): 19,
            (3, -3): 20,
            (2, -3): 21,
        },
    )
    assert parse_wires("test_small.data") == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_small.data", 6),
        ("test_01.data", 159),
        ("test_02.data", 135),
        ("input.data", 1264),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_small.data", 30),
        ("test_01.data", 610),
        ("test_02.data", 410),
        ("input.data", 37390),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
