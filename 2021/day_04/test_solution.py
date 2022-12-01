import pytest

from solution import load_data, solution_01, solution_02


@pytest.fixture
def boards():
    return [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]


@pytest.fixture
def numbers():
    return [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]


def test_load_data_numbers(numbers):
    assert load_data("test.data")[0] == numbers


def test_load_data_boards(boards):
    assert load_data("test.data")[1] == boards


@pytest.mark.parametrize(
    "source,score",
    [
        ("test.data", 4512),
        ("input.data", 2496),
    ],
)
def test_solution_01(source, score):
    assert solution_01(source) == score


@pytest.mark.parametrize(
    "source,score",
    [
        ("test.data", 1924),
        ("input.data", 25925),
    ],
)
def test_solution_02(source, score):
    assert solution_02(source) == score
