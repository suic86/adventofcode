from collections import defaultdict
from re import compile


def load_data(path):
    parser = compile(r"\d+")
    pipes = defaultdict(set)
    with open(path) as fobj:
        for program, *cs in map(parser.findall, fobj):
            pipes[int(program)].update(map(int, cs))
    return pipes


def dfs(graph, root):
    stack = [root]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])
    return visited


def zero_group_size(pipes):
    return len(dfs(pipes, 0))


def group_count(pipes):
    programs = set(pipes)
    count = 0
    while programs:
        count += 1
        root = programs.pop()
        connected = dfs(pipes, root)
        programs -= connected
    return count


def solution_01(path="input.data"):
    return zero_group_size(load_data(path))


def solution_02(path="input.data"):
    return group_count(load_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
