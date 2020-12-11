#!/usr/bin/env python3

from util import read_data, EMPTY, OCCUPIED


def next_seat_state(current_seat, adjacent_seats):
    if current_seat == EMPTY and OCCUPIED not in adjacent_seats:
        return OCCUPIED
    elif current_seat == OCCUPIED and adjacent_seats.count(OCCUPIED) >= 4:
        return EMPTY
    return current_seat


def adjacent_seats(x_size, y_size, x, y):
    return (
        (x_i, y_i)
        for x_i in range(max(x - 1, 0), min(x + 2, x_size))
        for y_i in range(max(y - 1, 0), min(y + 2, y_size))
        if x_i != x or y_i != y
    )


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
