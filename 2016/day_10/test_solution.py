from solution import load_instructions, solution_01, solution_02


def test_load_data():
    data = load_instructions("test.data")
    assert data[("bot", 1)].values == {3}
    assert data[("bot", 2)].values == {2, 5}
    assert data[("bot", 1)].high == ("bot", 0)
    assert data[("bot", 1)].low == ("output", 1)


def test_solution_01():
    assert solution_01() == 56


def test_solution_02():
    assert solution_02() == 7847
