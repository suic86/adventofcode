import pytest

from solution import find_marker, solution_01, solution_02


@pytest.mark.parametrize(
    "buffer,marker",
    [
        ("abcdefgh", 4),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_find_marker_packet(buffer, marker):
    assert find_marker(buffer, chunk_size=4) == marker


@pytest.mark.parametrize(
    "buffer,marker",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_find_marker_message(buffer, marker):
    assert find_marker(buffer, chunk_size=14) == marker


def test_solution_01():
    assert solution_01() == 1282


def test_solution_02():
    assert solution_02() == 3513
