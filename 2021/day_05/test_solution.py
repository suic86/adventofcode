import pytest
from solution import draw_lines, load_data, solution_01, solution_02


@pytest.fixture
def lines():
    return [
        [0, 9, 5, 9],
        [8, 0, 0, 8],
        [9, 4, 3, 4],
        [2, 2, 2, 1],
        [7, 0, 7, 4],
        [6, 4, 2, 0],
        [0, 9, 2, 9],
        [3, 4, 1, 4],
        [0, 0, 8, 8],
        [5, 5, 8, 2],
    ]


@pytest.fixture
def diagonal_diagram():
    return """1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."""


@pytest.fixture
def non_diagonal_diagram():
    return """.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111...."""


def _draw_diagram(covered):
    m = [[0] * 10 for _ in range(10)]
    for x, y in covered:
        m[x][y] = covered[(x, y)]
    return "\n".join("".join(str(c) if c else "." for c in row) for row in m)


def test_draw_lines_non_diagonal(lines, non_diagonal_diagram):
    assert _draw_diagram(draw_lines(lines, diagonals=False)) == non_diagonal_diagram


def test_draw_lines_diagonal(lines, diagonal_diagram):
    assert _draw_diagram(draw_lines(lines, diagonals=True)) == diagonal_diagram


def test_load_data(lines):
    assert load_data("test.data") == lines


@pytest.mark.parametrize("data,points_count", [("test.data", 5), ("input.data", 5576)])
def test_solution_01(data, points_count):
    assert solution_01(data) == points_count


@pytest.mark.parametrize(
    "data,points_count", [("test.data", 12), ("input.data", 18144)]
)
def test_solution_02(data, points_count):
    assert solution_02(data) == points_count
