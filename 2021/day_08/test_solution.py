import pytest

from solution import (
    load_data,
    count_easy_digits,
    decode_segments,
    decode_number,
    solution_01,
    solution_02,
)

NUMBERS = """
 0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


@pytest.fixture
def testdata():
    return [
        [
            [
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ],
            ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
        ],
        [
            [
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ],
            ["fcgedb", "cgb", "dgebacf", "gc"],
        ],
        [
            [
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ],
            ["cg", "cg", "fdcagb", "cbg"],
        ],
        [
            [
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ],
            ["efabcd", "cedba", "gadfec", "cb"],
        ],
        [
            [
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ],
            ["gecf", "egdcabf", "bgf", "bfgea"],
        ],
        [
            [
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ],
            ["gebdcfa", "ecba", "ca", "fadegcb"],
        ],
        [
            [
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ],
            ["cefg", "dcbef", "fcge", "gbcadfe"],
        ],
        [
            [
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ],
            ["ed", "bcgafe", "cdgba", "cbgef"],
        ],
        [
            [
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ],
            ["gbdfcae", "bgc", "cg", "cgb"],
        ],
        [
            [
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ],
            ["fgae", "cfgab", "fg", "bagce"],
        ],
    ]


def test_load_data(testdata):
    assert load_data("test.data") == testdata


def test_count_easy_digits(testdata):
    assert count_easy_digits(testdata) == 26


def test_decode_segments():
    """
     aaaa   dddd
    b    c e    a
    b    c e    a
     dddd   ffff
    e    f g    b
    e    f g    b
     gggg   cccc
    """
    inp = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split()
    decoded = {"a": "d", "b": "e", "c": "a", "d": "f", "e": "g", "f": "b", "g": "c"}
    assert decode_segments(inp) == decoded


def test_decode_number():
    patterns, segments = (
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(),
        "cdfeb fcadb cdfeb cdbaf".split(),
    )
    assert decode_number(patterns, segments) == 5353


@pytest.mark.parametrize(
    "source_data, sum_of_output_values", [("test.data", 26), ("input.data", 452)]
)
def test_solution_01(source_data, sum_of_output_values):
    assert solution_01(source_data) == sum_of_output_values


@pytest.mark.parametrize(
    "source_data, sum_of_output_values", [("test.data", 61229), ("input.data", 1096964)]
)
def test_solution_02(source_data, sum_of_output_values):
    assert solution_02(source_data) == sum_of_output_values
