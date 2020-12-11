#!/usr/bin/env python3

from util import read_data, EMPTY, OCCUPIED


def next_seat_state(current_seat, adjacent_seats):
    if current_seat == EMPTY and OCCUPIED not in adjacent_seats:
        return OCCUPIED
    elif current_seat == OCCUPIED and adjacent_seats.count(OCCUPIED) >= 5:
        return EMPTY
    return current_seat


def visible_adjacent_seats(area, x, y):
    x_size, y_size = len(area[0]), len(area)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = []
    for xd, yd in directions:
        xi, yi = x, y
        while True:
            xi += xd
            yi += yd
            if not (0 <= xi < x_size and 0 <= yi < y_size):
                break
            if area[yi][xi] in (OCCUPIED, EMPTY):
                result.append((xi, yi))
                break
    return result


def next_area_state(area):
    x_size, y_size = len(area[0]), len(area)
    new_state = [[None for _ in range(x_size)] for _ in range(y_size)]
    for y in range(y_size):
        for x in range(x_size):
            new_state[y][x] = next_seat_state(
                area[y][x],
                [area[j][i] for i, j in visible_adjacent_seats(area, x, y)],
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
