import pytest

from solution import run_program, solution_01, solution_02


@pytest.mark.parametrize(
    "program,output",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_run_program(program, output):
    assert run_program(program) == output


def test_solution_01():
    assert solution_01() == 3267740


def test_solution_02():
    assert solution_02() == 7870
