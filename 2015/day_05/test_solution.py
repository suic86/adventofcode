import pytest
from solution import is_nice_01, is_nice_02, solution_01, solution_02


@pytest.mark.parametrize("string", ["ugknbfddgicrmopn", "aaa"])
def test_nice_01(string):
    assert is_nice_01(string) == True


@pytest.mark.parametrize(
    "string",
    [
        "jchzalrnumimnmhp",
        "haegwjzuvuyypxyu",
        "dvszwmarrgswjxmb",
    ],
)
def test_naughty_01(string):
    assert is_nice_01(string) == False


@pytest.mark.parametrize("string", ["qjhvhtzxzqqjkmpb", "xxyxx"])
def test_nice_02(string):
    assert is_nice_02(string) == True


@pytest.mark.parametrize("string", ["uurcxstgmygtbstg", "ieodomkazucvgmuy"])
def test_naughty_02(string):
    assert is_nice_02(string) == False


def test_solution_01():
    assert solution_01() == 236


def test_solution_02():
    assert solution_02() == 51
