import pytest
from solution import (
    field_candidates,
    match_fields,
    parse_field,
    parse_ticket,
    read_data,
    solution_01,
    solution_02,
    ticket_scanning_error_rate,
    valid_tickets,
)


@pytest.mark.parametrize(
    "row,field",
    [
        ("class: 1-3 or 5-7", ("class", [[1, 3], [5, 7]])),
        (
            "departure location: 37-479 or 485-954",
            ("departure location", [[37, 479], [485, 954]]),
        ),
    ],
)
def test_parse_field(row, field):
    assert parse_field(row) == field


@pytest.mark.parametrize(
    "row,ticket",
    [
        (
            "97,101,149,103,137,61,59,223,263,179,131,113,241,127,53,109,89,173,107,211\n",
            [
                97,
                101,
                149,
                103,
                137,
                61,
                59,
                223,
                263,
                179,
                131,
                113,
                241,
                127,
                53,
                109,
                89,
                173,
                107,
                211,
            ],
        )
    ],
)
def test_parse_ticket(row, ticket):
    assert parse_ticket(row) == ticket


PARSED_TEST_SOLUTION_01_DATA = {
    "fields": {
        "class": [[1, 3], [5, 7]],
        "row": [[6, 11], [33, 44]],
        "seat": [[13, 40], [45, 50]],
    },
    "my ticket": [7, 1, 14],
    "nearby tickets": [
        [7, 3, 47],
        [40, 4, 50],
        [55, 2, 20],
        [38, 6, 12],
    ],
}


PARSED_TEST_SOLUTION_02_DATA = {
    "fields": {
        "class": [[0, 1], [4, 19]],
        "row": [[0, 5], [8, 19]],
        "seat": [[0, 13], [16, 19]],
    },
    "my ticket": [11, 12, 13],
    "nearby tickets": [
        [3, 9, 18],
        [15, 1, 5],
        [5, 14, 9],
    ],
}


@pytest.mark.parametrize(
    "source,parsed_data",
    [
        ("test_solution_01.data", PARSED_TEST_SOLUTION_01_DATA),
        ("test_solution_02.data", PARSED_TEST_SOLUTION_02_DATA),
    ],
)
def test_read_data(source, parsed_data):
    assert read_data(source) == parsed_data


def test_ticket_scanning_error_rate():
    assert ticket_scanning_error_rate(PARSED_TEST_SOLUTION_01_DATA) == 71
    assert ticket_scanning_error_rate(read_data("test_solution_01.data")) == 71


@pytest.mark.parametrize(
    "path,expected", [("test_solution_01.data", 71), ("input.data", 20013)]
)
def test_solution_01(path, expected):
    assert solution_01(path) == expected


@pytest.mark.parametrize(
    "ticket_data,expected",
    [
        (PARSED_TEST_SOLUTION_01_DATA, [[7, 3, 47]]),
        (
            PARSED_TEST_SOLUTION_02_DATA,
            [
                [3, 9, 18],
                [15, 1, 5],
                [5, 14, 9],
            ],
        ),
    ],
)
def test_valid_tickets(ticket_data, expected):
    assert valid_tickets(ticket_data) == expected


def test_field_candidates():
    assert field_candidates(PARSED_TEST_SOLUTION_02_DATA) == [
        [0, {"row"}],
        [1, {"row", "class"}],
        [2, {"row", "class", "seat"}],
    ]


def test_match_fields():
    assert match_fields(PARSED_TEST_SOLUTION_02_DATA) == [
        "row",
        "class",
        "seat",
    ]


def test_solution_02():
    assert solution_02() == 5977293343129
