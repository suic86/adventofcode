import pytest

from solution import (
    cancel_characters,
    clean_garbage,
    count_groups,
    count_garbage,
    solution_01,
    solution_02,
)


@pytest.mark.parametrize(
    "stream,cleaned",
    [
        ("<>", "<>"),
        ("<random characters>", "<random characters>"),
        ("<<<<>", "<<<<>"),
        ("<{!>}>", "<{}>"),
        ("<!!>", "<>"),
        ("<!!!>>", "<>"),
        ('<{o"i!a,<{i<a>', '<{o"i,<{i<a>'),
        ("{{<!>},{<!>},{<!>},{<a>}}", "{{<},{<},{<},{<a>}}"),
    ],
)
def test_cancel_characters(stream, cleaned):
    assert cancel_characters(stream) == cleaned


@pytest.mark.parametrize(
    "stream,cleaned",
    [
        ("<>", ""),
        ("<random characters>", ""),
        ("<<<<>", ""),
        ("{{<},{<},{<},{<a>}}", "{{}}"),
    ],
)
def test_remove_garbage(stream, cleaned):
    assert clean_garbage(stream) == cleaned


@pytest.mark.parametrize(
    "stream,group_count",
    [
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ],
)
def test_count_groups(stream, group_count):
    assert count_groups(stream) == group_count


@pytest.mark.parametrize(
    "stream,garbage_count",
    [
        ("<>", 0),
        ("<random characters>", 17),
        ("<<<<>", 3),
        ("<{!>}>", 2),
        ("<!!>", 0),
        ("<!!!>>", 0),
        ('<{o"i!a,<{i<a>', 10),
    ],
)
def test_count_garbage(stream, garbage_count):
    assert count_garbage(stream) == garbage_count


def test_solution_01():
    assert solution_01() == 12897


def test_solution_02():
    assert solution_02() == 7031
