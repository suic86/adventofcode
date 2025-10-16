import pytest
from solution import length, solution_01, solution_02


@pytest.mark.parametrize(
    "polymer,expected",
    [
        ("dabAcCaCBAcCcaDA", 10),
        ("dbcCCBcCcD", 6),
        ("daAcCaCAcCcaDA", 8),
        ("dabAaBAaDA", 4),
        ("abAcCaCBAcCcaA", 6),
    ],
)
def test_length(polymer, expected):
    assert length(polymer) == expected


@pytest.mark.parametrize(
    "polymer,to_remove,expected",
    [
        ("dabAcCaCBAcCcaDA", "", 10),
        ("dbcCCBcCcD", "A", 6),
        ("daAcCaCAcCcaDA", "B", 8),
        ("dabAaBAaDA", "C", 4),
        ("abAcCaCBAcCcaA", "D", 6),
    ],
)
def test_length_w_to_remove(polymer, to_remove, expected):
    assert length(polymer, to_remove=to_remove) == expected


@pytest.mark.parametrize("source,length", [("test.data", 10), ("input.data", 9704)])
def test_solution_01(source: str, length: int) -> None:
    assert solution_01(source) == length


@pytest.mark.parametrize("source,length", [("test.data", 4), ("input.data", 6942)])
def test_solution_02(source: str, length: int) -> None:
    assert solution_02(source) == length
