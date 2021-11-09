from re import compile

SECONDS = 2503

PARSER = compile(r"\d+")


def parse_data(path):
    with open(path) as fobj:
        return [list(map(int, PARSER.findall(line))) for line in fobj]


def calculate_distance(speed, fly, rest, time):
    full, partial = divmod(time, fly + rest)
    f, p = divmod(partial, fly)
    return (full * fly + (fly if f else p)) * speed


def calculate_points(reindeers, seconds):
    points = [0 for _ in reindeers]
    for second in range(1, seconds):
        distances = [calculate_distance(*r, second) for r in reindeers]
        lead_distance = max(distances)
        for reindeer, distance in enumerate(distances):
            if distance == lead_distance:
                points[reindeer] += 1
    return max(points)


def solution_01(path="input.data"):
    return max(calculate_distance(*data, SECONDS) for data in parse_data(path))


def solution_02(path="input.data"):
    return calculate_points(reindeers=parse_data(path), seconds=SECONDS)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
