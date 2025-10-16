import pytest
from solution import load_data, solution_01, solution_02


@pytest.fixture
def testdata():
    return [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_load_data(testdata):
    assert load_data("test.data") == testdata


@pytest.mark.parametrize(
    "source_data,score", [("test.data", 26397), ("input.data", 318081)]
)
def test_solution_01(source_data, score):
    assert solution_01(source_data) == score


@pytest.mark.parametrize(
    "source_data,score", [("test.data", 288957), ("input.data", 4361305341)]
)
def test_solution_02(source_data, score):
    assert solution_02(source_data) == score
