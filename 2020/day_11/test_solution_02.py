import pytest
from solution_02 import (
    next_area_state,  # visible_adjacent_seats,
    next_seat_state,
    solution_02,
)
from util import EMPTY, FLOOR, OCCUPIED, load_test_generations

# TODO: Add test for visible_adjacent_seats


@pytest.fixture
def testgenerations():
    return load_test_generations("test_solution_02_generations.data")


@pytest.mark.parametrize(
    "seat,adjacent_seats,expected",
    [
        (EMPTY, [EMPTY, EMPTY, EMPTY, FLOOR, FLOOR], OCCUPIED),
        (EMPTY, [EMPTY, EMPTY, EMPTY, FLOOR, OCCUPIED], EMPTY),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, FLOOR, EMPTY], OCCUPIED),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, FLOOR], OCCUPIED),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, FLOOR], EMPTY),
    ],
)
def test_next_seat_state(seat, adjacent_seats, expected):
    assert next_seat_state(seat, adjacent_seats) == expected


def test_next_seat_state_single_state_change(testgenerations):
    for gen, next_gen in zip(testgenerations, testgenerations[1:]):
        assert next_area_state(gen) == next_gen


def test_next_seat_state_multi_state_change(testgenerations):
    g = testgenerations[0]
    for _ in range(3):
        g = next_area_state(g)
    assert g == testgenerations[3]

    g = testgenerations[1]
    for _ in range(3):
        g = next_area_state(g)
    assert g == testgenerations[4]


def test_solution_02_test_data():
    assert solution_02("test_solution_02.data") == 26


@pytest.mark.slow
def test_solution_02_input_data():
    assert solution_02("input.data") == 1986
