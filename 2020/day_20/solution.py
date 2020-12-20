from collections import defaultdict
from functools import reduce
from itertools import product, starmap
from operator import mul


MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


MHEIGHT = len(MONSTER)
MWIDTH = len(MONSTER[0])


def read_data(path="input.data"):
    tiles = defaultdict(list)
    with open(path) as fobj:
        tile = None
        for line in map(str.rstrip, fobj):
            if not line:
                continue
            if ":" in line:
                tile = int(line.split()[-1].rstrip(":"))
                continue
            tiles[tile].append(line)
    return tiles


def is_match(first, second):
    return first == second or first[::-1] == second or first == second[::-1]


class Tile:
    def __init__(self, id, data):
        self._id = id
        self._data = data
        self._operations = []

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"Tile({self.id})"

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    @property
    def top(self):
        return self._data[0]

    @property
    def bottom(self):
        return self._data[-1]

    @property
    def left(self):
        return "".join(row[0] for row in self.data)

    @property
    def right(self):
        return "".join(row[-1] for row in self.data)

    @property
    def borders(self):
        return [self.top, self.left, self.bottom, self.right]

    def match_any_border(self, other):
        return any(starmap(is_match, product(self.borders, other.borders)))

    def _rot_clockwise(self, turns=1):
        data = self._data
        for _ in range(turns):
            data = list(map("".join, zip(*reversed(data))))
        self._data = data
        self._operations.append((self._rot_counterclockwise, turns))

    def _rot_counterclockwise(self, turns=1):
        data = self._data
        for _ in range(turns):
            data = list(map("".join, (zip(*data))))[::-1]
        self._data = data

    def vflip(self):
        self._data = self._data[::-1]
        self._operations.append(self.vflip)

    def hflip(self):
        self._data = [row[::-1] for row in self._data]
        self._operations.append(self.hflip)

    def rot90(self):
        self._rot_clockwise()

    def rot180(self):
        self._rot_clockwise(2)

    def rot270(self):
        self._rot_clockwise(3)

    def revert(self):
        if not self._operations:
            return
        operation = self._operations.pop()
        if isinstance(operation, tuple):
            operation, *args = operation
            operation(*args)
        else:
            operation()


def matching_tiles(tiles):
    tiles = [Tile(tile_id, tile_data) for tile_id, tile_data in tiles.items()]
    matching = defaultdict(set)
    for first, second in product(tiles, repeat=2):
        if first == second:
            continue
        if first.match_any_border(second):
            matching[first.id].add(second.id)
    return matching


def prod(seq):
    return reduce(mul, seq, 1) if seq else 0


def solution_01(path="input.data"):
    corner_tiles = [
        tile
        for tile, matching in matching_tiles(read_data(path)).items()
        if len(matching) == 2
    ]
    return prod(corner_tiles)


def trim_borders(tile_data):
    return [row[1:-1] for row in tile_data[1:-1]]


def assemble_image(tile_matrix, tiles):
    collected = [[trim_borders(tiles[column]) for column in row] for row in tile_matrix]
    assembled = []
    for row in collected:
        merged_rows = ["".join(column[i] for column in row) for i in range(len(row[0]))]
        assembled += merged_rows
    return assembled


def count_monsters(image):
    monsters = 0
    for r in range(len(image) - MHEIGHT):
        for c in range(len(image[0]) - MWIDTH):
            monsters += all(
                MONSTER[dr][dc] == image[r + dr][c + dc]
                for dr in range(MHEIGHT)
                for dc in range(MWIDTH)
                if MONSTER[dr][dc] == "#"
            )
    return monsters


def clasify_match(first, second):
    borders = ["top", "left", "bottom", "right"]
    for i, df in enumerate(first.borders):
        for j, ds in enumerate(second.borders):
            if df == ds:
                return borders[i], borders[j], False
            elif df[::-1] == ds:
                return borders[i], borders[j], True
    return None


if __name__ == "__main__":
    print("Solution 01:", solution_01())
