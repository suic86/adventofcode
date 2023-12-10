import pytest

from solution import parse_data, solution_01, solution_02


def test_parse_data() -> None:
    directions, graph = parse_data("test_01a.data")
    assert directions == "RL"
    assert graph == {
        "AAA": ["BBB", "CCC"],
        "BBB": ["DDD", "EEE"],
        "CCC": ["ZZZ", "GGG"],
        "DDD": ["DDD", "DDD"],
        "EEE": ["EEE", "EEE"],
        "GGG": ["GGG", "GGG"],
        "ZZZ": ["ZZZ", "ZZZ"],
    }


@pytest.mark.parametrize(
    "path,result", [("test_01a.data", 2), ("test_01b.data", 6), ("input.data", 12083)]
)
def test_solution_01(path: str, result: int) -> None:
    assert solution_01(path) == result


@pytest.mark.parametrize(
    "path,result", [("test_02.data", 6), ("input.data", 13385272668829)]
)
def test_solution_02(path: str, result: int) -> None:
    assert solution_02(path) == result
