from re import finditer, search


def parse_input(path="input.data"):
    with open(path) as fobj:
        for word in map(str.rstrip, fobj):
            yield word


def is_nice_01(string):
    """
    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    return (
        sum(map(bool, finditer("[aeiou]", string))) >= 3
        and bool(search(r"([a-z])\1", string))
        and not search(r"(ab|cd|pq|xy)", string)
    )


def is_nice_02(string):
    """
    A nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    return bool(search(r"([a-z]{2}).*\1", string)) and bool(
        search(r"([a-z]{1})(?!\1).\1", string)
    )


def solution_01(path="input.data"):
    return sum(map(is_nice_01, parse_input(path)))


def solution_02(path="input.data"):
    return sum(map(is_nice_02, parse_input(path)))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
