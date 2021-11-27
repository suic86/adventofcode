import pytest
from solution import bottom_program, load_data, sum_weights, solution_01, solution_02


TEST_TOWER = {
    "tknk": {"ugml", "padx", "fwft"},
    "ugml": {"gyxo", "ebii", "jptl"},
    "padx": {"havc", "pbga", "qoyq"},
    "fwft": {"ktlj", "cntj", "xhth"},
}

TEST_WEIGHTS = {
    "pbga": 66,
    "xhth": 57,
    "ebii": 61,
    "havc": 66,
    "ktlj": 57,
    "fwft": 72,
    "qoyq": 66,
    "padx": 45,
    "tknk": 41,
    "jptl": 61,
    "ugml": 68,
    "gyxo": 61,
    "cntj": 57,
}


def test_load_data_weights():
    weights, _ = load_data("test.data")
    assert weights == TEST_WEIGHTS


def test_load_data_towers():
    _, towers = load_data("test.data")
    assert towers == TEST_TOWER


def test_bottom_program():
    assert bottom_program(TEST_TOWER) == "tknk"


@pytest.mark.parametrize(
    "program, weight",
    [
        ("gyxo", 61),
        ("cntj", 57),
        ("ugml", 251),
        ("tknk", 778),
    ],
)
def test_sum_weights(program, weight):
    assert sum_weights(program, TEST_WEIGHTS, TEST_TOWER) == weight


def test_solution_01():
    assert solution_01() == "mkxke"


def test_solution_02():
    assert solution_02() == 268
