import pytest
from solution import (
    co2_scrubber_rating,
    gamma_epsilon,
    load_data,
    oxygen_generator_rating,
    solution_01,
    solution_02,
)


@pytest.fixture
def report():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_load_data(report):
    assert load_data("test.data") == report


def test_gamma_epsilon(report):
    assert gamma_epsilon(report) == (22, 9)


def test_oxygen_generator_rating(report):
    assert oxygen_generator_rating(report) == 23


def test_co2_scrubber_rating(report):
    assert co2_scrubber_rating(report) == 10


@pytest.mark.parametrize(
    "source_data,expected",
    [
        ("test.data", 198),
        ("input.data", 3633500),
    ],
)
def test_solution_01(source_data, expected):
    assert solution_01(source_data) == expected


@pytest.mark.parametrize(
    "source_data,expected",
    [
        ("test.data", 230),
        ("input.data", 4550283),
    ],
)
def test_solution_02(source_data, expected):
    assert solution_02(source_data) == expected
