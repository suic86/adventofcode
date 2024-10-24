from solution import parse_data, solution_01, solution_02, total_length

import pytest

# Expanded
# [
#     "....#........",
#     ".........#...",
#     "#............",
#     ".............",
#     ".............",
#     "........#....",
#     ".#...........",
#     "............#",
#     ".............",
#     ".............",
#     ".........#...",
#     "#....#.......",
# ]


@pytest.mark.parametrize(
    "galaxy",
    [(4, 0), (9, 1), (0, 2), (8, 5), (1, 6), (12, 7), (9, 10), (0, 11), (5, 11)],
)
def test_parse_data(galaxy: tuple[int, int]) -> None:
    assert galaxy in parse_data("test.data")


@pytest.mark.parametrize(
    "path,total_length", [("test.data", 374), ("input.data", 9723824)]
)
def test_solution_01(path, total_length) -> None:
    assert solution_01(path) == total_length


@pytest.mark.parametrize("expansion_factor,expected_length", [(10, 1030), (100, 8410)])
def test_total_length_expansion_factor(
    expansion_factor: int, expected_length: int
) -> None:
    assert total_length("test.data", expansion_factor) == expected_length


@pytest.mark.parametrize("path,total_length", [("input.data", 731244261352)])
def test_solution_02(path, total_length) -> None:
    assert solution_02(path) == total_length
