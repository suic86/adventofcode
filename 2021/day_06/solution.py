from collections import Counter, defaultdict


def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().strip().split(",")))


def simulator(initial_state, days):
    state = Counter(initial_state)
    for _ in range(days):
        new_state = defaultdict(int)
        for k, v in state.items():
            if k == 0:
                new_state[6] += v
                new_state[8] += v
            else:
                new_state[k - 1] += v
        state = new_state
    return state


def solution_01(path="input.data"):
    return sum(simulator(load_data(path), 80).values())


def solution_02(path="input.data"):
    return sum(simulator(load_data(path), 256).values())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
