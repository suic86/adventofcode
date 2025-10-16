from collections import deque
from re import compile

PARSER = compile(r"(?P<direction>[NSEWLRF])(?P<distance>\d+)")


def read_data(path="input.data"):
    with open(path) as source_file:
        return list(map(parse_action, source_file))


def parse_action(instruction):
    direction, distance = PARSER.fullmatch(instruction.rstrip()).groups()
    return direction, int(distance)


def solution_01(path="input.data"):
    directions = "ESWN"
    distances = dict.fromkeys(directions, 0)
    # direction pointer
    p = 0
    for d, v in read_data(path):
        if d in directions:
            distances[d] += v
        elif d == "F":
            distances[directions[p]] += v
        elif d == "R":
            p = (p + v // 90) % 4
        elif d == "L":
            p = (p - v // 90) % 4
    return abs(distances["N"] - distances["S"]) + abs(distances["E"] - distances["W"])


def solution_02(path="input.data"):
    directions = "ESWN"
    waypoint = deque([10, 0, 0, 1])
    distances = [0, 0, 0, 0]

    for d, v in read_data(path):
        if d in directions:
            waypoint[directions.index(d)] += v
        elif d == "R":
            waypoint.rotate(v // 90)
        elif d == "L":
            waypoint.rotate(-v // 90)
        elif d == "F":
            distances = [i + j * v for i, j in zip(distances, waypoint)]
    return abs(distances[0] - distances[2]) + abs(distances[1] - distances[3])


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
