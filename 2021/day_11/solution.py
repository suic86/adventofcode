from itertools import count, islice


def load_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, iter(row.strip()))) for row in fobj]


def gen_steps(data):
    width = len(data[0])
    height = len(data)

    def adjacents(r, c):
        # fmt: off
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (0 <= r + dr < height) and (0 <= c + dc < width):
                yield r + dr, c + dc
        # fmt: on

    for _ in count():
        # First, the energy level of each octopus increases by 1.
        data = [[column + 1 for column in row] for row in data]
        flashed = set()
        for r in range(height):
            for c in range(width):
                if (r, c) in flashed or data[r][c] <= 9:
                    continue
                data[r][c] = 0
                flashed.add((r, c))
                stack = [(r, c)]
                while stack:
                    rc, cc = stack.pop()
                    # This increases the energy level of all adjacent octopuses by 1,
                    # including octopuses that are diagonally adjacent.
                    for ra, ca in adjacents(rc, cc):
                        # An octopus can only flash at most once per step.
                        if (ra, ca) not in flashed:
                            data[ra][ca] += 1
                    for ra, ca in adjacents(rc, cc):
                        # If this causes an octopus to have an energy level greater than 9, it also flashes.
                        # An octopus can only flash at most once per step.
                        if (ra, ca) not in flashed and data[ra][ca] > 9:
                            data[ra][ca] = 0
                            flashed.add((ra, ca))
                            stack.append((ra, ca))
        yield len(flashed)


def solution_01(path="input.data"):
    return sum(islice(gen_steps(load_data(path)), 100))


def solution_02(path="input.data"):
    data = load_data(path)
    all_octopi = len(data) * len(data[0])
    return next(
        i for i, flashes in enumerate(gen_steps(data), 1) if flashes == all_octopi
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01('input.data')}")
    print(f"Solution 02: {solution_02('input.data')}")
