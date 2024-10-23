from itertools import accumulate, cycle


def read_data(path="input.data"):
    with open(path) as source_file:
        return list(map(int, source_file))


def solution_01(path="input.data"):
    return sum(read_data(path))


def solution_02(path="input.data"):
    unique_frequencies = set()
    for frequency in accumulate(cycle(read_data(path)), initial=0):
        if frequency in unique_frequencies:
            return frequency
        unique_frequencies.add(frequency)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
