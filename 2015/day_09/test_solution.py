import pytest
from solution import parse_data, solution_01, solution_02

PARSED_DATA = {
    ("Belfast", "Dublin"): 141,
    ("Belfast", "London"): 518,
    ("Dublin", "London"): 464,
    ("Dublin", "Belfast"): 141,
    ("London", "Dublin"): 464,
    ("London", "Belfast"): 518,
}


def test_parse_data():
    assert parse_data("test.data") == PARSED_DATA


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 605),
        ("input.data", 117),
    ],
)
def test_solution_01(inp, exp):
    assert solution_01(inp) == exp


@pytest.mark.parametrize(
    "inp,exp",
    [
        ("test.data", 982),
        ("input.data", 909),
    ],
)
def test_solution_02(inp, exp):
    assert solution_02(inp) == exp
