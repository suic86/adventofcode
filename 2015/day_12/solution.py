from re import compile
from json import load

NUMBER_PARSER = compile(r"-?\d+")


def sum_numbers(json):
    return sum(map(int, NUMBER_PARSER.findall(json)))


def sum_with_no_red(jobj, result=0):
    if isinstance(jobj, int):
        return result + jobj
    elif isinstance(jobj, list):
        return result + sum(map(sum_with_no_red, jobj))
    elif isinstance(jobj, str):
        return result
    elif isinstance(jobj, dict):
        if "red" in jobj.values():
            return result
        return (
            result
            + sum(map(sum_with_no_red, jobj.keys()))
            + sum(map(sum_with_no_red, jobj.values()))
        )


def solution_01(path="input.data"):
    with open(path) as fobj:
        return sum_numbers(fobj.read())


def solution_02(path="input.data"):
    with open(path, "rb") as fobj:
        return sum_with_no_red(load(fobj))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
