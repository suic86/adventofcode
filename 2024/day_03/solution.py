from re import compile

PARSER = compile(r"(?:(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\))")


def parse_data(path: str, parser=PARSER):
    with open(path) as fobj:
        return parser.findall(fobj.read().rstrip())


def solution_01(path: str = "input.data") -> int:
    return sum(int(a) * int(b) for _, _, a, b in parse_data(path) if a and b)


def solution_02(path: str = "input.data") -> int:
    on = True
    res = 0
    for y, n, a, b in parse_data(path):
        if y:
            on = True
        elif n:
            on = False
        elif on:
            res += int(a) * int(b)
    return res


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
