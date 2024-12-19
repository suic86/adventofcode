from solution import solution_01, solution_02

import pytest


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_01.data", 7036),
        ("test_02.data", 11048),
        ("input.data", 94444),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test_01.data", 0),
        ("test_02.data", 0),
        ("input.data", 0),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
