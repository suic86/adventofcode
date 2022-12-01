from collections import defaultdict


def load_data(path="input.data"):
    numbers = []
    boards = []
    with open(path) as fobj:
        data = map(str.strip, fobj)
        numbers = list(map(int, next(data).split(",")))
        # skip first empty line
        next(data)
        board = []
        for row in data:
            if not row:
                boards.append(board)
                board = []
                continue
            board.append(list(map(int, row.split())))
        if board:
            boards.append(board)
    return numbers, boards


def has_bingo(columns, rows):
    return 5 in columns.values() or 5 in rows.values()


def bingo(numbers, boards, first=True):
    columns = defaultdict(lambda: defaultdict(int))
    rows = defaultdict(lambda: defaultdict(int))
    marked = defaultdict(set)
    with_bingo = set()
    board_count = len(boards)

    for called in numbers:
        for b, board in enumerate(boards):
            if b in with_bingo:
                continue
            for r, row in enumerate(board):
                for c, column in enumerate(row):
                    if column != called:
                        continue

                    columns[b][c] += 1
                    rows[b][r] += 1
                    marked[b].add((r, c))

                    if has_bingo(columns[b], rows[b]):
                        with_bingo.add(b)
                        if first or len(with_bingo) == board_count:
                            return called, marked[b], board


def calculate_score(called, marked, board):
    return called * sum(
        column
        for r, row in enumerate(board)
        for c, column in enumerate(row)
        if (r, c) not in marked
    )


def solution_01(path="input.data"):
    return calculate_score(*bingo(*load_data(path)))


def solution_02(path="input.data"):
    return calculate_score(*bingo(*load_data(path), False))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
