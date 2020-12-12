#!/usr/bin/env python3

from util import read_data, EMPTY, OCCUPIED


def next_seat_state(current_seat, adjacent_seats):
    if current_seat == EMPTY and OCCUPIED not in adjacent_seats:
        return OCCUPIED
    elif current_seat == OCCUPIED and adjacent_seats.count(OCCUPIED) >= 5:
        return EMPTY
    return current_seat


def visible_adjacent_seats(area, seat_column, seat_row, column_count, row_count):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = []
    for column_difference, row_difference in directions:
        column, row = seat_column, seat_row
        while (
            0 <= (column := column + column_difference) < column_count
            and 0 <= (row := row + row_difference) < row_count
        ):
            if (seat_state := area[row][column]) in {OCCUPIED, EMPTY}:
                result.append(seat_state)
                break
    return result


def next_area_state(area):
    column_count, row_count = len(area[0]), len(area)
    new_state = [[None for _ in range(column_count)] for _ in range(row_count)]
    for row in range(row_count):
        for column in range(column_count):
            new_state[row][column] = next_seat_state(
                area[row][column],
                visible_adjacent_seats(area, column, row, column_count, row_count),
            )
    return new_state


def solution_02(path="input.data"):
    area = read_data(path)
    while True:
        if (new_area := next_area_state(area)) == area:
            break
        area = new_area
    return sum(row.count(OCCUPIED) for row in new_area)


if __name__ == "__main__":
    print("Solution 02:", solution_02())
