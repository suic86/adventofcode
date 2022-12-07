from collections import Counter


def parse_data(path="input.data"):
    stack = []
    visited = set()
    total_sizes = Counter()
    with open(path) as fobj:
        dirs = None
        for line in map(str.strip, fobj):
            if line == "$ ls" or line.startswith("dir"):
                continue
            elif line.startswith("$ cd"):
                if line == "$ cd ..":
                    stack.pop()
                elif line.startswith("$ cd"):
                    dirname = line.split(" ")[-1]
                    stack.append(dirname)
                dirs = list("/".join(stack[: i + 1]) for i in range(len(stack)))
            elif line[0].isnumeric():
                v, f = line.split()
                f = f"{dirs[-1]}/{f}"
                if f in visited:
                    continue
                visited.add(f)
                for d in dirs:
                    total_sizes[d] += int(v)
            else:
                raise ValueError(f"Invalid line: {line}.")
    return total_sizes


def solution_01(path="input.data", threshold=100_000):
    sizes = parse_data(path)
    return sum(size for size in sizes.values() if size <= threshold)


def solution_02(
    path="input.data", total_disk_space=70_000_000, required_free_space=30_000_000
):
    max_used_space = total_disk_space - required_free_space
    sizes = parse_data(path)
    used_space = sizes["/"]
    space_to_delete = used_space - max_used_space
    return min(filter(space_to_delete.__le__, sizes.values()))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
