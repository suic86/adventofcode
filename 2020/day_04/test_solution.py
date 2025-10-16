import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "source,result", [("test_solution_01.data", 2), ("input.data", 242)]
)
def test_solution_01(source, result):
    assert solution_01(source) == result


@pytest.mark.parametrize(
    "source,result", [("test_solution_02.data", 4), ("input.data", 186)]
)
def test_solution_02(source, result):
    assert solution_02(source) == result
