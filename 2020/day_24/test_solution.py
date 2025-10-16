import pytest
from solution import (
    PARSER,
    input_to_tiles,
    next_day,
    solution_01,
    solution_02,
    steps_to_tile,
)


@pytest.mark.parametrize(
    "input,parsed",
    [
        ("esenee", ["e", "se", "ne", "e"]),
        (
            "sesenwnenenewseeswwswswwnenewsewsw",
            [
                "se",
                "se",
                "nw",
                "ne",
                "ne",
                "ne",
                "w",
                "se",
                "e",
                "sw",
                "w",
                "sw",
                "sw",
                "w",
                "ne",
                "ne",
                "w",
                "se",
                "w",
                "sw",
            ],
        ),
    ],
)
def test_parser(input, parsed):
    assert PARSER(input) == parsed


def test_steps_to_tile():
    assert steps_to_tile(PARSER("nwwswee")) == (0, 0)


def test_next_day():
    tiles = input_to_tiles("test_solution_01.data")
    assert len(tiles) == 10
    tiles = next_day(tiles)
    assert len(tiles) == 15
    tiles = next_day(tiles)
    assert len(tiles) == 12
    tiles = next_day(tiles)
    assert len(tiles) == 25


@pytest.mark.parametrize(
    "source,result", [("test_solution_01.data", 10), ("input.data", 330)]
)
def test_solution_01(source, result):
    assert solution_01(source) == result


@pytest.mark.slow
@pytest.mark.parametrize(
    "source,result", [("test_solution_01.data", 2208), ("input.data", 3711)]
)
def test_solution_02(source, result):
    assert solution_02(source) == result
