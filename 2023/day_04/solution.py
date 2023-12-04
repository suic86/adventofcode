from typing import TypedDict


class Card(TypedDict):
    id: int
    wn: set[int]
    mn: list[int]


def parse_line(line: str) -> Card:
    cid, data = line.split(":")
    w, m = data.split(" | ")
    return {
        "id": int(cid.split()[1]),
        "wn": set(map(int, w.split())),
        "mn": list(map(int, m.split())),
    }


def parse_data(path: str = "input.data") -> list[Card]:
    with open(path) as fobj:
        return list(map(parse_line, fobj))


def points(card: Card) -> int:
    return int(2 ** (sum(n in card["wn"] for n in card["mn"]) - 1))


def additional_copies(cards: list[Card]) -> dict[int, list[int]]:
    return {
        card["id"]: [
            card["id"] + i
            for i in range(1, sum(n in card["wn"] for n in card["mn"]) + 1)
        ]
        for card in cards
    }


def addtional_card_counts(cards: list[Card]) -> dict[int, int]:
    copies = additional_copies(cards)
    copy_counts = {}

    def compute_value(cid: int) -> int:
        if cid not in copy_counts:
            copy_counts[cid] = sum(map(compute_value, copies[cid]), start=1)
        return copy_counts[cid]

    for k in copies:
        compute_value(k)
        if len(copy_counts) == len(copies):
            break

    return copy_counts


def solution_01(path: str = "input.data") -> int:
    return sum(map(points, parse_data(path)))


def solution_02(path: str = "input.data") -> int:
    return sum(addtional_card_counts(parse_data(path)).values())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
