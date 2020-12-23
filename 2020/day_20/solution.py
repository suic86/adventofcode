from collections import defaultdict, deque
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
        self._top = None
        self._bottom = None
        self._right = None
        self._left = None

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"Tile({self.id})"

    def __repr__(self):
        return f"Tile({self.id})"

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    @property
    def top(self):
        if self._top is None:
            self._top = self._data[0]
        return self._top

    @property
    def bottom(self):
        if self._bottom is None:
            self._bottom = self._data[-1]
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

    def _reset_borders(self):
        self._top = None
        self._bottom = None
        self._right = None
        self._left = None

    def _rot_clockwise(self, turns=1):
        data = self._data
        for _ in range(turns):
            data = list(map("".join, zip(*reversed(data))))
        self._data = data
        self._reset_borders()

    def vflip(self):
        self._data = self._data[::-1]
        self._reset_borders()

    def hflip(self):
        self._data = [row[::-1] for row in self._data]
        self._reset_borders()

    def rot90(self):
        self._rot_clockwise()
        self._reset_borders()

    def rot180(self):
        self._rot_clockwise(2)
        self._reset_borders()

    def rot270(self):
        self._rot_clockwise(3)
        self._reset_borders()


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


def classify_match(first, second):
    borders = ["top", "left", "bottom", "right"]
    for i, df in enumerate(first.borders):
        for j, ds in enumerate(second.borders):
            if df == ds:
                return borders[i], borders[j], False
            elif df[::-1] == ds:
                return borders[i], borders[j], True
    return None


def shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in graph[vertex] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None


def _get_with_same_lengths(paths):
    p1, p2, p3 = paths
    l1, l2, l3 = map(len, paths)
    if l1 == l2:
        return p1, p2
    elif l1 == l3:
        return p1, p3
    return p2, p3


def append_left(tile, to_tile):
    while True:
        border, adjacent, flipped = classify_match(tile, to_tile)
        if border == "left" and adjacent == "right":
            if flipped:
                tile.vflip()
            return tile
        tile.rot90()


def append_below(tile, to_tile):
    while True:
        border, adjacent, flipped = classify_match(tile, to_tile)
        if border == "top" and adjacent == "bottom":
            if flipped:
                tile.hflip()
            return tile
        tile.rot90()


def assemble_tiles(path="input.data"):
    data = read_data(path)
    mts = matching_tiles(data)

    corner_tiles = {k: v for k, v in mts.items() if len(v) == 2}
    perimeter_tiles = {k for k, v in mts.items() if len(v) < 4}

    perimeter_graph = {pt: mts[pt] & perimeter_tiles for pt in perimeter_tiles}

    # corner tile and adjacent tiles
    start = min(corner_tiles)
    start = Tile(start, data[start])
    first, second = (Tile(i, data[i]) for i in mts[start.id])

    # rotate corner tile until bottom and right borders become its matching borders
    while True:
        ms = {classify_match(start, first)[0], classify_match(start, second)[0]}
        if ms == {"bottom", "right"}:
            break
        start.rot90()

    paths_to_other_corners = [
        shortest_path(perimeter_graph, start.id, ct)
        for ct in corner_tiles
        if ct != start.id
    ]

    assert {classify_match(start, first)[0], classify_match(start, second)[0]} == {
        "bottom",
        "right",
    }

    left, top = _get_with_same_lengths(paths_to_other_corners)

    # HACK
    if path == "input.data":
        left, top = top, left

    # TODO: Fix this and replace the above hack with this
    # if classify_match(start, first)[0] == "right":
    #     if first.id in top:
    #         top, left = left, top
    # else:
    #     if first.id in left:
    #         top, left = left, top

    # image matrix
    tile_matrix = [[None for _ in range(len(top))] for _ in range(len(left))]
    tile_matrix[0][0] = start

    # collect top border
    for i, t in enumerate(top[1:], 1):
        t = Tile(t, data[t])
        append_left(t, tile_matrix[0][i - 1])
        tile_matrix[0][i] = t

    # collect left border
    for i, t in enumerate(left[1:], 1):
        t = Tile(t, data[t])
        append_below(t, tile_matrix[i - 1][0])
        tile_matrix[i][0] = t

    visited = set(top) | set(left)

    # fill the rest left-right top-down
    for c in range(1, len(top)):
        for r in range(1, len(left)):
            ti = mts[tile_matrix[r - 1][c].id] & mts[tile_matrix[r][c - 1].id] - visited
            assert len(ti) == 1
            ti = ti.pop()
            visited.add(ti)
            t = Tile(ti, data[ti])
            append_left(t, tile_matrix[r][c - 1])
            tile_matrix[r][c] = t

    return tile_matrix


def assemble_image(tile_matrix):
    collected = [[trim_borders(column.data) for column in row] for row in tile_matrix]
    assembled = []
    for row in collected:
        merged_rows = ["".join(column[i] for column in row) for i in range(len(row[0]))]
        assembled += merged_rows
    return assembled


def find_monsters(image):
    image = Tile(0, image)
    for _ in range(4):
        image.rot90()
        c = count_monsters(image.data)
        if c != 0:
            return c

    image.hflip()
    for _ in range(4):
        image.rot90()
        c = count_monsters(image.data)
        if c != 0:
            return c

    image.hflip()
    image.vflip()

    for _ in range(4):
        image.rot90()
        c = count_monsters(image.data)
        if c != 0:
            return c

    image.hflip()
    for _ in range(4):
        c = count_monsters(image.data)
        if c != 0:
            return c

    raise ValueError("No monsters found.")


def solution_02(path="input.data"):
    image = assemble_image(assemble_tiles(path))
    hash_count = sum(row.count("#") for row in image)
    monster_hash_count = sum(row.count("#") for row in MONSTER)
    mc = find_monsters(image)
    return hash_count - monster_hash_count * mc


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
