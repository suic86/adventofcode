from collections import deque


def parse_data(path="input.txt"):
    with open(path) as fobj:
        return str.strip(fobj.read())


def find_marker(buffer, chunk_size=4):
    chunk = deque(buffer[:chunk_size], maxlen=chunk_size)

    for marker_index, char in enumerate(buffer[chunk_size:], chunk_size):
        if len(set(chunk)) == chunk_size:
            return marker_index
        chunk.append(char)
    raise ValueError("Invalid message: missing start marker.")


def solution_01(path="input.data"):
    return find_marker(parse_data(path))


def solution_02(path="input.data"):
    return find_marker(parse_data(path), chunk_size=14)


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
