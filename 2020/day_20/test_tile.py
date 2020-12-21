import pytest

from test_solution_data import PARSED_TILES
from solution import Tile


@pytest.fixture
def simple_tile():
    return Tile(0, ["123", "456", "789"])


def test_tile():
    tile_id = 2311
    tile_data = PARSED_TILES[tile_id]
    tile = Tile(tile_id, tile_data)
    assert tile.top == "..##.#..#."
    assert tile.bottom == "..###..###"
    assert tile.left == ".#####..#."
    assert tile.right == "...#.##..#"
    assert tile.borders == ["..##.#..#.", ".#####..#.", "..###..###", "...#.##..#"]


def test_tile_vertical_flip(simple_tile):
    simple_tile.vflip()
    assert simple_tile.data == ["789", "456", "123"]
    assert simple_tile.top == "789"
    assert simple_tile.bottom == "123"
    assert simple_tile.left == "741"
    assert simple_tile.right == "963"
    simple_tile.vflip()
    assert simple_tile.data == ["123", "456", "789"]


def test_tile_horizontal_flip(simple_tile):
    simple_tile.hflip()
    assert simple_tile.data == ["321", "654", "987"]
    simple_tile.hflip()
    assert simple_tile.data == ["123", "456", "789"]


def test_tile_rot180(simple_tile):
    simple_tile.rot180()
    assert simple_tile.data == ["987", "654", "321"]
    simple_tile.rot180()
    assert simple_tile.data == ["123", "456", "789"]


def test_tile_rot90(simple_tile):
    simple_tile.rot90()
    assert simple_tile.data == ["741", "852", "963"]
    assert simple_tile.top == "741"
    assert simple_tile.bottom == "963"
    assert simple_tile.left == "789"
    assert simple_tile.right == "123"


def test_tile_rot270(simple_tile):
    simple_tile.rot270()
    assert simple_tile.data == ["369", "258", "147"]
    simple_tile.rot90()
    assert simple_tile.data == ["123", "456", "789"]


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
