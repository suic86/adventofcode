from itertools import product
from operator import add


def fill(size, lst, fillvalue=0):
    if len(lst) > size:
        return lst
    result = [fillvalue for _ in range(size)]
    for i, v in enumerate(lst):
        result[i] = v
    return result


def read_data(path="input.data", dimensions=3):
    active_cubes = set()
    with open(path) as fobj:
        for r, row in enumerate(map(str.rstrip, fobj)):
            for c, column in enumerate(row):
                if column == "#":
                    active_cubes.add(tuple(fill(dimensions, [r, c])))
    return active_cubes


def next_state(state, dimensions=3):
    new_state = set()
    for cube in state:
        active = 0
        for ds in product((-1, 0, 1), repeat=dimensions):
            if not any(ds):
                continue

            neighbour = tuple(map(add, cube, ds))

            if neighbour in state:
                active += 1
                continue

            if neighbour not in new_state:
                # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                ac = 0
                for t in product((-1, 0, 1), repeat=dimensions):
                    if not any(t):
                        continue

                    ac += tuple(map(add, neighbour, t)) in state

                    if ac > 3:
                        break
                else:
                    if ac == 3:
                        new_state.add(neighbour)

        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        # Otherwise, the cube becomes inactive.
        if active == 2 or active == 3:
            new_state.add(cube)
    return new_state


def active_cell_count(state):
    return len(state)


def solution_01(path="input.data"):
    state = read_data(path)
    for _ in range(6):
        state = next_state(state)
    return active_cell_count(state)


def solution_02(path="input.data"):
    state = read_data(path, dimensions=4)
    for _ in range(6):
        state = next_state(state, dimensions=4)
    return active_cell_count(state)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
