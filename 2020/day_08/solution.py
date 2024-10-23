def read_program(path="input.data"):
    with open(path) as program_file:
        return parse_program(program_file.read())


def parse_instruction(line):
    instruction, argument = line.split()
    return instruction, int(argument)


def parse_program(program_string):
    return list(
        map(parse_instruction, filter(None, map(str.strip, program_string.split("\n"))))
    )


def run_instruction(instruction, instruction_pointer, accumulator):
    i, a = instruction
    if i == "acc":
        accumulator += a
        instruction_pointer += 1
    elif i == "jmp":
        instruction_pointer += a
    elif i == "nop":
        instruction_pointer += 1
    else:
        raise ValueError(f"Invalid instruction: {i}")
    return instruction_pointer, accumulator


def run_program(program):
    ip = 0  # instruction pointer
    acc = 0  # accumulator value
    size = len(program)
    last = size - 1
    while True:
        yield ip, acc
        instruction = program[ip]
        new_ip, new_acc = run_instruction(instruction, ip, acc)
        new_ip %= size

        # last instruction reached - terminate the program
        if ip == last and (instruction[0] != "jmp" or instruction[1] == 1):
            yield -1, new_acc
            return

        ip, acc = new_ip, new_acc


def run_program_from_file(path="input.data"):
    program = read_program(path)
    yield from run_program(program)


def detect_infinite_loop(program):
    visited = set()
    status = run_program(program)
    while True:
        ip, acc = next(status)
        if ip in visited:
            return True, acc
        if ip == -1:
            return False, acc
        visited.add(ip)


def _swap_instruction(instruction):
    i, a = instruction
    if i == "nop":
        i = "jmp"
    elif i == "jmp":
        i = "nop"
    return (i, a)


def _solution_02_brute_force_algo(program):
    result = None

    for i, (instruction, _) in enumerate(program):
        if instruction not in ("jmp", "nop"):
            continue
        program[i] = _swap_instruction(program[i])
        has_infinite_loop, last_value = detect_infinite_loop(program)
        if not has_infinite_loop:
            if result is not None:
                raise Exception("More than one solution found.")
            result = last_value
        program[i] = _swap_instruction(program[i])

    if result is None:
        raise Exception("No solution found.")

    return result


def solution_01(path="input.data"):
    is_infinite, last_value = detect_infinite_loop(read_program(path))
    if not is_infinite:
        raise Exception("Something went wrong!")
    return last_value


def solution_02(path="input.data"):
    program = read_program(path)
    return _solution_02_brute_force_algo(program)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
