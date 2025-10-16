import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "data, full_overlaps",
    [
        ("test.data", 2),
        ("input.data", 530),
    ],
)
def test_solution_01(data, full_overlaps):
    assert solution_01(data) == full_overlaps


@pytest.mark.parametrize(
    "data, any_overlaps",
    [
        ("test.data", 4),
        ("input.data", 903),
    ],
)
def test_solution_02(data, any_overlaps):
    assert solution_02(data) == any_overlaps
