from solution import supports_tls

import pytest


@pytest.mark.parametrize(
    "address,expected",
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_supports_tls(address: str, expected: bool) -> None:
    assert supports_tls(address) == expected
