import pytest

from solution import (
    OpType,
    Packet,
    create_stream,
    eval_packet,
    parse_packets,
    solution_01,
    version_sum,
)


def test_parse_single_literal_packet() -> None:
    assert next(parse_packets(create_stream("D2FE28"))) == Packet(
        6, OpType.LITERAL, 2021
    )


def test_parse_single_operator_packet_length_type_0() -> None:
    assert next(parse_packets(create_stream("38006F45291200"))) == Packet(
        version=1,
        optype=OpType.LT,
        subpackets=[
            Packet(version=6, optype=OpType.LITERAL, value=10),
            Packet(version=2, optype=OpType.LITERAL, value=20),
        ],
    )


def test_parse_single_operator_packet_length_type_1() -> None:
    assert next(parse_packets(create_stream("EE00D40C823060"))) == Packet(
        version=7,
        optype=OpType.MAX,
        subpackets=[
            Packet(version=2, optype=OpType.LITERAL, value=1),
            Packet(version=4, optype=OpType.LITERAL, value=2),
            Packet(version=1, optype=OpType.LITERAL, value=3),
        ],
    )


@pytest.mark.parametrize(
    "stream,expected_sum",
    [
        ("620080001611562C8802118E34", 12),
        ("8A004A801A8002F478", 16),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_version_sum(stream: str, expected_sum: int) -> None:
    assert sum(map(version_sum, parse_packets(create_stream(stream)))) == expected_sum


@pytest.mark.parametrize(
    "data,value",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_eval_packet(data, value) -> None:
    assert next(map(eval_packet, parse_packets(create_stream(data)))) == value


def test_solution_01() -> None:
    assert solution_01() == 925
