import pytest
from solution import process_line, solution_01, solution_02


@pytest.mark.parametrize(
    "line,out",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_process_line_part_one(line: str, out: int) -> None:
    assert process_line(line) == out


@pytest.mark.parametrize(
    "line,out",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_process_line_part_two(line: str, out: int) -> None:
    assert process_line(line, part_two=True) == out


@pytest.mark.parametrize("data,exp", [("test.data", 142), ("input.data", 56506)])
def test_solution_01(data: str, exp: int) -> None:
    assert solution_01(data) == exp


@pytest.mark.parametrize("data,exp", [("test02.data", 281), ("input.data", 56017)])
def test_solution_02(data: str, exp: int) -> None:
    assert solution_02(data) == exp
