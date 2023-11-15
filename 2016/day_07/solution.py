from re import compile

SEQUENCE = compile(r"([a-z])([a-z])\2\1")
INBRACKETS = compile(r"\[(.*?)\]")


def load_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def has_tls_sequence(s: str) -> bool:
    return bool((mo := SEQUENCE.search(s)) and mo.group(0)[0] != mo.group(0)[1])


def supports_tls(address: str) -> bool:
    if any(has_tls_sequence(s) for s in INBRACKETS.findall(address)):
        return False
    return has_tls_sequence(address)


def solution_01(path: str = "input.data") -> int:
    return sum(map(supports_tls, load_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
