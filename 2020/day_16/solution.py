from functools import reduce
from itertools import chain, takewhile
from operator import truth
from re import compile


FIELD_PARSER = compile(
    r"(?P<name>[a-z ]+): (?P<fl>\d{1,3})-(?P<fu>\d{1,3}) or (?P<sl>\d{1,3})-(?P<su>\d{1,3})"
)


def parse_field(row):
    m = FIELD_PARSER.fullmatch(row)
    return (
        m.group("name"),
        [
            [int(m.group("fl")), int(m.group("fu"))],
            [int(m.group("sl")), int(m.group("su"))],
        ],
    )


def parse_ticket(row):
    return list(map(int, row.rstrip().split(",")))


def read_data(path="input.data"):
    data = {"fields": {}, "my ticket": None, "nearby tickets": []}
    with open(path) as fobj:
        rows = map(str.rstrip, fobj)
        fields = list(takewhile(truth, rows))
        data["fields"].update(dict(map(parse_field, fields)))
        # skip my ticket header
        next(rows)
        data["my ticket"] = parse_ticket(next(rows))
        # skip nearby ticket headers
        next(rows)
        next(rows)
        for row in rows:
            data["nearby tickets"].append(parse_ticket(row))
    return data


def value_in_range(value, rng):
    lower, upper = rng
    return lower <= value <= upper


def valid_field_ranges(ticket_data):
    return list(chain.from_iterable(ticket_data["fields"].values()))


def ticket_scanning_error_rate(ticket_data):
    valid_ranges = valid_field_ranges(ticket_data)
    return sum(
        value
        for value in chain.from_iterable(ticket_data["nearby tickets"])
        if not any(value_in_range(value, r) for r in valid_ranges)
    )


def is_valid_ticket(ticket, valid_ranges):
    return all(any(value_in_range(value, r) for r in valid_ranges) for value in ticket)


def valid_tickets(ticket_data):
    valid_ranges = valid_field_ranges(ticket_data)
    return [
        ticket
        for ticket in ticket_data["nearby tickets"]
        if is_valid_ticket(ticket, valid_ranges)
    ]


def field_candidates(ticket_data):
    if not is_valid_ticket(ticket_data["my ticket"], valid_field_ranges(ticket_data)):
        raise ValueError("You don't have a valid ticket.")

    tickets = valid_tickets(ticket_data) + [ticket_data["my ticket"]]
    ticket_fields = list(map(set, zip(*tickets)))

    if len(ticket_fields) != len(ticket_data["fields"]):
        return ValueError(
            "Different number of fields and ticket fields: %s != %s"
            % (len(ticket_fields["fields"]), len(ticket_fields))
        )

    fields = {
        name: set().union(*(range(l, u + 1) for l, u in ranges))
        for name, ranges in ticket_data["fields"].items()
    }

    return [
        [i, {name for name, rng in fields.items() if ticket_field.issubset(rng)}]
        for i, ticket_field in enumerate(ticket_fields)
    ]


def match_fields(ticket_data):
    candidates = sorted(field_candidates(ticket_data), key=lambda t: len(t[1]))

    for i, (_, candidate_set) in enumerate(candidates):
        for _, other_candidate_set in candidates[i + 1 :]:
            other_candidate_set -= candidate_set

    if any(len(candidate_set) > 1 for _, candidate_set in candidates):
        raise ValueError("Ambiguous data.")

    return [candidate_set.pop() for _, candidate_set in sorted(candidates)]


def solution_01(path="input.data"):
    return ticket_scanning_error_rate(read_data(path))


def prod(iterable):
    return reduce(int.__mul__, iterable, 1)


def solution_02(path="input.data"):
    ticket_data = read_data(path)
    fields = match_fields(ticket_data)
    return prod(
        value
        for field, value in zip(fields, ticket_data["my ticket"])
        if field.startswith("departure")
    )


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
