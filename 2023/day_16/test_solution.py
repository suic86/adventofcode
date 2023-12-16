import pytest

from solution import parse_data, show_layout, solution_01, solution_02


def test_show_data() -> None:
    with open("test.data") as fobj:
        data = fobj.read().rstrip()
    assert show_layout(parse_data("test.data")) == data


def test_parse_data_width_height() -> None:
    layout = parse_data("test.data")
    assert layout.height == 10
    assert layout.width == 10


def test_parse_data_objects() -> None:
    layout = parse_data("test.data")
    objs = layout.objects
    assert objs[(0, 1)] == "|"
    assert objs[(8, 6)] == "-"


@pytest.mark.parametrize("path,result", [("test.data", 46), ("input.data", 7067)])
def test_solution_01(path: str, result: int) -> None:
    assert solution_01(path) == result


def test_solution_02_test_data() -> None:
    assert solution_02("test.data") == 51


@pytest.mark.slow
def test_solution_02_input_data() -> None:
    assert solution_02("test.data") == 7324
