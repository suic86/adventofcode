from functools import reduce
from operator import itemgetter, mul
from re import compile


def parse_data(path="input.data"):
    numbers = compile(r"\d+")
    extract_int = lambda field: int(numbers.search(field).group(0))

    with open(path) as fobj:
        monkeys = {}
        for monkey in fobj.read().split("\n\n"):
            modulo = 1
            index, items, operation, test, iftrue, iffalse = map(
                str.strip, monkey.split("\n")[:6]
            )

            items = list(map(int, numbers.findall(items)))

            operation, value = operation.split()[-2:]
            if operation not in "*+":
                raise ValueError(f"Invalid operation {operation}.")

            if value == "old":
                if operation == "*":
                    operation = lambda v: v * v
                elif operation == "+":
                    operation = lambda v: v + v
            else:
                if operation == "*":
                    operation = int(value).__mul__
                elif operation == "+":
                    operation = int(value).__add__

            index, modulo, iftrue, iffalse = map(
                extract_int, [index, test, iftrue, iffalse]
            )

            test = lambda v, modulo=modulo, iftrue=iftrue, iffalse=iffalse: (
                iftrue if v % modulo == 0 else iffalse
            )

            monkeys[index] = {
                "items": items,
                "operation": operation,
                "test": test,
                "processed": 0,
                "modulo": modulo,
            }

        return monkeys


def do_rounds(monkeys, rounds=20, first_part=True):
    modulo = reduce(mul, (m["modulo"] for m in monkeys.values()), 1)
    for _ in range(rounds):
        for _, monkey in sorted(monkeys.items()):
            monkey["processed"] += len(monkey["items"])
            for new_item in map(monkey["operation"], monkey["items"]):
                if first_part:
                    new_item //= 3
                # https://www.reddit.com/r/adventofcode/comments/ziw4aq/comment/izsr5av/?utm_source=share&utm_medium=web2x&context=3
                # For any set of integers n, p and d: if d mod p = 0, then (n mod p) mod d = n mod d
                monkeys[monkey["test"](new_item)]["items"].append(new_item % modulo)
            monkey["items"] = []
    return monkeys


def monkey_business_level(monkeys):
    """Product of the processed items of the two most active monkeys."""
    return mul(*sorted(map(itemgetter("processed"), monkeys.values()))[-2:])


def solution_01(path="input.data"):
    return monkey_business_level(do_rounds(parse_data(path)))


def solution_02(path="input.data"):
    return monkey_business_level(
        do_rounds(parse_data(path), rounds=10000, first_part=False)
    )
