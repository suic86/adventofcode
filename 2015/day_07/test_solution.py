from solution import load_board, evaluate_board, solution_01, solution_02


def test_load_board_test_data():
    expected = {
        "x": "123",
        "y": "456",
        "d": "x AND y",
        "e": "x OR y",
        "f": "x LSHIFT 2",
        "g": "y RSHIFT 2",
        "h": "NOT x",
        "i": "NOT y",
    }
    assert load_board("test.data") == expected


def test_load_board_input_data():
    board = load_board("input.data")
    assert len(board) == 339
    assert board["a"] == "lx"
    assert board["ca"] == "bn AND by"


def test_evaluate_board():
    board = load_board("test.data")
    expected = {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
    assert evaluate_board(board) == expected


def test_solution_01():
    assert solution_01() == 3176


def test_solution_01():
    assert solution_02() == 14710
