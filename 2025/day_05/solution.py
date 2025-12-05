def parse_data(path: str = "input.data", part1=True):
    ranges = set()
    with open(path) as fp:
        for line in map(str.strip, fp):
            if line == "":
                break
            ranges.add(tuple(map(int, line.split("-"))))
        return (ranges, list(map(int, map(str.strip, fp))) if part1 else [])


def solution_01(path: str = "input.data") -> int:
    ranges, ingredients = parse_data(path)
    return sum(any(u <= i <= l for u, l in ranges) for i in ingredients)


def solution_02(path: str = "input.data") -> int:
    ranges, _ = parse_data(path, part1=False)
    ranges = sorted(ranges, reverse=True)
    merged = []
    to_merge = None
    while ranges:
        if to_merge is None:
            to_merge = list(ranges.pop())
            continue

        tu, tl = to_merge
        u, l = ranges.pop()

        # upper bound inside existing range or adjacent ranges
        if tu <= u <= tl or tu + 1 == l:
            to_merge = [tu, max(tl, l)]
            continue

        # no overlap
        merged.append(to_merge)
        ranges.append((u, l))
        to_merge = None

    if to_merge is not None:
        merged.append(to_merge)

    return sum(u - l + 1 for l, u in merged)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
