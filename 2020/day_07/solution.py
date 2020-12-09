#!/usr/bin/env python3

from collections import defaultdict
from re import sub


def parse_data(path):
    with open(path) as fobj:
        for line in map(str.rstrip, fobj):
            yield parse_rule(line)


def parse_rule(line):
    if "no other bags" in line:
        return (" ".join(line.split()[:2]), [])
    line = sub(r"bags?[,. ]? ?", "", line).strip()
    color_type, color, _, *contains = line.split()
    return " ".join((color_type, color)), [
        (" ".join(c), int(n)) for n, *c in zip(*[iter(contains)] * 3)
    ]


def dependency_tree(rules):
    tree = defaultdict(set)
    for bag, contains in rules:
        for b, _ in contains:
            tree[b].add(bag)
    return tree


def dfs(graph, root_node):
    visited = set()
    stack = [root_node]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            stack += graph[current_node]
    return visited


def rule_tree(rules):
    return {color: {c: n for c, n in contains} for color, contains in rules}


def count_all_bags(tree, color):
    if not tree[color]:
        return 1
    return 1 + sum(v * count_all_bags(tree, k) for k, v in tree[color].items())


def count_contained_bags(tree, color):
    return count_all_bags(tree, color) - 1


def solution_01(path="input.data"):
    graph = dependency_tree(parse_data(path))
    return len(dfs(graph, "shiny gold")) - 1


def solution_02(path="input.data"):
    return count_contained_bags(rule_tree(parse_data(path)), "shiny gold")


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
