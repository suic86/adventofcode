from collections import defaultdict
from functools import reduce
from itertools import product, starmap
from operator import mul


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
    return (
        first == second
        or first[::-1] == second
        or first == second[::-1]
    )


class Tile:
    def __init__(self, id, data):
        self._id = id
        self._data = data
        self._top = data[0]
        self._bottom = data[-1]
        self._left = None
        self._right = None

    def __hash__(self):
        return hash(self._id) 

    def __eq__(self, other):
        return self.id == other.id 

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    @property    
    def top(self):
        return self._top

    @property
    def bottom(self):
        return self._bottom

    @property
    def left(self):
        if self._left is None:
            self._left = "".join(row[0] for row in self.data)
        return self._left

    @property
    def right(self):
        if self._right is None:
            self._right = "".join(row[-1] for row in self.data)
        return self._right

    @property
    def borders(self):
        return [self.top, self.left, self.bottom, self.right]    

    def match_any_border(self, other):
        return any(starmap(is_match, product(self.borders, other.borders)))


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
    corner_tiles = [tile for tile, matching in matching_tiles(read_data(path)).items() if len(matching) == 2]
    return prod(corner_tiles)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
