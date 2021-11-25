def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def is_valid(passphrase, key=lambda x: x):
    unique_words = set()
    for word in map(key, passphrase.split()):
        if word in unique_words:
            return False
        else:
            unique_words.add(word)
    return True


def solution_01():
    return sum(map(is_valid, load_data()))


def solution_02():
    return sum(
        is_valid(passphrase, lambda p: "".join(sorted(p))) for passphrase in load_data()
    )


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
