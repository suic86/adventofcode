from functools import cache
from operator import add
from re import compile

Point = tuple[int, int, int, int]


def load_data(path="input.data"):
    # position=< 9,  1> velocity=< 0,  2>
    parser = compile(r"(-?\d+)")
    with open(path) as fobj:
        return tuple(tuple(map(int, parser.findall(line))) for line in fobj)


@cache
def find_message(points: tuple[Point], max_seconds: int = 11000) -> tuple[str, int]:
    xs, ys, dxs, dys = map(list, zip(*points))
    board: list[list[str]] = []
    seconds: int = 0
    for s in range(1, max_seconds + 1):
        xs = tuple(map(add, xs, dxs))
        ys = tuple(map(add, ys, dys))
        mnx, mny = min(xs), min(ys)
        mxx, mxy = max(xs), max(ys)
        if abs(mxy - mny) <= 9:
            board = [[" " for _ in range(mxx - mnx + 1)] for _ in range(mxy - mny + 1)]
            for y, x in zip(ys, xs):
                board[y - mny][x - mnx] = "#"
            seconds = s
    return "\n".join(map("".join, board)), seconds


def solution_01(path: str = "input.data") -> str:
    return find_message(load_data(path))[0]


def solution_02(path: str = "input.data") -> int:
    return find_message(load_data(path))[1]


if __name__ == "__main__":
    print(f"Solution 01:\n{solution_01()}")
    print(f"Solution 02: {solution_02()}")
