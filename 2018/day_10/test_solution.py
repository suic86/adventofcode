import pytest
from data import PARSED
from solution import find_message, load_data, solution_01, solution_02


@pytest.fixture
def message():
    with open("output.data") as fobj:
        return fobj.read()


@pytest.fixture
def points():
    return load_data("input.data")


def test_load_data():
    assert load_data("test.data") == PARSED


def test_find_message(points, message):
    assert find_message(points)[0] == message


def test_solution_01(message):
    assert solution_01() == message


def test_solution_02():
    assert solution_02() == 10558
