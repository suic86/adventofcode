import pytest

from solution import load_data, fold, solution_01, solution_02


@pytest.fixture
def testcoordinates():
    return {
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    }


@pytest.fixture
def testfolds():
    return [("y", 7), ("x", 5)]


def test_load_data(testcoordinates, testfolds):
    coordinates, folds = load_data("test.data")
    assert coordinates == testcoordinates
    assert folds == testfolds


def test_fold(testcoordinates, testfolds):
    assert len(fold(testcoordinates, *testfolds[0])) == 17


@pytest.mark.parametrize("source_data,dots", [("test.data", 17), ("input.data", 842)])
def test_solution_01(source_data, dots):
    assert solution_01(source_data) == dots


@pytest.mark.parametrize(
    "source_data,result",
    [
        ("test.data", "solution_02_test_data_result.txt"),
        ("input.data", "solution_02_input_data_result.txt"),
    ],
)
def test_solution_02(source_data, result):
    with open(result, "r") as fobj:
        expected = list(map(list, map(str.strip, fobj)))

    solution = [list(row.strip()) for row in solution_02(source_data).split("\n")]
    assert solution == expected
