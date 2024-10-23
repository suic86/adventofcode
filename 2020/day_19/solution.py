import re


def read_data(path="input.data"):
    rules = {}
    data = []
    with open(path) as fobj:
        rule_section = True
        for line in map(str.rstrip, fobj):
            if not line:
                rule_section = False
                continue
            if rule_section:
                rule_number, rule = line.split(": ")
                rules[int(rule_number)] = rule.strip('"')
            else:
                data.append(line)
    return rules, data


def convert_to_regex(rule, rules):
    terminals = "ab"

    rule = rules[rule]

    if rule in terminals:
        return rule

    return "(?:%s)" % "|".join(
        "".join(convert_to_regex(int(r), rules) for r in rl.split())
        for rl in rule.split(" | ")
    )


def solution_02_check(line, rule42, rule31):
    """
    Rule 8:  42    | 42 8      # rule 42 must appear one or more times
    Rule 11: 42 31 | 42 11 31  # rule 42 and rule 31 must appear n times where n > 0
    Rule 0:  8 11              # rule 8 and rule 11 must appear exactly one time

    Rule 0 means that

    1) rule 42 must appear at least twice (once in 8 and once in 11).
    2) rule 42 must appear more times than rule 31.
    """
    matches = re.fullmatch(f"({rule42}{{2,}})({rule31}+)", line)
    if matches is None:
        return False
    s42, s31 = matches.groups()
    l42 = len(re.findall(rule42, s42))
    l31 = len(re.findall(rule31, s31))
    return l42 > l31


def solution_01(path="input.data"):
    rules, data = read_data(path)
    rule0 = convert_to_regex(0, rules)
    rule0 = re.compile(rule0)
    return sum(rule0.fullmatch(d) is not None for d in data)


def solution_02(path="input.data"):
    rules, data = read_data(path)
    rule42 = convert_to_regex(42, rules)
    rule31 = convert_to_regex(31, rules)
    return sum(solution_02_check(line, rule42, rule31) for line in data)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
