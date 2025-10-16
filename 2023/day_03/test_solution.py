import pytest
from solution import Schema, gears, load_data, solution_01, solution_02, symbols


@pytest.fixture
def schema() -> Schema:
    return load_data("test.data")


def test_gears(schema) -> None:
    assert gears(schema) == {(1, 3), (4, 3), (8, 5)}


def test_symbols(schema) -> None:
    assert symbols(schema) == {(5, 5), (4, 3), (8, 3), (3, 6), (1, 3), (8, 5)}


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 4361),
        ("input.data", 554003),
    ],
)
def test_solution_01(path: str, expected: int) -> None:
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 467835),
        ("input.data", 87263515),
    ],
)
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
