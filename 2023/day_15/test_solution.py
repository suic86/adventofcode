import pytest

from solution import aoc_hash, solution_01, solution_02, sort_lens


@pytest.mark.parametrize(
    "instruction,hash",
    [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_aoc_hash(instruction: str, hash: int) -> None:
    assert aoc_hash(instruction) == hash


def test_sort_lens() -> None:
    instructions = [
        "rn=1",
        "cm-",
        "qp=3",
        "cm=2",
        "qp-",
        "pc=4",
        "ot=9",
        "ab=5",
        "pc-",
        "pc=6",
        "ot=7",
    ]
    boxes = {0: [("rn", 1), ("cm", 2)], 1: [], 3: [("ot", 7), ("ab", 5), ("pc", 6)]}
    assert sort_lens(instructions) == boxes


@pytest.mark.parametrize("path,hash_sum", [("test.data", 1320), ("input.data", 511498)])
def test_solution_01(path: str, hash_sum: int) -> None:
    assert solution_01(path) == hash_sum


@pytest.mark.parametrize("path,expected", [("test.data", 145), ("input.data", 284674)])
def test_solution_02(path: str, expected: int) -> None:
    assert solution_02(path) == expected
