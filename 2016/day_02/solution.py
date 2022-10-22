def parse_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        return list(map(str.strip, fobj))


KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

ALNUMPAD = [
    ["*", "*", "1", "*", "*"],
    ["*", "2", "3", "4", "*"],
    ["5", "6", "7", "8", "9"],
    ["*", "A", "B", "C", "*"],
    ["*", "*", "D", "*", "*"],
]

MOVES = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def decode_digit(
    instruction: str, starting_position: tuple[int, int]
) -> tuple[str, tuple[int, int]]:
    x, y = starting_position
    for move in instruction:
        dx, dy = MOVES[move]
        if not (0 <= x + dx < 3) or not (0 <= y + dy < 3):
            continue
        x += dx
        y += dy

    return KEYPAD[y][x], (x, y)


def decode_alnum_code(
    instruction: str, starting_position: tuple[int, int]
) -> tuple[str, tuple[int, int]]:
    x, y = starting_position
    for move in instruction:
        dx, dy = MOVES[move]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 5) or not (0 <= ny < 5):
            continue
        if ALNUMPAD[ny][nx] == "*":
            continue
        x, y = nx, ny

    return ALNUMPAD[y][x], (x, y)


def solution_01(path: str = "input.data") -> int:
    starting_position = (1, 1)
    digits = []
    for instruction in parse_data(path):
        digit, starting_position = decode_digit(instruction, starting_position)
        digits.append(digit)
    return int("".join(digits))


def solution_02(path: str = "input.data") -> str:
    starting_position = (0, 2)
    alnum_code = []
    for instruction in parse_data(path):
        alnum, starting_position = decode_alnum_code(instruction, starting_position)
        alnum_code.append(alnum)
    return "".join(alnum_code)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
