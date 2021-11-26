def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj))


def steps_to_escape(jumps, second_part=False):
    position = 0
    counter = 1
    size = len(jumps)

    while True:
        previous = position
        position += jumps[position]
        jumps[previous] += -1 if second_part and jumps[previous] >= 3 else 1
        if position < 0 or position >= size:
            return counter
        counter += 1


def solution_01():
    return steps_to_escape(load_data())


def solution_02():
    return steps_to_escape(load_data(), second_part=True)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
