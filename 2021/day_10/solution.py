def load_data(path="input.path"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


PAIRS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPEN_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def solution_01(path="input.data"):
    score = 0
    for line in load_data(path):
        stack = []
        for c in line:
            if c not in PAIRS:
                stack.append(c)
                continue
            if stack.pop() is not PAIRS[c]:
                # corrupted
                score += SCORES[c]
                break
    return score


def solution_02(path="input.data"):
    scores = []
    for line in load_data(path):
        score = 0
        stack = []
        corrupted = False
        for c in line:
            if c not in PAIRS:
                stack.append(c)
                continue
            if stack.pop() is not PAIRS[c]:
                corrupted = True
                break
        if not corrupted:
            while stack:
                score = score * 5 + OPEN_SCORES[stack.pop()]
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
