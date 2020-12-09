import pytest


from solution import (
    contains_sum,
    first_non_matching,
    solution_01,
    solution_02,
    subarray_with_given_sum,
)


@pytest.fixture
def test_solution_data():
    with open("test_solution.data") as fobj:
        return [int(line.rstrip()) for line in fobj]


@pytest.mark.parametrize(
    "data,value,result", [([1, 2, 3], 4, True), ([1, 2, 3], 6, False)]
)
def test_contains_sum(data, value, result):
    assert contains_sum(data, value) == result


def test_first_non_matching(test_solution_data):
    assert first_non_matching(test_solution_data, 5) == 127


def test_subarray_with_given_sum(test_solution_data):
    assert subarray_with_given_sum(test_solution_data, 127) == [15, 25, 47, 40]


def test_solution_01():
    assert solution_01() == 375054920


def test_solution_02():
    assert solution_02() == 54142584
