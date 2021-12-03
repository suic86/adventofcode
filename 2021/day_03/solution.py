from collections import Counter
from operator import itemgetter, mul


def load_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.strip, fobj))


def gamma_epsilon(report):
    bits = [0] * len(report[0])
    for row in report:
        for i, bit in enumerate(row):
            if bit == "1":
                bits[i] += 1
    half = len(report) // 2
    TR = str.maketrans("01", "10")
    gamma = "".join(str(int(bit >= half)) for bit in bits)
    epsilon = gamma.translate(TR)
    return int(gamma, 2), int(epsilon, 2)


def count_bits(report, bit):
    return Counter(map(itemgetter(bit), report))


def oxygen_generator_rating(report):
    """
    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    """
    bit = 0
    while len(report) > 1:
        bit_count = count_bits(report, bit)
        most_common = str(int(bit_count["1"] >= bit_count["0"]))
        report = [row for row in report if row[bit] == most_common]
        bit += 1
    return int(report[0], 2)


def co2_scrubber_rating(report):
    """
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    """
    bit = 0
    while len(report) > 1:
        bit_count = count_bits(report, bit)
        least_common = str(int(bit_count["1"] < bit_count["0"]))
        report = [row for row in report if row[bit] == least_common]
        bit += 1
    return int(report[0], 2)


def solution_01(path="input.data"):
    return mul(*gamma_epsilon(load_data(path)))


def solution_02(path="input.data"):
    report = load_data(path)
    return oxygen_generator_rating(report) * co2_scrubber_rating(report)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
