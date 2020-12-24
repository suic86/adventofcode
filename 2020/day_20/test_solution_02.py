import pytest

from test_solution_data import (
    IMAGE_WITH_MONSTERS,
)

from solution import (
    MONSTER,
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
    assert count_monsters(IMAGE_WITH_MONSTERS, MONSTER) == 2


@pytest.fixture
def matched_tiles():
    return {
        2311: {1427, 1951, 3079},
        1951: {2311, 2729},
        1171: {1489, 2473},
        1427: {1489, 2311, 2473, 2729},
        1489: {1171, 1427, 2971},
        2473: {1171, 1427, 3079},
        2971: {1489, 2729},
        2729: {1427, 1951, 2971},
        3079: {2311, 2473},
    }
