#!/usr/bin/env python3

from functools import lru_cache
from util import read_data, EMPTY, OCCUPIED


def next_seat_state(current_seat, adjacent_seats):
    if current_seat == EMPTY and OCCUPIED not in adjacent_seats:
        return OCCUPIED
    elif current_seat == OCCUPIED and adjacent_seats.count(OCCUPIED) >= 4:
        return EMPTY
    return current_seat


@lru_cache(maxsize=8736)
def adjacent_seats(x_size, y_size, x, y):
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [
        (x_i, y_i)
        for x_d, y_d in adjacents
        if 0 <= (x_i := x + x_d) < x_size and 0 <= (y_i := y + y_d) < y_size
    ]


def next_area_state(area):
    x_size, y_size = len(area[0]), len(area)
    new_state = [[None for _ in range(x_size)] for _ in range(y_size)]
    for y in range(y_size):
        for x in range(x_size):
            new_state[y][x] = next_seat_state(
                area[y][x],
                [area[y_i][x_i] for x_i, y_i in adjacent_seats(x_size, y_size, x, y)],
            )
    return new_state


def solution_01(path="input.data"):
    area = read_data(path)
    while True:
        if (new_area := next_area_state(area)) == area:
            break
        area = new_area
    return sum(row.count(OCCUPIED) for row in new_area)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
