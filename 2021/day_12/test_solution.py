import pytest

from solution import load_data, path_count, solution_01, solution_02


@pytest.fixture
def smallgraph():
    return {
        "start": {"A", "b"},
        "A": {"start", "c", "b", "end"},
        "b": {"A", "d", "end", "start"},
        "d": {"b"},
        "c": {"A"},
        "end": {"A", "b"},
    }


def test_load_data(smallgraph):
    assert load_data("small_test.data") == smallgraph


def test_path_count_smallgraph(smallgraph):
    assert path_count(smallgraph) == 10


@pytest.mark.parametrize(
    "source_data,paths_count",
    [
        ("small_test.data", 10),
        ("middle_test.data", 19),
        ("test.data", 226),
        ("input.data", 5958),
    ],
)
def test_path_count(source_data, paths_count):
    assert path_count(load_data(source_data)) == paths_count


@pytest.mark.parametrize(
    "source_data,paths_count",
    [
        ("small_test.data", 10),
        ("middle_test.data", 19),
        ("test.data", 226),
        ("input.data", 5958),
    ],
)
def test_solution_01(source_data, paths_count):
    assert solution_01(source_data) == paths_count


@pytest.mark.parametrize(
    "source_data,paths_count",
    [
        ("small_test.data", 36),
        ("middle_test.data", 103),
        ("test.data", 3509),
        ("input.data", 150426),
    ],
)
def test_solution_02(source_data, paths_count):
    assert solution_02(source_data) == paths_count
