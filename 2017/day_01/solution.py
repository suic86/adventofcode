def load_data(path="input.data"):
    with open(path) as fobj:
        return fobj.read().strip()


def solution_01(captcha: str) -> int:
    captcha = captcha + captcha[0]
    return sum(int(i) for i, j in zip(captcha, captcha[1:]) if i == j)


def solution_02(captcha: str) -> str:
    halfway_around = len(captcha) // 2
    captcha = captcha + captcha[:halfway_around]
    return sum(int(i) for i, j in zip(captcha, captcha[halfway_around:]) if i == j)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01(load_data())}")
    print(f"Solution 02: {solution_02(load_data())}")
