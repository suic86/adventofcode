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
def adjacent_seats(column_count, row_count, column, row):
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [
        (adjacent_column, adjacent_row)
        for row_difference, column_difference in adjacents
        if 0 <= (adjacent_column := column + column_difference) < column_count
        and 0 <= (adjacent_row := row + row_difference) < row_count
    ]


def next_area_state(area):
    column_count, row_count = len(area[0]), len(area)
    new_state = [[None for _ in range(column_count)] for _ in range(row_count)]
    for row in range(row_count):
        for column in range(column_count):
            new_state[row][column] = next_seat_state(
                area[row][column],
                [
                    area[adjacent_row][adjacent_column]
                    for adjacent_column, adjacent_row in adjacent_seats(
                        column_count, row_count, column, row
                    )
                ],
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
