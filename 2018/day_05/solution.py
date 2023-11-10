def load_data(path="input.data"):
    with open(path) as fobj:
        return str.strip(fobj.read())


def length(p: str, to_remove: str = "") -> int:
    stack: list[str] = []
    to_remove = to_remove.lower()

    def is_reactive() -> bool:
        return previous.islower() != unit.islower() and previous.lower() == unit.lower()

    for unit in p:
        if unit.lower() == to_remove:
            continue
        if not stack:
            stack.append(unit)
            continue
        previous = stack[-1]
        if is_reactive():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)


def reacted_length(polymer: str, shortest=False) -> int:
    if not shortest:
        return length(polymer)

    return min(length(polymer, to_remove=unit) for unit in set(polymer.lower()))


def solution_01(path="input.data") -> int:
    return reacted_length(load_data(path))


def solution_02(path="input.data") -> int:
    return reacted_length(load_data(path), shortest=True)
