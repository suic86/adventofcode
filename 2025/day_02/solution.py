from re import compile


def parse_data(path: str = "input.data") -> list[list[str]]:
    with open(path) as fp:
        return [list(rng.split("-")) for rng in str.strip(fp.read()).split(",")]


def is_invalid(id: str) -> bool:
    return len(id) % 2 == 0 and id[: len(id) // 2] == id[len(id) // 2 :]


def solution_01(path="input.data") -> int:
    return sum(
        sum(id for id in range(int(fid), int(lid) + 1) if is_invalid(str(id)))
        for fid, lid in parse_data(path)
    )


def is_invalid_02(id: str, rgx=compile(r"^(\d+)\1+$")) -> bool:
    return bool(rgx.match(id))


def solution_02(path="input.data") -> int:
    return sum(
        sum(id for id in range(int(fid), int(lid) + 1) if is_invalid_02(str(id)))
        for fid, lid in parse_data(path)
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
