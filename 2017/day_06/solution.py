from re import findall


def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, findall(r"\d+", fobj.read().strip())))


def redistribute(banks):
    size = len(banks)
    most_blocks = max(banks)
    index = banks.index(most_blocks)
    banks[index] = 0

    while most_blocks:
        index = (index + 1) % size
        banks[index] += 1
        most_blocks -= 1

    return banks


def steps_to_infinite_loop(banks):
    seen_states = {tuple(banks)}
    counter = 1

    while True:
        banks = redistribute(banks)
        if (state := tuple(banks)) not in seen_states:
            seen_states.add(state)
            counter += 1
            continue
        return counter


def cycles_between_same_states(banks):
    seen_states = {tuple(banks): 0}
    counter = 1

    while True:
        banks = redistribute(banks)
        if (state := tuple(banks)) in seen_states:
            return counter - seen_states[state] + 1
        else:
            counter += 1
            seen_states[state] = counter


def solution_01():
    return steps_to_infinite_loop(load_data())


def solution_02():
    return cycles_between_same_states(load_data())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
