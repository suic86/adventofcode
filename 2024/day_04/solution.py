def parse_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def solution_01(path="input.data"):
    m = parse_data(path)
    h = len(m)
    w = len(m[0])
    patterns = ("XMAS", "SAMX")
    total = 0

    for row in m:
        total += sum(row[i : i + 4] in patterns for i in range(w))

    for c in range(w):
        column = "".join(row[c] for row in m)
        total += sum(column[i : i + 4] in patterns for i in range(h))

    for s in range(2 * h - 1):
        z = 0 if s < h else s - h + 1
        diag1 = "".join(m[j][(h - 1) - (s - j)] for j in range(z, s - z + 1))
        diag2 = "".join(m[j][s - j] for j in range(z, s - z + 1))
        total += sum(diag1[i : i + 4] in patterns for i in range(len(diag1)))
        total += sum(diag2[i : i + 4] in patterns for i in range(len(diag2)))

    return total


def solution_02(path="input.data"):
    m = parse_data(path)
    h = len(m)
    w = len(m[0])
    patterns = ("MMSS", "SSMM", "MSMS", "SMSM")

    total = 0
    for i in range(h - 2):
        for j in range(w - 2):
            total += m[i + 1][j + 1] == "A" and (
                "".join((m[i][j], m[i][j + 2], m[i + 2][j], m[i + 2][j + 2]))
                in patterns
            )
    return total


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
