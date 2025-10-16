from itertools import count, islice


def read_data(path="input.data"):
    with open(path) as fobj:
        timestamp, buses = map(str.rstrip, fobj)
    return int(timestamp), [
        (offset, int(bus)) for offset, bus in enumerate(buses.split(",")) if bus != "x"
    ]


def time_difference(bus, time_stamp):
    return (bus - time_stamp % bus) % bus


def solution_01(path="input.data"):
    timestamp, buses = read_data(path)
    waittime, bus = min((time_difference(bus, timestamp), bus) for _, bus in buses)
    return waittime * bus


def solution_02(path="input.data"):
    # TODO: Refactor, document and optimize (for the last bus only the *first* value is needed)
    _, buses = read_data(path)
    first = buses[0][1]
    second = first + first
    for bus_list_index, bus in buses[1:]:
        # find the first and second timestamp at which the next bus leaves *n* minutes after the previous
        # where *n* is the difference between list indices of the next and the previous bus
        first, second = islice(
            (
                i
                for i in count(first, second - first)
                if (i % bus) == bus - (bus_list_index % bus)
            ),
            2,
        )
    return first


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
