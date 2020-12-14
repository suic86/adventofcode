import pytest
from solution import (
    generate_addresses,
    mask_address,
    memory_address_decoder,
    parse_instructions,
    parse_mask,
    read_data,
    run_converter,
    solution_01,
    solution_02,
)


def test_read_data():
    assert read_data("test_solution_01.data") == [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]


def test_parse_mask():
    assert parse_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == {
        1: 0,
        6: 1,
    }


def test_parse_instructions_with_parsed_mask():
    data = read_data("test_solution_01.data")
    assert parse_instructions(data, parsed_mask=True) == [
        ["mask", {1: 0, 6: 1}],
        ["mem", [8, 11]],
        ["mem", [7, 101]],
        ["mem", [8, 0]],
    ]


def test_parse_instructions_without_parsed_mask():
    data = read_data("test_solution_01.data")
    assert parse_instructions(data, parsed_mask=False) == [
        ["mask", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"],
        ["mem", [8, 11]],
        ["mem", [7, 101]],
        ["mem", [8, 0]],
    ]


def test_run_program():
    assert run_converter("test_solution_01.data") == {8: 64, 7: 101}


@pytest.mark.parametrize(
    "address,mask,masked_address",
    [
        (
            42,
            "000000000000000000000000000000X1001X",
            "000000000000000000000000000000X1101X",
        ),
        (
            26,
            "00000000000000000000000000000000X0XX",
            "00000000000000000000000000000001X0XX",
        ),
    ],
)
def test_mask_address(address, mask, masked_address):
    assert mask_address(address, mask) == masked_address


@pytest.mark.parametrize(
    "masked_address,addresses",
    [
        ("00000000000000000000000000000001X0XX", [16, 17, 18, 19, 24, 25, 26, 27]),
        ("000000000000000000000000000000X1101X", [26, 27, 58, 59]),
    ],
)
def test_generate_addresses(masked_address, addresses):
    assert generate_addresses(masked_address) == addresses


def test_memory_address_decoder():
    assert memory_address_decoder("test_solution_02.data") == {
        16: 1,
        17: 1,
        18: 1,
        19: 1,
        24: 1,
        25: 1,
        26: 1,
        27: 1,
        58: 100,
        59: 100,
    }


@pytest.mark.parametrize(
    "source,expected", [("test_solution_01.data", 165), ("input.data", 8566770985168)]
)
def test_solution_01(source, expected):
    assert solution_01(source) == expected


@pytest.mark.parametrize(
    "source,expected", [("test_solution_02.data", 208), ("input.data", 4832039794082)]
)
def test_solution_02(source, expected):
    assert solution_02(source) == expected
