import pytest
from solution import fuel, solution_01, total_fuel


def test_solution_01():
    assert solution_01() == 3159380


@pytest.mark.parametrize(
    "module,fuel_weight", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_fuel(module, fuel_weight):
    assert fuel(module) == fuel_weight


@pytest.mark.parametrize("module,fuel", [(14, 2), (1969, 966), (100756, 50346)])
def test_total_fuel(module, fuel):
    assert total_fuel(module) == fuel
