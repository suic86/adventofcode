from solution import sum_numbers, sum_with_no_red, solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "json,expected",
    [
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ],
)
def test_sum_numbers(json, expected):
    assert sum_numbers(json) == expected


@pytest.mark.parametrize(
    "jobj,expected",
    [
        [[1, 2, 3], 6],
        [[1, {"c": "red", "b": 2}, 3], 4],
        [{"d": "red", "e": [1, 2, 3, 4], "f": 5}, 0],
        [[1, "red", 5], 6],
    ],
)
def test_sum_with_no_red(jobj, expected):
    assert sum_with_no_red(jobj) == expected


def test_solution_01():
    assert solution_01() == 191164


def test_solution_02():
    assert solution_02() == 87842
