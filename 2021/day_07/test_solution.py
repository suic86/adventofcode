import pytest
from solution import load_data, solution_01, solution_02


@pytest.fixture
def initial_state():
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_load_data(initial_state):
    assert load_data("test.data") == initial_state


@pytest.mark.parametrize(
    "source_data, fuel",
    [("test.data", 37), ("input.data", 326132)],
)
def test_solution_01(source_data, fuel):
    assert solution_01(source_data) == fuel


@pytest.mark.parametrize(
    "source_data, fuel",
    [("test.data", 168), ("input.data", 88612508)],
)
def test_solution_02(source_data, fuel):
    assert solution_02(source_data) == fuel
