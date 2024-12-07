def parse_line(line: str) -> tuple[int, list[int]]:
    m, ns = line.rstrip().split(": ")
    return int(m), list(map(int, ns.split()))


def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(parse_line, fobj))


def is_valid(n, ms):
    q = [ms[0]]
    for m in ms[1:]:
        nq = []
        while q:
            x = q.pop()
            if n == (a := x + m) or n == (mu := x * m):
                return True
            nq.append(mu)
            nq.append(a)
        q = nq
    return n in q


def is_valid_02(n, ms):
    q = [ms[0]]
    for m in ms[1:]:
        nq = []
        for x in q:
            if (a := x + m) <= n:
                nq.append(a)
            if (mu := x * m) <= n:
                nq.append(mu)
            if c := int(f"{x}{m}"):
                nq.append(c)
        q = nq
    return n in q


def solution_01(path="input.data"):
    return sum(n for n, ms in parse_data(path) if is_valid(n, ms))


def solution_02(path="input.data"):
    return sum(n for n, ms in parse_data(path) if is_valid_02(n, ms))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
