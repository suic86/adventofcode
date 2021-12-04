from solution import distance, farthest, solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "path,expected",
    [
        ("ne,ne,ne", 3),
        ("ne,ne,sw,sw", 0),
        ("ne,ne,s,s", 2),
        ("se,sw,se,sw,sw", 3),
    ],
)
def test_distance(path, expected):
    assert distance(path.split(",")) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("ne,ne,ne", 3),
        ("ne,ne,sw,sw", 2),
        ("ne,ne,s,s", 2),
        ("se,sw,se,sw,sw", 3),
    ],
)
def test_farthest(path, expected):
    assert farthest(path.split(",")) == expected


def test_solution_01():
    assert solution_01() == 698


def test_solution_02():
    assert solution_02() == 1435
