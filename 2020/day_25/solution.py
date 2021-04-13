from itertools import islice


def parse_data(path="input.data"):
    with open(path) as fobj:
        return tuple(map(int, fobj.readlines()))


def key_gen(subject_number=7):
    value = 1
    while True:
        yield value
        value = (value * subject_number) % 20201227


def loop_size(public_key, subject_number=7):
    return next(i for i, key in enumerate(key_gen()) if key == public_key)


def encryption_key(pbk1, pbk2):
    size = loop_size(pbk1)
    return list(islice(key_gen(subject_number=pbk2), size, size + 1))[0]


def solution_01(path="input.data"):
    return encryption_key(*parse_data(path))


if __name__ == "__main__":
    print("Solution 01:", solution_01("input.data"))
