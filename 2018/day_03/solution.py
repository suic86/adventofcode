from re import compile

Claim = tuple[int, int, int, int, int]
Coord = tuple[int, int]

# input format: #1 @ 1,3: 4x4
PARSER = compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


def parse_data(path="input.data") -> list[Claim]:
    with open(path) as fobj:
        return [tuple(map(int, PARSER.fullmatch(line).groups())) for line in map(str.strip, fobj)]  # type: ignore


def inches(claims: list[Claim]) -> tuple[set[Coord], set[Coord]]:
    overlaping: set[Coord] = set()
    non_overlaping: set[Coord] = set()
    for _, x, y, w, h in claims:
        for dx in range(w):
            for dy in range(h):
                inch = (x + dx, y + dy)
                if inch in overlaping:
                    continue
                elif inch in non_overlaping:
                    overlaping.add(inch)
                    non_overlaping.remove(inch)
                else:
                    non_overlaping.add(inch)
    return overlaping, non_overlaping


def non_overlapping_claim(claims: list[Claim]) -> int:
    _, non_overlaping = inches(claims)
    for c, x, y, w, h in claims:
        if all(
            (x + dx, y + dy) in non_overlaping for dx in range(w) for dy in range(h)
        ):
            return c
    raise ValueError("Invalid input.")


def solution_01(path="input.data") -> int:
    overlapping, _ = inches(parse_data(path))
    return len(overlapping)


def solution_02(path="input.data") -> int:
    return non_overlapping_claim(parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
