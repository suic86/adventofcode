from collections import defaultdict


def parse_game(record: str) -> dict[str, int]:
    result = defaultdict(int)
    game, rounds = record.strip().split(":")
    result["id"] = int(game.split()[1])
    for round in rounds.split(";"):
        for colors in round.split(","):
            value, color = colors.split()
            result[color] = max(result[color], int(value))
    return result


def load_data(path: str = "input.data") -> list[dict[str, int]]:
    with open(path) as fobj:
        return list(map(parse_game, fobj))


def solution_01(path: str = "input.data") -> int:
    return sum(
        data["id"]
        for data in load_data(path)
        if data["red"] <= 12 and data["green"] <= 13 and data["blue"] <= 14
    )


def solution_02(path: str = "input.data") -> int:
    return sum(data["red"] * data["green"] * data["blue"] for data in load_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
