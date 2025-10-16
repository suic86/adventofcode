import pytest
from solution import load_data, scaled_grid_value, solution_01, solution_02


@pytest.fixture
def testdata():
    # fmt: off
    return [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
    ]
    # fmt: on


@pytest.fixture
def largetestdata():
    with open("large_test.data") as fobj:
        return [[int(c) for c in r] for r in map(str.strip, fobj)]


def test_load_data(testdata):
    assert load_data("test.data") == testdata


def test_scaled_grid_value(testdata, largetestdata):
    for i in range(len(largetestdata)):
        for j in range(len(largetestdata[0])):
            assert scaled_grid_value(testdata, i, j) == largetestdata[i][j]


@pytest.mark.parametrize("source_data,risk", [("test.data", 40), ("input.data", 388)])
def test_solution_01_test_data(source_data, risk):
    assert solution_01(source_data) == risk


@pytest.mark.parametrize("source_data,risk", [("test.data", 315), ("input.data", 2819)])
def test_solution_02(source_data, risk):
    assert solution_02(source_data) == risk
