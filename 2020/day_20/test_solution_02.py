import pytest

from test_solution_data import (
    ASSEMBLED_TILES,
    IMAGE,
    IMAGE_WITH_MONSTERS,
    PARSED_TILES,
)

from solution import (
    assemble_image,
    count_monsters,
    trim_borders,
)


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


def test_count_monsters():
    assert count_monsters(IMAGE_WITH_MONSTERS) == 2


@pytest.mark.skip
def test_assemble_image():
    assert assemble_image(ASSEMBLED_TILES, PARSED_TILES) == IMAGE
