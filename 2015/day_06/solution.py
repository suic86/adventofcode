from operator import not_
from re import compile

INSTRUCTION_PARSER = compile(
    r"(?:turn )?(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)"
)


def parse_instruction(instruction, parser=INSTRUCTION_PARSER):
    i, *cs = parser.match(instruction).groups()
    return [i] + list(map(int, cs))


def count_lights(grid):
    return sum(map(sum, grid))


def grid(size=1000):
    return [bytearray(size) for _ in range(size)]


def process_grid_01(instructions, grid):
    for instruction, rl, cl, ru, cu in instructions:
        cu += 1
        ru += 1
        updated = None
        if instruction == "on":
            updated = [1 for _ in range(cl, cu)]
            for ri in range(rl, ru):
                grid[ri][cl:cu] = updated
        elif instruction == "off":
            updated = bytearray(cu - cl)
            for ri in range(rl, ru):
                grid[ri][cl:cu] = updated
        elif instruction == "toggle":
            for ri in range(rl, ru):
                grid[ri][cl:cu] = map(not_, grid[ri][cl:cu])
        else:
            raise ValueError("Invalid instruction")
    return grid


def process_grid_02(instructions, grid):
    actions = {
        "on": lambda row: (light + 1 for light in row),
        "off": lambda row: (max(light - 1, 0) for light in row),
        "toggle": lambda row: (light + 2 for light in row),
    }
    for instruction, rl, cl, ru, cu in instructions:
        cu += 1
        ru += 1
        for ri in range(rl, ru):
            grid[ri][cl:cu] = actions[instruction](grid[ri][cl:cu])
    return grid


def solution_01(path="input.data"):
    with open(path) as fobj:
        return count_lights(
            process_grid_01(map(parse_instruction, map(str.rstrip, fobj)), grid())
        )


def solution_02(path="input.data"):
    with open(path) as fobj:
        return count_lights(
            process_grid_02(map(parse_instruction, map(str.rstrip, fobj)), grid())
        )


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
