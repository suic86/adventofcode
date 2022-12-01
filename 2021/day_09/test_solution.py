import pytest

from solution import basin_sizes, load_data, low_points, solution_01, solution_02


@pytest.fixture
def testdata():
    return [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_load_data(testdata):
    assert load_data("test.data") == testdata


def test_basin_sizes(testdata):
    assert basin_sizes(testdata) == [3, 9, 14, 9]


def test_low_points(testdata):
    assert low_points(testdata) == [[(0, 1), 1], [(0, 9), 0], [(2, 2), 5], [(4, 6), 5]]


@pytest.mark.parametrize(
    "source_data,risk_level_sum", [("test.data", 15), ("input.data", 480)]
)
def test_solution_01(source_data, risk_level_sum):
    assert solution_01(source_data) == risk_level_sum


@pytest.mark.parametrize(
    "source_data,basin_size_product", [("test.data", 1134), ("input.data", 1045660)]
)
def test_solution_02(source_data, basin_size_product):
    assert solution_02(source_data) == basin_size_product
