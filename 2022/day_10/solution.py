from itertools import cycle


def parse_data(path="input.data"):
    with open(path) as fobj:
        return [
            None if line == "noop" else int(line.split()[1])
            for line in map(str.strip, fobj)
        ]


def signal_strength(program, cycles=(20, 60, 100, 140, 180, 220)):
    x = 1
    ccycle = 0
    result = 0
    max_cycle = max(cycles)
    for instruction in cycle(program):
        if ccycle >= max_cycle:
            break
        # first cycle
        ccycle += 1
        if ccycle in cycles:
            result += ccycle * x

        # noop completes in one cycle
        if instruction is None:
            continue

        # second cycle
        ccycle += 1
        if ccycle in cycles:
            result += ccycle * x
        x += instruction
    return result


def draw(program, width=40, height=6):
    """
    If the sprite is positioned such that
    one of its three pixels is the pixel currently being drawn,
    the screen produces a lit pixel (#);
    otherwise, the screen leaves the pixel dark (.).
    """
    screen = [list("." * width) for _ in range(height)]
    max_cycle = width * height
    beam = ((r, c) for r in range(height) for c in range(width))

    def draw_pixel(x):
        pixel = next(beam)
        r, c = pixel
        if x - 1 <= c <= x + 1:
            screen[r][c] = "#"

    x = 1
    ccycle = 0

    for instruction in cycle(program):

        # first cycle
        ccycle += 1
        if ccycle > max_cycle:
            break
        draw_pixel(x)

        # noop completes in one cycle
        if instruction is None:
            continue

        # second cycle
        ccycle += 1
        if ccycle > max_cycle:
            break
        draw_pixel(x)
        x += instruction

    return "\n".join(map("".join, screen))


def solution_01(path="input.data"):
    return signal_strength(parse_data(path))


def solution_02(path="input.data"):
    return draw(parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print("Solution 02: ERCREPCJ")
    print(f"Solution 02 Screen:\n{solution_02()}")
