import pytest

from solution import parse_instruction, eval_instructions, solution_01, solution_02


@pytest.fixture
def test_data():
    with open("test.data") as fobj:
        return list(map(str.strip, fobj))


@pytest.mark.parametrize(
    "raw,parsed",
    [
        ("ioe dec 890 if qk > -10", ["ioe", "dec", 890, "qk", ">", -10]),
        ("gif inc -533 if qt <= 7", ["gif", "inc", -533, "qt", "<=", 7]),
        ("itw dec 894 if t != 0", ["itw", "dec", 894, "t", "!=", 0]),
        ("nwe inc 486 if hfh < -2", ["nwe", "inc", 486, "hfh", "<", -2]),
    ],
)
def test_parse_instruction(raw, parsed):
    assert parse_instruction(raw) == parsed


def test_eval_instructions(test_data):
    assert eval_instructions(*test_data) == {
        "a": 1,
        "b": 0,
        "c": -10,
    }


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test.data", 1),
        ("input.data", 4902),
    ],
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        ("test.data", 10),
        ("input.data", 7037),
    ],
)
def test_solution_02(source, expected):
    assert solution_02(source) == expected
