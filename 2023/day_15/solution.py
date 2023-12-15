from collections import defaultdict
from functools import reduce

Boxes = dict[int, list[tuple[str, int]]]


def load_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        return fobj.read().strip().split(",")


def aoc_hash(instruction: str) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.

    >>> aoc_hash("rn=1")
    30
    """
    return reduce(lambda a, c: ((a + c) * 17) % 256, map(ord, instruction), 0)


def sort_lens(instructions: list[str]) -> Boxes:
    boxes: dict[int, list[tuple[str, int]]] = defaultdict(list)
    for instruction in instructions:
        if "=" in instruction:
            lens, fs = instruction.split("=")
            hash = aoc_hash(lens)
            focal_length = int(fs)
            box = boxes[hash]
            if not box:
                boxes[hash].append((lens, focal_length))
            else:
                found = False
                for i in range(len(box)):
                    if box[i][0] == lens:
                        box[i] = (lens, focal_length)
                        found = True
                        break
                if not found:
                    box.append((lens, focal_length))
        elif instruction.endswith("-"):
            lens = instruction[:-1]
            hash = aoc_hash(lens)
            boxes[hash] = [(le, fe) for le, fe in boxes[hash] if le != lens]
        else:
            assert ValueError(f"Invalid token: {instruction}.")
    return boxes


def focusing_power(boxes: Boxes) -> int:
    return sum(
        (k + 1) * i * v for k, l in boxes.items() for i, (_, v) in enumerate(l, start=1)
    )


def solution_01(path: str = "input.data") -> int:
    return sum(map(aoc_hash, load_data(path)))


def solution_02(path: str = "input.data") -> int:
    return focusing_power(sort_lens(load_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
