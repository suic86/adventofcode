import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,shortest_n,top_n,expected",
    [
        ("test.data", 10, 3, 40),
        ("input.data", 1000, 3, 121770),
    ],
)
def test_solution_01(path, shortest_n, top_n, expected):
    assert solution_01(path, shortest_n, top_n) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 25272),
        ("input.data", 7893123992),
    ],
)
def test_solution_02(path, expected):
    assert solution_02(path) == expected
