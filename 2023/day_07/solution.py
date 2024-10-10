from collections import Counter
from dataclasses import dataclass


@dataclass
class Hand:
    cards: str
    bid: int


def rank(hand: Hand, part2: bool = False) -> tuple[list[int], list[int]]:
    if not part2:
        card_ranks = "23456789TJQKA"
        return sorted(Counter(hand.cards).values(), reverse=True), [
            card_ranks.index(c) for c in hand.cards
        ]

    card_ranks = "J23456789TQKA"

    counts = Counter(hand.cards)
    if "J" not in counts:
        counts["J"] = 0

    jokers = counts["J"]
    del counts["J"]
    card_counts = sorted(counts.values(), reverse=True)
    if not card_counts:
        card_counts = [jokers]
    else:
        card_counts[0] += jokers
    return card_counts, [card_ranks.index(c) for c in hand.cards]


def parse_data(path: str = "input.data") -> list[Hand]:
    with open(path) as fobj:
        return [Hand(cards, int(bid)) for cards, bid in map(str.split, fobj)]


def sum_hands(hands: list[Hand]) -> int:
    return sum(rank * hand.bid for rank, hand in enumerate(hands, start=1))


def solution_01(path: str = "input.data") -> int:
    return sum_hands(sorted(parse_data(path), key=rank))


def solution_02(path: str = "input.data") -> int:
    return sum_hands(sorted(parse_data(path), key=lambda h: rank(h, part2=True)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
