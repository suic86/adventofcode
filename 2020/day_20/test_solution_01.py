import pytest
from solution import (
    is_match,
    matching_tiles,
    read_data,
    solution_01,
)
from test_solution_data import (
    MATCHING_TILES,
    PARSED_TILES,
)


def test_read_data():
    assert read_data("test_solution_01.data") == PARSED_TILES


@pytest.mark.parametrize(
    "first,second,match",
    [
        ("..##.#..#.", "..##.#..#.", True),
        ("..##.#..#.", ".#..#.##..", True),
        ("...#.#..#.", ".#..#.##..", False),
        ("##########", "..........", False),
    ],
)
def test_is_match(first, second, match):
    assert is_match(first, second) == match


def test_matching_tiles():
    result = matching_tiles(PARSED_TILES)
    assert result == MATCHING_TILES
    assert sum(len(v) == 2 for v in result.values()) == 4


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_01.data", 20899048083289), ("input.data", 30425930368573)],
)
def test_solution_01(source, result):
    assert solution_01(source) == result
