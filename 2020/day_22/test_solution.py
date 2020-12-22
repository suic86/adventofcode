import pytest
from collections import deque
from solution import play, play_recursive, read_data, score, solution_01, solution_02


@pytest.fixture
def decks():
    return [9, 2, 6, 3, 1], [5, 8, 4, 7, 10]


def test_read_data(decks):
    assert read_data("test_solution_01.data") == decks


def test_play(decks):
    assert play(*decks) == deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])


def test_score():
    assert score(deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])) == 306


def test_play_recursive(decks):
    assert play_recursive(*decks) == (2, deque([7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))


@pytest.mark.parametrize(
    "source,result", [("test_solution_01.data", 306), ("input.data", 31781)]
)
def test_solution_01(source, result):
    assert solution_01(source) == result


def test_solution_02_test_data():
    assert solution_02("test_solution_01.data") == 291


def test_solution_02_input_data():
    assert solution_02("input.data") == 35154
