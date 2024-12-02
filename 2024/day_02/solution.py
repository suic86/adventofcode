def parse_data(path="input.data"):
    with open(path) as fobj:
        return [list(map(int, line.split())) for line in map(str.rstrip, fobj)]


def safe_report_01(report):
    return all(i < j and 1 <= j - i <= 3 for i, j in zip(report, report[1:])) or all(
        i > j and 1 <= i - j <= 3 for i, j in zip(report, report[1:])
    )


def safe_report_02(report):
    return any(
        safe_report_01([e for j, e in enumerate(report) if j != i])
        for i in range(len(report))
    )


def solution_01(path="input.data"):
    return sum(map(safe_report_01, parse_data(path)))


def solution_02(path="input.data"):
    return sum(map(safe_report_02, parse_data(path)))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
