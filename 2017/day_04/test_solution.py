import pytest
from solution import is_valid, solution_01, solution_02


@pytest.mark.parametrize(
    "passphrase,valid",
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
)
def test_is_valid(passphrase, valid):
    assert is_valid(passphrase) == valid


@pytest.mark.parametrize(
    "passphrase,valid",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test_is_valid_anagram_key(passphrase, valid):
    anagram_key = lambda p: "".join(sorted(p))
    assert is_valid(passphrase, key=anagram_key) == valid


def test_solution_01():
    assert solution_01() == 325


def test_solution_02():
    assert solution_02() == 119
