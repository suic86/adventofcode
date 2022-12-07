from solution import solution_01, solution_02


def test_solution_01_test_data():
    assert solution_01("test.data") == 95437


def test_solution_02_input_data():
    assert solution_01("input.data") == 1989474


def test_solution_02_test_data():
    assert solution_02("test.data") == 24933642


def test_solution_02():
    assert solution_02() == 1111607
