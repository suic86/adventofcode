import pytest

from solution import load_data, solution_01, solution_02


@pytest.fixture
def testdata():
    # fmt: off
    return [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
    # fmt: on


def test_load_data(testdata):
    assert load_data("test.data") == testdata


@pytest.mark.parametrize(
    "source_data,total_flashes", [("test.data", 1656), ("input.data", 1681)]
)
def test_solution_01(source_data, total_flashes):
    assert solution_01(source_data) == total_flashes


@pytest.mark.parametrize(
    "source_data,first_synchronized_flash", [("test.data", 195), ("input.data", 276)]
)
def test_solution_02(source_data, first_synchronized_flash):
    assert solution_02(source_data) == first_synchronized_flash
