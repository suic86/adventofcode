from functools import cache
from hashlib import md5
from itertools import count, islice

from hashes import FIRST_PART, SECOND_PART

DOORID = "reyedfim"


@cache
def hashes(door_id: str = DOORID, length: int = 8, use_cache=False) -> list[str]:
    if use_cache and door_id == door_id and length == 8:
        return FIRST_PART
    return list(
        islice(
            (
                digest
                for i in count()
                if (
                    digest := md5(f"{door_id}{i}".encode("utf-8")).hexdigest()
                ).startswith("00000")
            ),
            length,
        )
    )


@cache
def cinematic_hashes(
    door_id: str = DOORID, length: int = 8, use_cache=False
) -> list[str]:
    if use_cache and door_id == door_id and length == 8:
        return SECOND_PART

    digits = set("01234567")
    hashes = []
    for i in count():
        digest = md5(f"{door_id}{i}".encode("utf-8")).hexdigest()
        if digest.startswith("00000"):
            if (index := digest[5]) in digits:
                hashes.append(digest)
                digits.remove(index)
            if not digits:
                break
    return hashes


def solution_01(use_cache=False):
    return "".join(h[5] for h in hashes(use_cache=use_cache))


def solution_02(use_cache=False):
    buffer = [""] * 8

    for h in cinematic_hashes(use_cache=use_cache):
        p, v = h[5:7]
        buffer[int(p)] = v
    return "".join(buffer)


if __name__ == "__main__":
    from sys import argv

    use_cache = len(argv) == 2 and argv[1] == "cached"
    print(f"Solution 01: {solution_01(use_cache=use_cache)}")
    print(f"Solution 02: {solution_02(use_cache=use_cache)}")
