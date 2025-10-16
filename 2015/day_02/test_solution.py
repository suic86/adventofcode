import pytest
from solution import ribbon, solution_01, solution_02, wrapping_paper


@pytest.mark.parametrize("sides,expected", [((2, 3, 4), 58), ((1, 1, 10), 43)])
def test_wrapping_paper(sides, expected):
    assert wrapping_paper(*sides) == expected


@pytest.mark.parametrize("sides,expected", [((2, 3, 4), 34), ((1, 1, 10), 14)])
def test_ribbon(sides, expected):
    assert ribbon(*sides) == expected


@pytest.mark.parametrize(
    "path,expected", [("test_solution.data", 101), ("input.data", 1586300)]
)
def test_solution_01(path, expected):
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected", [("test_solution.data", 48), ("input.data", 3737498)]
)
def test_solution_02(path, expected):
    assert solution_02(path) == expected
