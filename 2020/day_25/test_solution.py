import pytest
from solution import encryption_key, loop_size, solution_01


@pytest.mark.parametrize("public_key,size", [(5764801, 8), (17807724, 11)])
def test_loop_size(public_key, size):
    assert loop_size(public_key) == size


@pytest.mark.parametrize(
    "pbk1,pbk2,expected", [(5764801, 17807724, 14897079), (17807724, 5764801, 14897079)]
)
def test_encryption_key(pbk1, pbk2, expected):
    assert encryption_key(pbk1, pbk2) == expected


def test_solution_01():
    assert solution_01() == 19924389
