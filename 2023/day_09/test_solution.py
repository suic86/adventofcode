import pytest

from solution import (
    interpolate,
    interpolate_part_2,
    parse_data,
    solution_01,
    solution_02,
)


def test_parse_data() -> None:
    assert parse_data("test.data") == [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]


@pytest.mark.parametrize(
    "line,expected",
    [
        ([0, 3, 6, 9, 12, 15], 18),
        ([1, 3, 6, 10, 15, 21], 28),
        ([10, 13, 16, 21, 30, 45], 68),
    ],
)
def test_interpolate(line: list[int], expected: int) -> None:
    assert interpolate(line) == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ([10, 13, 16, 21, 30, 45], 5),
        ([0, 3, 6, 9, 12, 15], -3),
        ([1, 3, 6, 10, 15, 21], 0),
    ],
)
def test_interpolate_part2(line: list[int], expected: int) -> None:
    assert interpolate_part_2(line) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 114),
        ("input.data", 1974913025),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 2),
        ("input.data", 884),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
