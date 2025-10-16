from collections import Counter

import pytest
from solution import load_data, simulator, solution_01, solution_02


@pytest.fixture
def initial_state():
    return [3, 4, 3, 1, 2]


def test_load_data(initial_state):
    assert load_data("test.data") == initial_state


# fmt: off
@pytest.mark.parametrize("days,expected_state", [
    ( 1, [2, 3, 2, 0, 1]), 
    ( 2, [1, 2, 1, 6, 0, 8]), 
    ( 3, [0, 1, 0, 5, 6, 7, 8]), 
    ( 4, [6, 0, 6, 4, 5, 6, 7, 8, 8]), 
    ( 5, [5, 6, 5, 3, 4, 5, 6, 7, 7, 8]), 
    ( 6, [4, 5, 4, 2, 3, 4, 5, 6, 6, 7]), 
    ( 7, [3, 4, 3, 1, 2, 3, 4, 5, 5, 6]), 
    ( 8, [2, 3, 2, 0, 1, 2, 3, 4, 4, 5]), 
    ( 9, [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8]), 
    (10, [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]), 
    (11, [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8]), 
    (12, [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8]), 
    (13, [4, 5, 4, 2, 3, 4, 5, 6, 6, 0, 4, 5, 6, 6, 6, 7, 7, 8, 8]), 
    (14, [3, 4, 3, 1, 2, 3, 4, 5, 5, 6, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8]), 
    (15, [2, 3, 2, 0, 1, 2, 3, 4, 4, 5, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7]), 
    (16, [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 8]), 
    (17, [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8]), 
    (18, [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]), 
])
# fmt: on
def test_simulator(initial_state, days, expected_state):
    assert simulator(initial_state, days) == Counter(expected_state)


@pytest.mark.parametrize(
    "source_data, number_of_fishes", [("test.data", 5934), ("input.data", 371379)]
)
def test_solution_01(source_data, number_of_fishes):
    assert solution_01(source_data) == number_of_fishes


@pytest.mark.parametrize(
    "source_data, number_of_fishes",
    [("test.data", 26984457539), ("input.data", 1674303997472)],
)
def test_solution_02(source_data, number_of_fishes):
    assert solution_02(source_data) == number_of_fishes
