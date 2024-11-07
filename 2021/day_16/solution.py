from dataclasses import dataclass, field
from enum import IntEnum
from io import StringIO
from itertools import count
from math import prod
from typing import Generator

VERSION_CHUNK_LENGTH = 3
TYPE_CHUNK_LENGTH = 3


class LengthType(IntEnum):
    TOTAL_LENGTH = 0
    SUBPACK_COUNT = 1


class OpType(IntEnum):
    SUM = 0
    MUL = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


@dataclass
class Packet:
    version: int
    optype: OpType
    value: int | None = None
    subpackets: list["Packet"] = field(default_factory=lambda: [])


def create_stream(data: str) -> StringIO:
    return StringIO("".join(bin(int(c, 16))[2:].zfill(4) for c in data))


def try_read_int(stream: StringIO, length: int) -> tuple[int, bool]:
    r = stream.read(length)
    return (0 if not r else int(r, 2)), len(r) == length


def parse_packets(stream: StringIO, n: int = -1) -> Generator[Packet, None, None]:
    for _ in count(0) if n < 1 else range(n):
        version, ok = try_read_int(stream, VERSION_CHUNK_LENGTH)
        if not ok:
            break

        ptype, ok = try_read_int(stream, TYPE_CHUNK_LENGTH)
        if not ok:
            break

        if ptype == OpType.LITERAL:
            value = []
            while True:
                end, bit = stream.read(1), stream.read(4)
                if end == "1":
                    value.append(bit)
                elif end == "0":
                    value.append(bit)
                    yield Packet(version, OpType(ptype), int("".join(value), 2))
                    break
                else:
                    raise ValueError(f"Invalid bit: {end + bit}")
        else:
            length_type, ok = try_read_int(stream, 1)
            if not ok:
                break
            if length_type == LengthType.TOTAL_LENGTH:
                sp_length, ok = try_read_int(stream, 15)
                if not ok:
                    break
                yield Packet(
                    version,
                    OpType(ptype),
                    subpackets=list(parse_packets(StringIO(stream.read(sp_length)))),
                )
            elif length_type == LengthType.SUBPACK_COUNT:
                sp_cnt, ok = try_read_int(stream, 11)
                if not ok:
                    break
                yield Packet(
                    version,
                    OpType(ptype),
                    subpackets=list(parse_packets(stream, n=sp_cnt)),
                )
            else:
                raise ValueError(f"Invalid length type bit {length_type}.")


def version_sum(packet: Packet) -> int:
    if not packet.subpackets:
        return packet.version
    return packet.version + sum(version_sum(sp) for sp in packet.subpackets)


def eval_packet(packet: Packet) -> int:
    match packet.optype:
        case OpType.LITERAL:
            if packet.value is None:
                raise ValueError("Invalid literal packet.")
            return packet.value
        case OpType.SUM | OpType.MUL | OpType.MAX | OpType.MIN:
            subpacket_values = map(eval_packet, packet.subpackets)
            match packet.optype:
                case OpType.SUM:
                    return sum(subpacket_values)
                case OpType.MUL:
                    return prod(subpacket_values)
                case OpType.MAX:
                    return max(subpacket_values)
                case OpType.MIN:
                    return min(subpacket_values)
        case OpType.GT | OpType.LT | OpType.EQ:
            if len(packet.subpackets) != 2:
                raise ValueError(
                    f"Invalid number of subpacket for binary operation: {len(packet.subpackets)}"
                )
            p1 = eval_packet(packet.subpackets[0])
            p2 = eval_packet(packet.subpackets[1])
            match packet.optype:
                case OpType.LT:
                    return p1 < p2
                case OpType.GT:
                    return p1 > p2
                case OpType.EQ:
                    return p1 == p2
        case _:
            raise ValueError(f"Invalid operation: {packet.ptype}")


def solution_01(path: str = "input.data") -> int:
    with open(path) as fobj:
        return sum(map(version_sum, parse_packets(create_stream(fobj.read()))))


def solution_02(path: str = "input.data") -> int:
    with open(path) as fobj:
        return next(map(eval_packet, parse_packets(create_stream(fobj.read()))))


if __name__ == "__main__":
    print(f"Solution 01: {solution_01()}")
    print(f"Solution 02: {solution_02()}")
