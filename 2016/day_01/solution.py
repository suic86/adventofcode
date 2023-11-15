from collections import deque


def load_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        data = fobj.read()
    return data.strip().split(", ")


DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class directions:
    def __init__(self):
        self.ds = deque(DIRECTIONS)

    def next(self, rotation: str) -> tuple[int, int]:
        if rotation == "L":
            self.ds.rotate(-1)
        elif rotation == "R":
            self.ds.rotate(1)
        else:
            raise ValueError(f"Invalid rotation {rotation}. Must be L or R")
        return self.ds[0]


def calculate_distance(moves: list[str]) -> int:
    ds = directions()
    x = y = 0
    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        dx, dy = ds.next(direction)
        x += distance * dx
        y += distance * dy
    return abs(x) + abs(y)


def first_visited_twice(moves: list[str]) -> tuple[int, int]:
    ds = directions()
    x = y = 0
    visited = {(0, 0)}
    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        dx, dy = ds.next(direction)
        for _ in range(distance):
            x += dx
            y += dy
            t = (x, y)
            if t in visited:
                return t
            visited.add(t)
    raise ValueError("Invalid input. No location visited twice.")


def solution_01():
    return calculate_distance(load_data())


def solution_02():
    return sum(map(abs, first_visited_twice(load_data())))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
