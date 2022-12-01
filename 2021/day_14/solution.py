from collections import Counter
from itertools import islice


def load_data(path="input.data"):
    with open(path) as fobj:
        fobj = map(str.strip, fobj)
        polymer_template = next(fobj)
        # skip empty line
        next(fobj)
        insertion_rules = {tuple(k): v for k, v in (row.split(" -> ") for row in fobj)}
    return polymer_template, insertion_rules


# naive_ functions were used to solve the first part


def naive_step_gen(polymer_template, insertion_rules):
    state = list(polymer_template)
    while True:
        new_state = []
        for pair in zip(state, state[1:]):
            if pair in insertion_rules:
                new_state.extend([pair[0], insertion_rules[pair]])
            else:
                new_state.append(pair[0])
        new_state.append(state[-1])
        state = new_state
        yield "".join(state)


def naive_nth_step(n, polymer_template, insertion_rules):
    return Counter(
        next(islice(naive_step_gen(polymer_template, insertion_rules), n - 1, n))
    )


def naive_solution_01(path="input.data"):
    element_counts = naive_nth_step(10, *load_data(path))
    return max(element_counts.values()) - min(element_counts.values())


def optimized_step_gen(polymer_template, insertion_rules):
    elements = Counter(polymer_template)
    state = Counter(zip(polymer_template, polymer_template[1:]))
    while True:
        new_state = Counter()
        for pair, count in state.items():
            if pair not in insertion_rules:
                new_state[pair] = count
                continue
            left, right = pair
            element = insertion_rules[pair]
            new_state[(left, element)] += count
            new_state[(element, right)] += count
            elements[element] += count
        state = new_state
        yield elements


def optimized_nth_step(n, polymer_template, insertion_rules):
    if n == 0:
        return Counter(polymer_template)
    return next(islice(optimized_step_gen(polymer_template, insertion_rules), n - 1, n))


def solution_01(path="input.data"):
    element_counts = optimized_nth_step(10, *load_data(path))
    return max(element_counts.values()) - min(element_counts.values())


def solution_02(path="input.data"):
    element_counts = optimized_nth_step(40, *load_data(path))
    return max(element_counts.values()) - min(element_counts.values())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
