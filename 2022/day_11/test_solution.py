from solution import solution_01, solution_02


def test_solution_01_test_data():
    assert solution_01("test.data") == 10605


def test_solution_01():
    assert solution_01() == 101436


def test_soluiton_02_test_data():
    assert solution_02("test.data") == 2713310158


def test_soluiton_02():
    assert solution_02() == 19754471646
