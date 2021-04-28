from solution import (
    count_lights,
    grid,
    parse_instruction,
    process_grid_01,
    process_grid_02,
    solution_01,
    solution_02,
)


import pytest


@pytest.mark.parametrize(
    "instruction,parsed",
    [
        ["turn on 489,959 through 759,964", ["on", 489, 959, 759, 964]],
        ["turn off 820,516 through 871,91", ["off", 820, 516, 871, 91]],
        ["toggle 120,314 through 745,489", ["toggle", 120, 314, 745, 489]],
    ],
)
def test_parse_instruction(instruction, parsed):
    assert parse_instruction(instruction) == parsed


@pytest.mark.parametrize(
    "instructions,lights_count",
    [
        [["turn on 0,0 through 999,999"], 1000000],
        [["toggle 0,0 through 999,0"], 1000],
        [["turn on 499,499 through 500,500"], 4],
    ],
)
def test_process_grid_01(instructions, lights_count):
    assert (
        count_lights(process_grid_01(map(parse_instruction, instructions), grid()))
        == lights_count
    )


@pytest.mark.parametrize(
    "instructions,lights_count",
    [
        [["turn on 0,0 through 0,0"], 1],
        [["toggle 0,0 through 999,999"], 2000000],
    ],
)
def test_process_grid_02(instructions, lights_count):
    assert (
        count_lights(process_grid_02(map(parse_instruction, instructions), grid()))
        == lights_count
    )


def test_solution_01():
    assert solution_01() == 569999


def test_solution_02():
    assert solution_02() == 17836115
