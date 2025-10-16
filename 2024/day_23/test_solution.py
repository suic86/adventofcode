import pytest
from solution import solution_01, solution_02


@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", 7),
        ("input.data", 1368),
    ],
)
def test_solution_01(path, expected) -> None:
    assert solution_01(path) == expected


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "path,expected",
    [
        ("test.data", "co,de,ka,ta"),
        ("test_randomized.data", "co,de,ka,ta"),
        ("input.data", "dd,ig,il,im,kb,kr,pe,ti,tv,vr,we,xu,zi"),
        ("input_randomized.data", "dd,ig,il,im,kb,kr,pe,ti,tv,vr,we,xu,zi"),
    ],
)
def test_solution_02(path, expected) -> None:
    assert solution_02(path) == expected
