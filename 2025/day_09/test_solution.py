import pytest

from solution import solution_01


@pytest.mark.parametrize(
    "path,expected", [("test.data", 50), ("input.data", 4743645488)]
)
def test_solution_01(path, expected):
    assert solution_01(path) == expected
