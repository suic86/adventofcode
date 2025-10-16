import pytest
from solution import (
    count_all_bags,
    count_contained_bags,
    dependency_tree,
    parse_data,
    parse_rule,
    rule_tree,
    solution_01,
    solution_02,
)


@pytest.mark.parametrize(
    "line,rule",
    [
        ("faded blue bags contain no other bags.", ("faded blue", [])),
        ("dotted black bags contain no other bags.", ("dotted black", [])),
    ],
)
def test_parses_contains_no(line, rule):
    assert parse_rule(line) == rule


@pytest.mark.parametrize(
    "line,rule",
    [
        (
            "bright white bags contain 1 shiny gold bag.",
            ("bright white", [("shiny gold", 1)]),
        ),
        (
            "muted black bags contain 4 dotted yellow bag.",
            ("muted black", [("dotted yellow", 4)]),
        ),
    ],
)
def test_parses_contains_one(line, rule):
    assert parse_rule(line) == rule


@pytest.mark.parametrize(
    "line,rule",
    [
        (
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            ("dark orange", [("bright white", 3), ("muted yellow", 4)]),
        ),
        (
            "light red bags contain 1 bright white bag, 2 bright yellow bags.",
            ("light red", [("bright white", 1), ("bright yellow", 2)]),
        ),
    ],
)
def test_parses_contains_two_or_more(line, rule):
    assert parse_rule(line) == rule


@pytest.mark.parametrize(
    "rules,tree",
    [([("faded blue", [])], {})],
)
def test_dependency_tree_contains_no(rules, tree):
    assert dependency_tree(rules) == tree


@pytest.mark.parametrize(
    "rules,tree",
    [
        (
            [("muted black", [("dotted yellow", 1)])],
            {
                "dotted yellow": {
                    "muted black",
                }
            },
        ),
        (
            [("dark orange", [("bright white", 1), ("muted yellow", 2)])],
            {
                "bright white": {
                    "dark orange",
                },
                "muted yellow": {
                    "dark orange",
                },
            },
        ),
        (
            [
                ("dark orange", [("bright white", 3), ("muted yellow", 4)]),
                ("dotted yellow", []),
            ],
            {
                "bright white": {
                    "dark orange",
                },
                "muted yellow": {
                    "dark orange",
                },
            },
        ),
    ],
)
def test_dependency_tree_contains_one_or_more(rules, tree):
    assert dependency_tree(rules) == tree


@pytest.mark.parametrize(
    "source,contained_bags",
    [
        ("test_solution_01.data", 33),
        ("test_solution_02.data", 127),
        ("input.data", 20190),
    ],
)
def test_count_all_bags(source, contained_bags):
    assert count_all_bags(rule_tree(parse_data(source)), "shiny gold") == contained_bags


@pytest.mark.parametrize(
    "source,contained_bags",
    [
        ("test_solution_01.data", 32),
        ("test_solution_02.data", 126),
        ("input.data", 20189),
    ],
)
def test_count_contained_bags(source, contained_bags):
    assert (
        count_contained_bags(rule_tree(parse_data(source)), "shiny gold")
        == contained_bags
    )


@pytest.mark.parametrize(
    "source,expected", [("test_solution_01.data", 4), ("input.data", 128)]
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.parametrize(
    "source,contained_bags",
    [
        ("test_solution_01.data", 32),
        ("test_solution_02.data", 126),
        ("input.data", 20189),
    ],
)
def test_solution_02(source, contained_bags):
    assert solution_02(source) == contained_bags
