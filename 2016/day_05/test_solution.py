import pytest

from hashes import FIRST_PART, SECOND_PART
from solution import cinematic_hashes, hashes, solution_01, solution_02


@pytest.mark.slow()
def test_hashes() -> None:
    assert hashes() == FIRST_PART


@pytest.mark.slow()
def test_cinematic_hashes() -> None:
    assert cinematic_hashes() == SECOND_PART


@pytest.mark.slow()
def test_solution_01() -> None:
    assert solution_01() == "f97c354d"


@pytest.mark.slow()
def test_solution_02() -> None:
    assert solution_02() == "863dde27"
