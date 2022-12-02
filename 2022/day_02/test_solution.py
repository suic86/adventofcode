from solution import solution_01, solution_02


def test_solution_01_sample_strategy():
    assert solution_01("test.data") == 15


def test_solution_01():
    assert solution_01() == 10816


def test_solution_02_sample_strategy():
    assert solution_02("test.data") == 12


def test_solution_02():
    assert solution_02() == 11657
