from solution import group_count, load_data, solution_01, solution_02, zero_group_size

import pytest

TEST_PIPES = {
    0: {2},
    1: {1},
    2: {0, 3, 4},
    3: {2, 4},
    4: {2, 3, 6},
    5: {6},
    6: {4, 5},
}


def test_load_data():
    assert load_data("test.data") == TEST_PIPES


def test_zero_group_size():
    assert zero_group_size(TEST_PIPES) == 6


def test_group_count():
    assert group_count(TEST_PIPES) == 2


@pytest.mark.parametrize(
    "input_data,size",
    [
        ("test.data", 6),
        ("input.data", 115),
    ],
)
def test_solution_01(input_data, size):
    assert solution_01(input_data) == size


@pytest.mark.parametrize(
    "input_data,size",
    [
        ("test.data", 2),
        # ("input.data", 115),
    ],
)
def test_solution_02(input_data, size):
    assert solution_02(input_data) == size
