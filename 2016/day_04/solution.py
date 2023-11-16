from collections import Counter
from dataclasses import dataclass
from string import ascii_lowercase

STORAGE_NAME = "northpole object storage"
ALPHABET_SIZE = len(ascii_lowercase)


@dataclass
class Room:
    name: list[str]
    id: int
    checksum: str


def load_data(path: str = "input.data") -> list[Room]:
    with open(path) as fobj:
        parsed: list[Room] = []
        for line in map(str.strip, fobj):
            *n, ic = line.split("-")
            i, c = ic[:-1].split("[")
            parsed.append(Room(n, int(i), c))
    return parsed


def is_real(room: Room) -> bool:
    return room.checksum == "".join(
        k
        for k, _ in sorted(
            Counter("".join(room.name)).items(), key=lambda t: (-t[1], t[0])
        )[:5]
    )


shifters = {
    i: str.maketrans(
        ascii_lowercase,
        "".join(chr((ord(c) - 97 + i) % ALPHABET_SIZE + 97) for c in ascii_lowercase),
    )
    for i in range(26)
}


def decrypt_name(room: Room) -> str:
    return " ".join(room.name).translate(shifters[room.id % ALPHABET_SIZE])


def solution_01(path: str = "input.data") -> int:
    return sum(room.id for room in filter(is_real, load_data(path)))


def solution_02(path: str = "input.data") -> int:
    return next(
        room.id
        for room in filter(is_real, load_data(path))
        if decrypt_name(room) == STORAGE_NAME
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
