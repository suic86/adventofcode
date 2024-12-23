from collections import defaultdict


def parse_data(path="input.data") -> list[tuple[str, str]]:
    with open(path) as fobj:
        return [tuple(line.split("-")) for line in map(str.rstrip, fobj)]


def networks(connections: list[tuple[int, int]]) -> int:
    g = defaultdict(set)
    for s, e in connections:
        g[s].add(e)
        g[e].add(s)

    return len(
        {
            frozenset((c, e, x))
            for c in {e for e in g if e.startswith("t")}
            for e in g[c]
            for x in g[e]
            if x != c and x != e and x in g[c]
        }
    )


def password(connections: list[tuple[int, int]]) -> str:
    g = defaultdict(set)
    for s, e in connections:
        g[s].add(e)
        g[e].add(s)

    components = set()
    size = 0

    for v in g:
        stack = [(v, {v})]
        visited = set()
        while stack:
            n, p = stack.pop()
            visited.add(n)
            if len(p) > size:
                size = len(p)
                components = {frozenset(p)}
            elif len(p) == size:
                components.add(frozenset(p))
            for e in g[n] - (visited | p):
                if p.issubset(g[e]):
                    stack.append((e, p | {e}))
    if len(components) != 1:
        raise ValueError(
            f"There must be exactly 1 largest set of computer but was: {len(components)}"
        )
    return ",".join(sorted(components.pop()))


def solution_01(path="input.data"):
    return networks(parse_data(path))


def solution_02(path="input.data"):
    return password(parse_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
