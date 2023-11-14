from collections import Counter


def load_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def get_repetition_code(messages: list[str], most_frequent: bool = True) -> str:
    return "".join(
        str([min, max][most_frequent](c.items(), key=lambda t: t[1])[0])
        for c in map(Counter, zip(*messages))
    )


def solution_01(path: str = "input.data") -> str:
    return get_repetition_code(load_data(path))


def solution_02(path: str = "input.data") -> str:
    return get_repetition_code(load_data(path), most_frequent=False)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
