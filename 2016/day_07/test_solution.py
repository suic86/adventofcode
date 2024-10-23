import pytest
from solution import solution_01, solution_02, ssl_support, tls_support


@pytest.mark.parametrize(
    "address,expected",
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
        (
            "lrqapqafjqfroqz[zenrntyrnrjtuij]kaewwkrjpcmeylerv[camcigwjgpyeaqg]wpkzihyjlcquzrg[ttfagxotubvfeiqkg]amqnhawihumfajhvd",
            False,
        ),
    ],
)
def test_ssl_support(address: str, expected: bool) -> None:
    assert ssl_support(address) == expected


@pytest.mark.parametrize(
    "address,expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
        (
            "lrqapqafjqfroqz[zenrntyrnrjtuij]kaewwkrjpcmeylerv[camcigwjgpyeaqg]wpkzihyjlcquzrg[ttfagxotubvfeiqkg]amqnhawihumfajhvd",
            False,
        ),
    ],
)
def test_tls_support(address: str, expected: bool) -> None:
    assert tls_support(address) == expected


def test_solution_01():
    assert solution_01() == 110


def test_solution_02():
    assert solution_02() == 242
