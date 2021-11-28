from re import sub


def cancel_characters(stream):
    return sub(r"!.", "", stream)


def clean_garbage(stream):
    return sub(r"<.*?>", "", stream)


def count_groups(stream):
    level = 0
    count = 0
    for char in clean_garbage(cancel_characters(stream)):
        if char == "{":
            level += 1
            count += level
        elif char == "}":
            level -= 1
    return count


def count_garbage(stream):
    with_garbage = cancel_characters(stream)
    without_garbage = sub(r"<.*?>", "<>", with_garbage)
    return len(with_garbage) - len(without_garbage)


def solution_01(path="input.data"):
    with open("input.data") as fobj:
        return count_groups(fobj.read())


def solution_02(path="input.data"):
    with open("input.data") as fobj:
        return count_garbage(fobj.read())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
