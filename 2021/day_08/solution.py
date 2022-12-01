from collections import Counter
from itertools import starmap


def load_data(path="input.data"):
    with open(path) as fobj:
        parsed_data = []
        for row in fobj:
            patterns, digits = row.split(" | ")
            patterns = patterns.split()
            digits = digits.split()
            parsed_data.append([patterns, digits])
    return parsed_data


def count_easy_digits(data):
    return sum(len(digit) in (2, 4, 3, 7) for _, digits in data for digit in digits)


SEGMENT_FREQUENCIES = {"a": 8, "b": 6, "c": 8, "d": 7, "e": 4, "f": 9, "g": 7}


def decode_segments(patterns):
    segment_frequencies = Counter("".join(patterns))

    def same_frequency_segment(segment):
        """Find the segment with the same frequency as the given segment."""
        return next(
            k
            for k, v in segment_frequencies.items()
            if v == SEGMENT_FREQUENCIES[segment]
        )

    segments = {}
    patterns = list(map(set, sorted(patterns, key=len)))
    one, seven, four = patterns[:3]

    # Segments with unique frequencies
    for segment in "ebf":
        segments[segment] = same_frequency_segment(segment)

    # seven contains the same segments as one except from the `a` segment
    segments["a"] = (seven - one).pop()

    # `a` and `c` have same frequencies but `a` has already been found
    del segment_frequencies[segments["a"]]
    segments["c"] = same_frequency_segment("c")

    # both `d` and `g` have the same frequency i.e. 7

    # four consists of `b`, `c`, `d` and `f` segments and except `d` all have been decoded
    segments["d"] = (four - {segments[s] for s in "bcf"}).pop()

    # after deletion of `d`, there's only one segment which has frequency = 7 and that corresponds to segment `g`
    del segment_frequencies[segments["d"]]
    segments["g"] = same_frequency_segment("g")

    return segments


SEGMENTS_TO_DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def decode_number(patterns, digits):
    f, t = "", ""
    for k, v in decode_segments(patterns).items():
        f += v
        t += k
    tr = str.maketrans(f, t)
    return int(
        "".join(
            SEGMENTS_TO_DIGITS["".join(sorted(digit.translate(tr)))] for digit in digits
        )
    )


def solution_01(path="input.data"):
    return count_easy_digits(load_data(path))


def solution_02(path="input.data"):
    return sum(starmap(decode_number, load_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
