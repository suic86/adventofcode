import pytest

from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "source,result",
    [
        ("test_solution_01_01.data", 7 * 5),
        ("test_solution_01_02.data", 22 * 10),
    ],
)
def test_solution_01(source, result):
    assert solution_01(source) == result


def test_solution_01_input_data():
    assert solution_01("input.data") == 1690


@pytest.mark.parametrize(
    "source,result",
    [
        ("test_solution_01_01.data", 8),
        ("test_solution_01_02.data", 19208),
        ("input.data", 5289227976704),
    ],
)
def test_solution_02(source, result):
    assert solution_02(source) == result
