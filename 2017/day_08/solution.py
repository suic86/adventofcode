from operator import eq, ne, gt, ge, lt, le


def parse_instruction(raw):
    parsed = raw.split()
    parsed.pop(3)
    parsed[2], parsed[5] = int(parsed[2]), int(parsed[5])
    return parsed


def eval_condition(value, operation, condition_value):
    operations = {">": gt, "<": lt, ">=": ge, "<=": le, "==": eq, "!=": ne}
    return operations[operation](value, condition_value)


def eval_instructions(*instructions):
    registers = {}

    for raw_instruction in instructions:
        parsed = parse_instruction(raw_instruction)
        (
            register,
            operation,
            value,
            condition_register,
            condition_operation,
            condition_value,
        ) = parsed

        if register not in registers:
            registers[register] = 0

        if condition_register not in registers:
            registers[condition_register] = 0

        if eval_condition(
            registers[condition_register], condition_operation, condition_value
        ):
            if operation == "inc":
                registers[register] += value
            elif operation == "dec":
                registers[register] -= value
            else:
                raise ValueError(
                    f"Invalid operation: {operation} (allowed values: inc, dec)."
                )

    return registers


def solution_02(path="input.data"):
    registers = {}
    current_register = None

    def eval_instruction(raw_instruction):
        nonlocal current_register
        parsed = parse_instruction(raw_instruction)
        (
            register,
            operation,
            value,
            condition_register,
            condition_operation,
            condition_value,
        ) = parsed

        current_register = register

        if register not in registers:
            registers[register] = 0

        if condition_register not in registers:
            registers[condition_register] = 0

        if eval_condition(
            registers[condition_register], condition_operation, condition_value
        ):
            if operation == "inc":
                registers[register] += value
            elif operation == "dec":
                registers[register] -= value
            else:
                raise ValueError(
                    f"Invalid operation: {operation} (allowed values: inc, dec)."
                )

    max_value = 0

    with open(path) as fobj:
        for raw_instruction in map(str.strip, fobj):
            eval_instruction(raw_instruction)
            if (value := registers[current_register]) > max_value:
                max_value = value

    return max_value


def solution_01(path="input.data"):
    with open(path) as fobj:
        return max(eval_instructions(*fobj).values())


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02('input.data')}")
