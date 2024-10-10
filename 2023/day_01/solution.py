def process_line(line: str, part_two: bool = False) -> int:
    parsed: list[str] = []
    for i, c in enumerate(line):
        if c.isdigit():
            parsed.append(c)
        elif part_two:
            for j, n in enumerate(
                [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ],
                start=1,
            ):
                if line[i:].startswith(n):
                    parsed.append(str(j))
                    break
    return int("".join([parsed[0], parsed[-1]]))


def parse_data(path: str = "input.data", part_two: bool = False) -> list[int]:
    with open(path) as fobj:
        return [process_line(line, part_two) for line in map(str.strip, fobj)]


def solution_01(path: str = "input.data") -> int:
    return sum(parse_data(path, part_two=False))


def solution_02(path: str = "input.data") -> int:
    return sum(parse_data(path, part_two=True))


if __name__ == "__main__":
    print(f"Solution_01: {solution_01()}")
    print(f"Solution_02: {solution_02()}")
