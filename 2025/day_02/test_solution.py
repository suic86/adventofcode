import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 1227775554),
        ("input.data", 56660955519),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 4174379265),
        ("input.data", 79183223243),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
