import pytest
from solution import (
    Tile,
    assemble_image,
    count_monsters,
    is_match,
    matching_tiles,
    read_data,
    solution_01,
    trim_borders,
)
from test_solution_data import MATCHING_TILES, PARSED_TILES, ASSEMBLED_TILES, IMAGE, IMAGE_WITH_MONSTERS


def test_read_data():
    assert read_data("test_solution_01.data") == PARSED_TILES


def test_tile():
    tile_id = 2311
    tile_data = PARSED_TILES[tile_id]
    tile = Tile(tile_id, tile_data)
    assert tile.top == "..##.#..#."
    assert tile.bottom == "..###..###"
    assert tile.left == ".#####..#."
    assert tile.right == "...#.##..#"
    assert tile.borders == ["..##.#..#.", ".#####..#.", "..###..###", "...#.##..#"]


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


@pytest.mark.parametrize(
    "first,second,match",
    [
        (1951, 2729, True),
        (1951, 2311, True),
        (1951, 1427, False),
        (1951, 1171, False),
        (1427, 2311, True),
        (1427, 2729, True),
        (1427, 2473, True),
        (1427, 1489, True),
        (1427, 1171, False),
    ],
)
def test_tile_match_any_border(first, second, match):
    first = Tile(first, PARSED_TILES[first])
    second = Tile(second, PARSED_TILES[second])
    assert first.match_any_border(second) == match
    assert second.match_any_border(first) == match


"""
1951    2311    3079
2729    1427    2473
2971    1489    1171
"""


def test_matching_tiles():
    result = matching_tiles(PARSED_TILES)
    assert result == MATCHING_TILES
    assert sum(len(v) == 2 for v in result.values()) == 4


@pytest.mark.parametrize("source,result", [("test_solution_01.data", 20899048083289)])
def test_solution_01(source, result):
    assert solution_01(source) == result


def test_trim_borders():
    tile_data = [
        "#.##...##.",
        "#.####...#",
        ".....#..##",
        "#...######",
        ".##.#....#",
        ".###.#####",
        "###.##.##.",
        ".###....#.",
        "..#.#..#.#",
        "#...##.#..",
    ]
    trimmed = [
        ".####...",
        "....#..#",
        "...#####",
        "##.#....",
        "###.####",
        "##.##.##",
        "###....#",
        ".#.#..#.",
    ]
    assert trim_borders(tile_data) == trimmed


@pytest.mark.skip
def test_assemble_image():
    assert assemble_image(ASSEMBLED_TILES, PARSED_TILES) == IMAGE


def test_count_monsters():
    assert count_monsters(IMAGE_WITH_MONSTERS) == 2
