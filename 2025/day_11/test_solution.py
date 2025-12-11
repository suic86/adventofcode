import pytest

from solution import solution_01


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 5),
        # ("input.data", -1),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected
