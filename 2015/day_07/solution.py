from operator import and_, lshift, or_, rshift

MAXINT = 65535


def load_board(path="input.data"):
    with open(path) as fobj:
        return dict(line.split(" -> ")[::-1] for line in map(str.strip, fobj))


def evaluate_board(board):
    evaluated = set()

    def eval_bin(v, op, f):
        l, r = v.split(f" {op} ")
        if l.isnumeric() and r.isnumeric():
            board[k] = f(int(l), int(r))
            evaluated.add(k)
        elif l.isnumeric() and (r in evaluated):
            board[k] = f(int(l), board[r])
            evaluated.add(k)
        elif (l in evaluated) and r.isnumeric():
            board[k] = f(board[l], int(r))
            evaluated.add(k)
        elif l in evaluated and r in evaluated:
            board[k] = f(board[l], board[r])
            evaluated.add(k)

    while len(evaluated) != len(board):
        for k, v in board.items():
            if k in evaluated:
                continue

            if v.isnumeric():
                board[k] = int(v)
                evaluated.add(k)
            elif "NOT" in v:
                _, x = v.split()
                if x.isnumeric():
                    board[k] = MAXINT - int(x)
                    evaluated.add(k)
                elif x in evaluated:
                    board[k] = MAXINT - board[x]
                    evaluated.add(k)
            elif "AND" in v:
                eval_bin(v, "AND", and_)
            elif "OR" in v:
                eval_bin(v, "OR", or_)
            elif "RSHIFT" in v:
                eval_bin(v, "RSHIFT", rshift)
            elif "LSHIFT" in v:
                eval_bin(v, "LSHIFT", lshift)
            elif v in evaluated:
                board[k] = board[v]
                evaluated.add(k)
    return board


def solution_01(path="input.data"):
    board = load_board(path)
    return evaluate_board(board)["a"]


def solution_02(path="input.data"):
    a = evaluate_board(load_board(path))["a"]
    board = load_board(path)
    board["b"] = str(a)
    return evaluate_board(board)["a"]


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
