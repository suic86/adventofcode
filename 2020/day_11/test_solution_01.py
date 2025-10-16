import pytest
from solution_01 import adjacent_seats, next_area_state, next_seat_state, solution_01
from util import EMPTY, FLOOR, OCCUPIED, load_test_generations


@pytest.fixture
def testgenerations():
    return load_test_generations("test_solution_01_generations.data")


@pytest.mark.parametrize(
    "seat,adjacent_seats,expected",
    [
        (EMPTY, [EMPTY, EMPTY, EMPTY, FLOOR, FLOOR], OCCUPIED),
        (EMPTY, [EMPTY, EMPTY, EMPTY, FLOOR, OCCUPIED], EMPTY),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, FLOOR, EMPTY], OCCUPIED),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, FLOOR], EMPTY),
        (OCCUPIED, [OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, FLOOR], EMPTY),
    ],
)
def test_next_seat_state(seat, adjacent_seats, expected):
    assert next_seat_state(seat, adjacent_seats) == expected


@pytest.mark.parametrize(
    "column,row,adjacents",
    [
        (0, 0, {(1, 0), (0, 1), (1, 1)}),
        (3, 0, {(2, 0), (2, 1), (3, 1), (4, 1), (4, 0)}),
    ],
)
def test_adjacent_seats(column, row, adjacents):
    assert set(adjacent_seats(5, 5, column, row)) == adjacents


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


def test_solution_01_test_data():
    assert solution_01("test_solution_01.data") == 37


def test_solution_01_input_data():
    assert solution_01("input.data") == 2204
