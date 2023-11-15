from solution import parse_data, read_by_columns, solution_01, solution_02

READ_BY_COLUMNS = [
    (101, 102, 103),
    (201, 202, 203),
    (301, 302, 303),
    (401, 402, 403),
    (501, 502, 503),
    (601, 602, 603),
]


def test_solution_01():
    assert solution_01() == 1050


def test_solution_02():
    assert solution_02() == 1921


def test_read_by_columns():
    parsed_rows = parse_data("sample.data")
    assert read_by_columns(parsed_rows) == READ_BY_COLUMNS
