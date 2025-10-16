import pytest
from solution import parse_data, solution_01, solution_02, wins


@pytest.mark.parametrize(
    "path,parsed",
    [
        ("test.data", [(7, 9), (15, 40), (30, 200)]),
        ("input.data", [(61, 430), (67, 1036), (75, 1307), (71, 1150)]),
    ],
)
def test_parse_data(path: str, parsed: list[tuple[int, int]]) -> None:
    assert parse_data(path) == parsed


@pytest.mark.parametrize("race,expected", [((7, 9), 4), ((15, 40), 8), ((30, 200), 9)])
def test_wins(race: tuple[int, int], expected: int) -> None:
    assert wins(race) == expected


@pytest.mark.parametrize("path,total", [("test.data", 288), ("input.data", 316800)])
def test_solution_01(path: str, total: int) -> None:
    assert solution_01(path) == total


def test_solution_02_test_data() -> None:
    assert solution_02("test.data") == 71503


@pytest.mark.slow
def test_solution_02_input_data() -> None:
    assert solution_02("input.data") == 45647654
