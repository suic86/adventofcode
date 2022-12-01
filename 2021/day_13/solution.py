from operator import itemgetter


def load_data(path="input.data"):
    folds = []
    coordinates = set()
    before_separator = True
    with open(path) as fobj:
        for row in map(str.strip, fobj):
            if not row:
                before_separator = False
                continue
            if before_separator:
                coordinates.add(tuple(map(int, row.split(","))))
            else:
                axis, value = row.replace("fold along ", "").split("=")
                folds.append((axis, int(value)))
    return coordinates, folds


def fold(coordinates, axis, value):
    new_data = set()
    if axis == "y":
        for x, y in coordinates:
            if y != value:
                new_data.add((x, 2 * value - y if y > value else y))
    elif axis == "x":
        for x, y in coordinates:
            if x != value:
                new_data.add(((2 * value - x) if x > value else x, y))
    else:
        raise ValueError(f"Axis must be x or y but got {axis}.")
    return new_data


def draw_folded(coordinates, folds):
    for axis, value in folds:
        coordinates = fold(coordinates, axis, value)

    mx = max(map(itemgetter(0), coordinates))
    my = max(map(itemgetter(1), coordinates))

    folded_paper = [[" "] * (mx + 1) for _ in range(my + 1)]
    for x, y in coordinates:
        folded_paper[y][x] = "\u2588"

    return "\n".join(map("".join, folded_paper))


def solution_01(path="input.data"):
    coordinates, folds = load_data(path)
    axis, value = folds[0]
    return len(fold(coordinates, axis, value))


def solution_02(path="input.data"):
    return draw_folded(*load_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    # Look at solution_02_input_data_result.txt.
    # It contains the drawn page after all folds.
    print("Solution 02: 'BFKRCJZU'")
