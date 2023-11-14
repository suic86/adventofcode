from solution import load_data, solution_01, solution_02
import pytest

PARSED_DATA = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar",
]


def test_load_data():
    assert load_data("test.data") == PARSED_DATA


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test.data", "easter"),
        ("input.data", "usccerug"),
    ],
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test.data", "advent"),
        ("input.data", "cnvvtafc"),
    ],
)
def test_solution_02(source, expected):
    assert solution_02(source) == expected
