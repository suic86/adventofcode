from collections import Counter
from itertools import islice

import pytest
from solution import (
    load_data,
    naive_step_gen,
    optimized_step_gen,
    solution_01,
    solution_02,
)


@pytest.fixture
def testdata():
    polymer_template = "NNCB"
    insertion_rules = {
        ("C", "H"): "B",
        ("H", "H"): "N",
        ("C", "B"): "H",
        ("N", "H"): "C",
        ("H", "B"): "C",
        ("H", "C"): "B",
        ("H", "N"): "C",
        ("N", "N"): "C",
        ("B", "H"): "H",
        ("N", "C"): "B",
        ("N", "B"): "B",
        ("B", "N"): "B",
        ("B", "B"): "N",
        ("B", "C"): "B",
        ("C", "C"): "N",
        ("C", "N"): "C",
    }
    return polymer_template, insertion_rules


def test_load_data(testdata):
    assert load_data("test.data") == testdata


@pytest.mark.parametrize(
    "step,polymer",
    [
        (1, "NCNBCHB"),
        (2, "NBCCNBBBCBHCB"),
        (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
    ],
)
def test_step_gen(step, polymer, testdata):
    first_step = next(islice(naive_step_gen(*testdata), step - 1, step))
    assert first_step == polymer


@pytest.mark.parametrize(
    "step,polymer",
    [
        (1, "NCNBCHB"),
        (2, "NBCCNBBBCBHCB"),
        (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
    ],
)
def test_optimized_step_gen(step, polymer, testdata):
    nth_step = next(islice(optimized_step_gen(*testdata), step - 1, step))
    assert nth_step == Counter(polymer)


@pytest.mark.parametrize(
    "source_data,result", [("test.data", 1588), ("input.data", 2891)]
)
def test_solution_01(source_data, result):
    assert solution_01(source_data) == result


@pytest.mark.parametrize(
    "source_data,result", [("test.data", 2188189693529), ("input.data", 4607749009683)]
)
def test_solution_02(source_data, result):
    assert solution_02(source_data) == result
