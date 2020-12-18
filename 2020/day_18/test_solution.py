import pytest

from solution import evaluate, parse, solution_01, solution_02


@pytest.mark.parametrize(
    "expression,result",
    [
        ("(2 * 3)", "2 3 *"),
        ("1 + 2 * 3 + 4 * 5 + 6", "1 2 + 3 * 4 + 5 * 6 +"),
        ("(2 + 3) * 4 * 5", "2 3 + 4 * 5 *"),
        ("2 * 3 + (4 * 5)", "2 3 * 4 5 * +"),
        ("(2 + 3) + (4 * 5)", "2 3 + 4 5 * +"),
        (
            "5 + (8 * 3 + 9 + 3 * 4 * 3)",
            "5 8 3 * 9 + 3 + 4 * 3 * +",
        ),
        (
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
            "5 9 * 7 3 * 3 * 9 + 3 * 8 6 + 4 * + *",
        ),
        (
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
            "2 4 + 9 * 6 9 + 8 * 6 + * 6 + 2 + 4 + 2 *",
        ),
        (
            "6 * (9 * 5 * 9 + 9 + (3 + 7) * (8 + 9 + 3 + 5 + 2 + 7)) * (6 + 7 + 4) + (2 + (2 + 7 * 2 + 4 + 2) + 4 * (9 + 6 * 5 + 2 * 9)) + (8 + (8 + 6 * 5 + 6 + 9) + (2 * 7 + 2 * 9 * 9) + 7)",
            "6 9 5 * 9 * 9 + 3 7 + + 8 9 + 3 + 5 + 2 + 7 + * * 6 7 + 4 + * 2 2 7 + 2 * 4 + 2 + + 4 + 9 6 + 5 * 2 + 9 * * + 8 8 6 + 5 * 6 + 9 + + 2 7 * 2 + 9 * 9 * + 7 + +",
        ),
        (
            "(8 * (2 + 8) + 9 + 7 + 8 * (3 * 6 + 7 * 6 + 5 + 7)) * (2 + 9 * (4 * 7 + 3 + 4 + 6 * 5)) * ((2 + 9 + 6 * 3 * 8) * 5 * 4) * 7",
            "8 2 8 + * 9 + 7 + 8 + 3 6 * 7 + 6 * 5 + 7 + * 2 9 + 4 7 * 3 + 4 + 6 + 5 * * * 2 9 + 6 + 3 * 8 * 5 * 4 * * 7 *",
        ),
    ],
)
def test_parse_no_precedence(expression, result):
    assert " ".join(parse(expression, operator_precendence={"+": 0, "*": 0})) == result


@pytest.mark.parametrize(
    "expression,result",
    [
        ("2 + 3 + 4", 9),
        ("2 + 3 * 4", 20),
        ("1 + 2 * 3 + 4 * 5 + 6", 71),
        ("(2 * 3)", 6),
        ("(2 + 3) * 4 * 5", 100),
        ("2 * 3 + (4 * 5)", 26),
        ("(2 + 3) + (4 * 5)", 25),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
    ],
)
def test_evaluate_no_precedence(expression, result):
    assert evaluate(parse(expression, operator_precendence={"+": 0, "*": 0})) == result


@pytest.mark.parametrize(
    "expression",
    [
        "2 + 3 + 4",
        "2 + 3 * 4",
        "1 + 2 * 3 + 4 * 5 + 6",
        "(2 * 3)",
        "(2 + 3) * 4 * 5",
        "2 * 3 + (4 * 5)",
        "(2 + 3) + (4 * 5)",
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
    ],
)
def test_evaluation_mathematical_precendence(expression):
    assert evaluate(parse(expression, operator_precendence={"*": 1, "+": 0})) == eval(
        expression
    )


@pytest.mark.parametrize(
    "expression,result",
    [
        ("1 + (2 * 3) + (4 * (5 + 6))", 51),
        ("2 * 3 + (4 * 5)", 46),
        ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
        ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
        ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    ],
)
def test_evaluate_addition_precedence(expression, result):
    assert evaluate(parse(expression, operator_precendence={"+": 1, "*": 0})) == result


@pytest.mark.parametrize(
    "source,result", [("test_solution_01.data", 26335), ("input.data", 4940631886147)]
)
def test_solution_01(source, result):
    assert solution_01(source) == result


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_02.data", 693942), ("input.data", 283582817678281)],
)
def test_solution_02(source, result):
    assert solution_02(source) == result
