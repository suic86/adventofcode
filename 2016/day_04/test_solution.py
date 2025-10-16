import pytest
from solution import Room, decrypt_name, is_real, load_data, solution_01, solution_02

PARSED: list[Room] = [
    Room(["aaaaa", "bbb", "z", "y", "x"], 123, "abxyz"),
    Room(["a", "b", "c", "d", "e", "f", "g", "h"], 987, "abcde"),
    Room(["not", "a", "real", "room"], 404, "oarel"),
    Room(["totally", "real", "room"], 200, "decoy"),
]


def test_load_data():
    assert load_data("test.data") == PARSED


@pytest.mark.parametrize("room, expected", zip(PARSED, (True, True, True, False)))
def test_is_real(room: Room, expected: bool) -> None:
    assert is_real(room) == expected


def test_decrypt_name() -> None:
    assert (
        decrypt_name(Room(["qzmt", "zixmtkozy", "ivhz"], 343, ""))
        == "very encrypted name"
    )


@pytest.mark.parametrize(
    "source,expected", [("test.data", 1514), ("input.data", 245102)]
)
def test_solution_01(source: str, expected: int) -> None:
    assert solution_01(source) == expected


def test_solution_02() -> None:
    assert solution_02() == 324
