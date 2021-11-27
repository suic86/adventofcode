from operator import sub
from re import compile


def load_data(path):
    parser = compile(r"([a-z]+) \((\d+)\)(?: -> )?(.+)?")

    weights = {}
    tower = {}

    with open(path) as fobj:
        for row in map(str.strip, fobj):
            program, weight, subprograms = parser.match(row).groups()
            weights[program] = int(weight)
            if subprograms is not None:
                tower[program] = set(subprograms.split(", "))

    return weights, tower


def bottom_program(tower):
    return (set(tower) - set().union(*tower.values())).pop()


def sum_weights(program, weights, tower):
    """Sum the program weight and all weights about the program."""
    if program in tower:
        return weights[program] + sum(
            sum_weights(subprogram, weights, tower) for subprogram in tower[program]
        )
    return weights[program]


def required_weight(weights, tower):
    summed_weights = {
        program: {sum_weights(subprogram, weights, tower) for subprogram in subprograms}
        for program, subprograms in tower.items()
    }

    unballanced_weights = {
        program: weights
        for program, weights in summed_weights.items()
        if len(weights) > 1
    }

    # Find the first unballanced disk
    program, first_unbalanced_disk = min(
        unballanced_weights.items(), key=lambda t: sum(t[1])
    )

    weight_difference = abs(sub(*first_unbalanced_disk))

    unballanced_weight = max(first_unbalanced_disk)

    return (
        weights[
            next(
                subprogram
                for subprogram in tower[program]
                if sum_weights(subprogram, weights, tower) == unballanced_weight
            )
        ]
        - weight_difference
    )


def solution_01():
    _, tower = load_data("input.data")
    return bottom_program(tower)


def solution_02():
    return required_weight(*load_data("input.data"))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
