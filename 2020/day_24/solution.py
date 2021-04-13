from collections import defaultdict
from re import compile

PARSER = compile(r"(e|se|sw|w|nw|ne)").findall

# See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
CONVERSION = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1),
}
ADJACENTS = list(CONVERSION.values())


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(PARSER, map(str.rstrip, fobj)))


def steps_to_tile(steps):
    r, q = 0, 0
    for rd, qd in map(CONVERSION.get, steps):
        r += rd
        q += qd
    return r, q


def input_to_tiles(path="input.data"):
    tiles = defaultdict(bool)
    for tile in map(steps_to_tile, read_data(path)):
        tiles[tile] = not tiles[tile]
    return {k for k, v in tiles.items() if v}


def next_day(tiles):
    new_tiles = set()

    for (q, r) in tiles:
        adj = sum((q + qd, r + rd) in tiles for qd, rd in ADJACENTS)
        if not (adj == 0 or adj > 2):
            new_tiles.add((q, r))

    adjacents = {
        adj
        for q, r in tiles
        for qd, rd in ADJACENTS
        if (adj := (q + qd, r + rd)) not in tiles
    }

    for (q, r) in adjacents:
        if sum((q + qd, r + rd) in tiles for qd, rd in ADJACENTS) == 2:
            new_tiles.add((q, r))

    return new_tiles


def solution_01(path="input.data"):
    return len(input_to_tiles(path))


def solution_02(path="input.data"):
    tiles = input_to_tiles(path)
    for _ in range(100):
        tiles = next_day(tiles)
    return len(tiles)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
