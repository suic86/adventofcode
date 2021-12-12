from collections import defaultdict, Counter


def load_data(path="input.data"):
    graph = defaultdict(set)
    with open(path) as fobj:
        for row in map(str.strip, fobj):
            f, t = row.split("-")
            graph[f].add(t)
            graph[t].add(f)
    return graph


# Modified version of dfs_paths
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def path_count(graph):
    count = 0
    stack = [("start", ["start"])]
    while stack:
        (cave, path) = stack.pop()
        for next_cave in graph[cave] - set(filter(str.islower, path)):
            if next_cave == "end":
                count += 1
            else:
                stack.append((next_cave, path + [next_cave]))
    return count


# Modified version of dfs_paths
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def path_count_solution_02(graph):
    count = 0
    stack = [("start", ["start"])]
    while stack:
        (cave, path) = stack.pop()
        caves = Counter(filter(str.islower, path))
        # the caves named "start" and "end" can only be visited exactly once each
        for next_cave in graph[cave] - {"start"}:
            # you might have time to visit a single small cave twice
            if next_cave.islower() and (next_cave in caves and 2 in caves.values()):
                continue
            if next_cave == "end":
                count += 1
            else:
                stack.append((next_cave, path + [next_cave]))
    return count


def solution_01(path="input.data"):
    return path_count(load_data(path))


def solution_02(path="input.data"):
    return path_count_solution_02(load_data(path))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
