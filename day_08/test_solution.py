import pytest

from itertools import islice
from solution import (
    detect_infinite_loop,
    parse_instruction,
    parse_program,
    run_instruction,
    run_program,
    run_program_from_file,
    solution_01,
    solution_02,
)


TEST_DATA_SOLUTION_01 = """
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        """
TERMINATING_PROGRAM = "acc 1\nacc 1\nacc 1"


@pytest.mark.parametrize(
    "line,instruction",
    [
        ("nop +0", ("nop", 0)),
        ("acc +1", ("acc", 1)),
        ("jmp +4", ("jmp", 4)),
        ("acc +3", ("acc", 3)),
        ("jmp -3", ("jmp", -3)),
        ("acc -99", ("acc", -99)),
    ],
)
def test_parse_instruction(line, instruction):
    assert parse_instruction(line) == instruction


@pytest.mark.parametrize(
    "instruction,result",
    [
        (("nop", 0), (1, 0)),
        (("acc", 1), (1, 1)),
        (("jmp", 4), (4, 0)),
        (("acc", 3), (1, 3)),
        (("jmp", -3), (-3, 0)),
        (("acc", -99), (1, -99)),
    ],
)
def test_run_instruction(instruction, result):
    assert run_instruction(instruction, 0, 0) == result


@pytest.mark.parametrize(
    "program_string,instructions",
    [
        (
            TEST_DATA_SOLUTION_01,
            (
                ("nop", 0),
                ("acc", 1),
                ("jmp", 4),
                ("acc", 3),
                ("jmp", -3),
                ("acc", -99),
                ("acc", 1),
                ("jmp", 4),
                ("acc", 6),
            ),
        ),
        ("acc 1\nacc 1\nacc 1", (("acc", 1), ("acc", 1), ("acc", 1))),
    ],
)
def test_parse_program(program_string, instructions):
    return parse_program(program_string) == instructions


@pytest.mark.parametrize(
    "program,steps,result",
    [
        (
            parse_program(
                "nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6\n"
            ),
            10,
            [
                (0, 0),
                (1, 0),
                (2, 1),
                (6, 1),
                (7, 2),
                (3, 2),
                (4, 5),
                (1, 5),
                (2, 6),
                (6, 6),
            ],
        ),
        (
            parse_program("acc +1\nacc +1\nacc +1"),
            10,
            [(0, 0), (1, 1), (2, 2), (-1, 3)],
        ),
    ],
)
def test_run_program(program, steps, result):
    assert list(islice(run_program(program), steps)) == result


@pytest.mark.parametrize(
    "program_source,steps,result",
    [
        (
            "test_solution_01.data",
            10,
            [
                (0, 0),
                (1, 0),
                (2, 1),
                (6, 1),
                (7, 2),
                (3, 2),
                (4, 5),
                (1, 5),
                (2, 6),
                (6, 6),
            ],
        )
    ],
)
def test_run_program_from_file(program_source, steps, result):
    assert list(islice(run_program_from_file(program_source), steps)) == result


@pytest.mark.parametrize(
    "program,result",
    [
        (parse_program(TEST_DATA_SOLUTION_01), (True, 5)),
        (parse_program(TERMINATING_PROGRAM), (False, 3)),
    ],
)
def test_detect_inifinite_loop(program, result):
    assert detect_infinite_loop(program) == result


@pytest.mark.parametrize(
    "program_file,result", [("test_solution_01.data", 5), ("input.data", 1816)]
)
def test_solution_01(program_file, result):
    assert solution_01(program_file) == result


@pytest.mark.parametrize(
    "program_file,result",
    [
        ("input.data", 1149),
    ],
)
def test_solution_02(program_file, result):
    assert solution_02(program_file) == result
