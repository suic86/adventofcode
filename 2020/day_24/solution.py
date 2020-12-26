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
    return tiles


def next_day(tiles):
    to_flip = []
    new_tiles = {}

    for (q, r), color in tiles.items():
        new_tiles[(q, r)] = color
        for qd, rd in CONVERSION.values():
            if (q + qd, r + rd) not in tiles:
                new_tiles[(q + qd, r + rd)] = False

    for (q, r), color in new_tiles.items():
        adjacents = sum(
            new_tiles.get((q + qd, r + rd), 0) for qd, rd in CONVERSION.values()
        )
        # tile is black
        if color and (adjacents == 0 or adjacents > 2):
            to_flip.append((q, r))
        # tile is white
        elif not color and adjacents == 2:
            to_flip.append((q, r))

    for tile in to_flip:
        new_tiles[tile] = not new_tiles[tile]

    return new_tiles


def solution_01(path="input.data"):
    return sum(input_to_tiles(path).values())


def solution_02(path="input.data"):
    tiles = input_to_tiles(path)
    for _ in range(100):
        tiles = next_day(tiles)
    return sum(tiles.values())


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
