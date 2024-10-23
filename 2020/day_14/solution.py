from itertools import product


def read_data(path="input.data"):
    with open(path) as fobj:
        return list(map(str.rstrip, fobj))


def parse_mask(mask):
    return {i: int(b) for i, b in enumerate(reversed(mask)) if b != "X"}


def parse_instructions(data, parsed_mask=False):
    instructions = []
    for line in data:
        instruction, value = line.split(" = ")
        if instruction == "mask":
            instructions.append(["mask", parse_mask(value) if parsed_mask else value])
        elif instruction.startswith("mem["):
            instructions.append(
                ["mem", [int("".join(filter(str.isdigit, instruction))), int(value)]]
            )
        else:
            raise ValueError("Invalid instruction %s." % instruction)
    return instructions


def update_bit(number, bit, value):
    return number ^ (-value ^ number) & (1 << bit)


def run_converter(path="input.data"):
    instructions = parse_instructions(read_data(path), parsed_mask=True)
    mask = None
    memory = {}
    for instruction, value in instructions:
        if instruction not in ("mem", "mask"):
            raise ValueError("Invalid instruction.")
        if instruction == "mask":
            mask = value
            continue
        if instruction == "mem":
            address, value = value
            for b, v in mask.items():
                value = update_bit(value, b, v)
            memory[address] = value
    return memory


def mask_address(address, mask):
    return "".join(
        (m in "1X") and m or a for a, m in zip("{0:036b}".format(address), mask)
    )


def generate_addresses(masked_address):
    if "X" not in masked_address:
        return [int(masked_address, 2)]
    template = masked_address.replace("X", "%s")
    return [
        int(template % values, 2)
        for values in product((0, 1), repeat=masked_address.count("X"))
    ]


def memory_address_decoder(path="input.data"):
    instructions = parse_instructions(read_data(path))
    mask = None
    memory = {}
    for instruction, value in instructions:
        if instruction == "mask":
            mask = value
            continue
        if instruction == "mem":
            address, value = value
            memory.update(
                dict.fromkeys(generate_addresses(mask_address(address, mask)), value)
            )
    return memory


def solution_01(path="input.data"):
    return sum(run_converter(path).values())


def solution_02(path="input.data"):
    return sum(memory_address_decoder(path).values())


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
