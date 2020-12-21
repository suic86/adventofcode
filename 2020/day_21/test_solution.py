import pytest
from solution import read_data, allergens_to_ingredients, solution_01, solution_02


@pytest.fixture
def parsed_data():
    return {
        "dairy": [
            ["mxmxvkd", "kfcds", "sqjhc", "nhms"],
            ["trh", "fvjkl", "sbzzf", "mxmxvkd"],
        ],
        "fish": [["mxmxvkd", "kfcds", "sqjhc", "nhms"], ["sqjhc", "mxmxvkd", "sbzzf"]],
        "soy": [["sqjhc", "fvjkl"]],
    }


def test_parse_data(parsed_data):
    assert read_data("test_solution_01.data")[0] == parsed_data


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_01.data", {"dairy": "mxmxvkd", "fish": "sqjhc", "soy": "fvjkl"})],
)
def test_allergens_to_ingredients(source, result):
    assert allergens_to_ingredients(read_data(source)[0]) == result


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_01.data", 5), ("input.data", 1685)],
)
def test_solution_01(source, result):
    assert solution_01(source) == result


@pytest.mark.parametrize(
    "source,result",
    [
        ("test_solution_01.data", "mxmxvkd,sqjhc,fvjkl"),
        ("input.data", "ntft,nhx,kfxr,xmhsbd,rrjb,xzhxj,chbtp,cqvc"),
    ],
)
def test_solution_02(source, result):
    assert solution_02(source) == result
