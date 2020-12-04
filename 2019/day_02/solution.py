#!/usr/bin/env python3

HALT = 99
INSTRUCTION_SIZE = 4


def read_program(path="input.data"):
    with open(path) as fobj:
        return list(map(int, fobj.read().split(",")))


def compute(opcode, noun, verb):
    return {
        1: lambda: noun + verb,
        2: lambda: noun * verb,
    }[opcode]()


def run_program(program):
    memory = program[:]
    ip = 0  # instruction pointer
    while memory[ip] != HALT:
        opcode, noun, verb, out = memory[ip : ip + INSTRUCTION_SIZE]
        memory[out] = compute(opcode, memory[noun], memory[verb])
        ip += INSTRUCTION_SIZE
    return memory


def solution_01(path="input.data"):
    program = read_program(path)
    program[1] = 12
    program[2] = 2
    return run_program(program)[0]


def solution_02():
    for noun in range(100):
        for verb in range(100):
            program = read_program()
            program[1], program[2] = noun, verb
            if run_program(program)[0] == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    print(solution_01())
    print(solution_02())
