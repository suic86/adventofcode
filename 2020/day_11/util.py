OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(list, fobj))


def load_test_generations(path):
    generations = []
    with open(path) as fobj:
        generation = []
        for line in map(list, map(str.rstrip, fobj)):
            if line:
                generation.append(line)
                continue
            generations.append(generation)
            generation = []
    return generations
