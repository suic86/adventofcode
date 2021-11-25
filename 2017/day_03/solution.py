from math import ceil, sqrt
from itertools import islice
from urllib.request import urlopen


PUZZLE_INPUT = 289326


def spiral(number):
    """Generates the shorted spiral with more than 'number' of squares."""
    n = ceil(sqrt(number))

    x, y = 0, 0
    dx, dy = 0, -1

    for _ in range(n * n):
        if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1 - x:
            dx, dy = -dy, dx  # corner, change direction

        if abs(x) > n // 2 or abs(y) > n // 2:  # non-square
            dx, dy = -dy, dx  # change direction
            x, y = -y + dx, x + dy  # jump

        yield x, y

        x += dx
        y += dy


def distance(number):
    return sum(map(abs, next(islice(spiral(number), number - 1, number))))


def solution_01():
    return distance(PUZZLE_INPUT)


CACHED_TABLE = None


def solution_02():
    global CACHED_TABLE
    if CACHED_TABLE:
        table = CACHED_TABLE
    else:
        # Square spiral of sums of selected preceding terms, starting at 1.
        # Table of n, a(n) for n=1..961 by Klaus Brockhaus
        table = (
            urlopen("https://oeis.org/A141481/b141481.txt")
            .read()
            .decode("utf-8")
            .strip()
            .split("\n")
        )
        table = [int(row.split()[1]) for row in table if not row.startswith("#")]
        CACHED_TABLE = table

    for value in table:
        if value > PUZZLE_INPUT:
            return value


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
