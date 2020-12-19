import pytest
from solution import (
    read_data,
    convert_to_regex,
    solution_01,
    solution_02,
    solution_02_check,
)


def test_read_data():
    rules, data = read_data("test_solution_01.data")
    assert rules == {
        0: "4 1 5",
        1: "2 3 | 3 2",
        2: "4 4 | 5 5",
        3: "4 5 | 5 4",
        4: "a",
        5: "b",
    }
    assert data == [
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]


def test_convert_to_regex():
    rules = {0: "1 2 1", 1: "2 | 3", 2: "a", 3: "b"}
    assert convert_to_regex(0, rules) == "(?:(?:a|b)a(?:a|b))"
    rules = {0: "1 2 1", 1: "2 3", 2: "a", 3: "b"}
    assert convert_to_regex(0, rules) == "(?:(?:ab)a(?:ab))"


@pytest.mark.parametrize(
    "message",
    [
        "bbabbbbaabaabba",
        "babbbbaabbbbbabbbbbbaabaaabaaa",
        "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
        "bbbbbbbaaaabbbbaaabbabaaa",
        "bbbababbbbaaaaaaaabbababaaababaabab",
        "ababaaaaaabaaab",
        "ababaaaaabbbaba",
        "baabbaaaabbaaaababbaababb",
        "abbbbabbbbaaaababbbbbbaaaababb",
        "aaaaabbaabaaaaababaa",
        "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
        "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
    ],
)
def test_solution_02_check_test_data_expect_true(message):
    rules, _ = read_data("test_solution_02.data")
    r_42 = convert_to_regex(42, rules)
    r_31 = convert_to_regex(31, rules)
    assert solution_02_check(message, r_42, r_31) is True


@pytest.mark.parametrize(
    "message",
    [
        "aaaabbaaaabbaaa",
        "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
        "babaaabbbaaabaababbaabababaaab",
    ],
)
def test_solution_02_check_test_data_expect_false(message):
    rules, _ = read_data("test_solution_02.data")
    r_42 = convert_to_regex(42, rules)
    r_31 = convert_to_regex(31, rules)
    assert solution_02_check(message, r_42, r_31) is False


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_01.data", 2), ("test_solution_02.data", 3), ("input.data", 144)],
)
def test_solution_01(source, result):
    assert solution_01(source) == result


@pytest.mark.parametrize(
    "source,result",
    [("test_solution_02.data", 12), ("input.data", 260)],
)
def test_solution_02(source, result):
    assert solution_02(source) == result
