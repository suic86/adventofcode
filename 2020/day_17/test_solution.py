import pytest
from solution import read_data, next_state, solution_01, solution_02

test_solution_01_data = {
    (0, 1, 0),
    (1, 2, 0),
    (2, 0, 0),
    (2, 1, 0),
    (2, 2, 0),
}

test_solution_02_data = {
    (0, 1, 0, 0),
    (1, 2, 0, 0),
    (2, 0, 0, 0),
    (2, 1, 0, 0),
    (2, 2, 0, 0),
}


def test_read_data():
    assert read_data("test_solution_01.data") == test_solution_01_data
    assert read_data("test_solution_01.data", dimensions=4) == test_solution_02_data


def test_next_state_solution_01():
    ns = next_state(test_solution_01_data)
    assert len(ns) == 11
    ns = next_state(ns)
    assert len(ns) == 21
    ns = next_state(ns)
    assert len(ns) == 38


def test_next_state_solution_02():
    ns = next_state(test_solution_02_data, dimensions=4)
    assert len(ns) == 29
    ns = next_state(ns, dimensions=4)
    assert len(ns) == 60


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test_solution_01.data", 112),
        ("input.data", 293),
    ],
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.slow
@pytest.mark.parametrize(
    "source,expected",
    [
        ("test_solution_01.data", 848),
        ("input.data", 1816),
    ],
)
def test_solution_02(source, expected):
    assert solution_02(source) == expected
