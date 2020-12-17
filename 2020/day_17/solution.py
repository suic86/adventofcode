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
    sparse_matrix = {}
    with open(path) as fobj:
        for r, row in enumerate(map(str.rstrip, fobj)):
            for c, column in enumerate(row):
                if column == "#":
                    sparse_matrix[tuple(fill(dimensions, [r, c]))] = column
    return sparse_matrix


def next_state(state, dimensions=3):
    new_state = {}
    for cube, value in state.items():
        active = 0
        for ds in product((-1, 0, 1), repeat=dimensions):
            if not any(ds):
                continue

            neighbour = tuple(map(add, cube, ds))

            if neighbour not in state:
                if neighbour not in new_state:
                    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                    ac = 0
                    for t in product((-1, 0, 1), repeat=dimensions):
                        if not any(t):
                            continue

                        ac += state.get(tuple(map(add, neighbour, t)), ".") == "#"

                        if ac > 3:
                            break
                    else:
                        if ac == 3:
                            new_state[neighbour] = "#"
                continue

            if state[neighbour] == "#":
                active += 1

        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
        # Otherwise, the cube becomes inactive.
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        new_state[cube] = (
            "#" if (value == "#" and active in (2, 3) or active == 3) else "."
        )
    return new_state


def active_cell_count(state):
    return sum(value == "#" for value in state.values())


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
