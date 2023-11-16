from collections import defaultdict, deque
from dataclasses import dataclass, field

Id = tuple[str, int]
Receiver = Id


@dataclass
class Bot:
    values: set[int] = field(default_factory=set)
    high: Receiver | None = None
    low: Receiver | None = None


Instructions = dict[Id, Bot]


def load_instructions(path: str = "input.data") -> Instructions:
    result: dict[Receiver, Bot] = defaultdict(Bot)
    with open(path) as fobj:
        for line in map(str.strip, fobj):
            match line.split():
                case ["value", v, _, _, t, i]:
                    result[(t, int(i))].values.add(int(v))
                case ["bot", i, _, _, _, tl, l, *_, th, h]:
                    bot = result[("bot", int(i))]
                    bot.high, bot.low = (th, int(h)), (tl, int(l))
                case _:
                    raise ValueError(f"Invalid instruction: {line}")
    return result


def evaluate(instructions: Instructions, part_01=True) -> int:
    outputs = {}
    tasks = deque(k for k, v in instructions.items() if len(v.values) == 2)
    while tasks:
        i = tasks.pop()
        bot = instructions[i]
        mi, mx = sorted(bot.values)
        if part_01 and mi == 17 and mx == 61:
            return i[1]
        bot.values = set()
        for receiver, value in [(bot.high, mx), (bot.low, mi)]:
            match receiver:
                case ("bot", i):
                    instructions[receiver].values.add(value)
                    if len(instructions[receiver].values) == 2:
                        tasks.appendleft(receiver)
                case ("output", i):
                    outputs[i] = value
                case None:
                    raise ValueError("Receiver not defined.")
                case _:
                    raise ValueError(f"Invalid receiver: {receiver}.")
    return outputs[0] * outputs[1] * outputs[2]


def solution_01(path="input.data"):
    return evaluate(load_instructions(path))


def solution_02(path="input.data"):
    return evaluate(load_instructions(path), part_01=False)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
