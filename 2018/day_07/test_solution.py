from solution import construction_time, load_data, solution_01, solution_02

import pytest

PARSED_DATA = {"A": {"C"}, "B": {"A"}, "D": {"A"}, "E": {"F", "B", "D"}, "F": {"C"}}


def test_load_data():
    assert load_data("test.data") == PARSED_DATA


@pytest.mark.parametrize(
    "source,workers,default_duration", [("test.data", 2, 0), ("input.data", 5, 60)]
)
def test_construction_time(source, workers, default_duration):
    assert construction_time(
        load_data(source), workers=workers, default_duration=default_duration
    )


@pytest.mark.parametrize(
    "source,expected",
    [("test.data", "CABDFE"), ("input.data", "OUGLTKDJVBRMIXSACWYPEQNHZF")],
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


def test_solution_02():
    assert solution_02() == 929
