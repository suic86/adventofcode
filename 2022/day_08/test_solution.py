from solution import solution_01, solution_02


def test_solution_01_test_data():
    assert solution_01("test.data") == 21


def test_solution_01():
    assert solution_01() == 1812


def test_solution_02_test_data():
    assert solution_02("test.data") == 8


def test_solution_02():
    assert solution_02() == 315495
