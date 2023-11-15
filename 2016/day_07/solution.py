import re

from itertools import chain


def load_data(path: str = "input.data") -> list[str]:
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def split_address(address: str) -> tuple[list[str], list[str]]:
    outer: list[str] = []
    inner: list[str] = []
    buffer: list[str] = []
    inside = False
    for c in address:
        if c not in "[]":
            buffer.append(c)
            continue
        if c == "[":
            if inside:
                raise ValueError("Invalid address.")
            outer.append("".join(buffer))
            inside = True
        elif c == "]":
            if not inside:
                raise ValueError("Invalid address.")
            inner.append("".join(buffer))
            inside = False
        buffer = []
    if inside:
        raise ValueError("Invalid address.")
    if buffer:
        outer.append("".join(buffer))
    return outer, inner


def list_abas(chunk: str) -> list[tuple[str, str, str]]:
    return [
        (a, b, c) for a, b, c in zip(chunk, chunk[1:], chunk[2:]) if a == c and a != b
    ]


def has_tls_sequence(chunk: str) -> bool:
    return any(
        a == d and a != b and b == c
        for a, b, c, d in zip(chunk, chunk[1:], chunk[2:], chunk[3:])
    )


def tls_support(address: str) -> bool:
    outer, inner = split_address(address)
    return (not any(map(has_tls_sequence, inner))) and any(map(has_tls_sequence, outer))


def ssl_support(address: str) -> bool:
    outer, inner = split_address(address)
    if not (inner and outer):
        return False
    inside = set(chain.from_iterable(map(list_abas, inner)))
    outside = set(chain.from_iterable(map(list_abas, outer)))
    return any((s, f, s) in inside for f, s, _ in outside)


def solution_01(path: str = "input.data") -> int:
    return sum(map(tls_support, load_data(path)))


def solution_02(path: str = "input.data") -> int:
    return sum(map(ssl_support, load_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
