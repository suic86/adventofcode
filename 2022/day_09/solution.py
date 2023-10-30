def parse_data(path="input.data"):
    with open(path) as fobj:
        return [(d, int(v)) for d, v in map(str.split, map(str.strip, fobj))]


def update_rope(rope, motion):
    dr, dc = motion
    hr, hc = rope[0]
    h = [hr + dr, hc + dc]
    new_rope = [h]

    for t in rope[1:]:
        dr = h[0] - t[0]
        dc = h[1] - t[1]
        if abs(dr) == 2 and abs(dc) == 2:
            t[0] += dr // 2
            t[1] += dc // 2
        elif abs(dr) == 2:
            t[0] += dr // 2
            t[1] += dc
        elif abs(dc) == 2:
            t[0] += dr
            t[1] += dc // 2
        new_rope.append(t)
        h = t
    return new_rope


def simulate(motions, length=10):
    knots = [[0, 0] for _ in range(length)]
    visited = {tuple(knots[-1])}
    ds = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for d, v in motions:
        motion = ds[d]
        for _ in range(v):
            knots = update_rope(knots, motion)
            visited.add(tuple(knots[-1]))
    return len(visited)


def solution_01(path="input.data"):
    return simulate(parse_data(path), length=2)


def solution_02(path="input.data"):
    return simulate(parse_data(path), length=10)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
