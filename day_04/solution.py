#!/usr/bin/env python3
import re

FIELD_KEYS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}


def read_passport_data(path="input.data"):
    with open(path) as fobj:
        passport = []
        for row in fobj:
            row = row.rstrip()
            if not row:
                yield " ".join(passport)
                passport = []
            passport.append(row)
        if passport:
            yield " ".join(passport)


def value_in_range(value, lower, upper):
    try:
        value = int(value)
    except ValueError:
        return False
    return lower <= value <= upper


def is_byr_valid(year):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    return value_in_range(year, 1920, 2002)


def is_iyr_valid(year):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    return value_in_range(year, 2010, 2020)


def is_eyr_valid(year):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    return value_in_range(year, 2020, 2030)


def is_hgt_valid(height):
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    m = re.match(r"(\d+)(in|cm)", height)
    if m is None:
        return False

    value, unit = m.groups()
    if unit == "cm":
        return value_in_range(value, 150, 193)
    elif unit == "in":
        return value_in_range(value, 59, 76)
    return False


def is_hcl_valid(hair_color):
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
    return bool(re.match("^#[0-9a-f]{6}$", hair_color))


def is_ecl_valid(eye_color):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    return eye_color in "amb blu brn gry grn hzl oth".split()


def is_pid_valid(passport_id):
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    return bool(re.match("^[0-9]{9}$", passport_id))


def is_cid_valid(country_id):
    """cid (Country ID) - ignored, missing or not."""
    return True


def parse_passport_data(passport_data):
    return dict(field.split(":") for field in passport_data.split())


def is_passport_data_valid(passport_data):
    missing_keys = FIELD_KEYS - set(parse_passport_data(passport_data))
    if not missing_keys:
        return True
    elif len(missing_keys) == 1 and missing_keys.pop() == "cid":
        return True
    return False


def is_passport_valid(passport_data):
    if not is_passport_data_valid(passport_data):
        return False
    validation_map = {
        "byr": is_byr_valid,
        "iyr": is_iyr_valid,
        "eyr": is_eyr_valid,
        "hgt": is_hgt_valid,
        "hcl": is_hcl_valid,
        "ecl": is_ecl_valid,
        "pid": is_pid_valid,
        "cid": is_cid_valid,
    }
    passport = parse_passport_data(passport_data)
    return all(validation_map[key](value) for key, value in passport.items())


def solution_01(path="input.data"):
    return sum(map(is_passport_data_valid, read_passport_data(path)))


def solution_02(path="input.data"):
    return sum(map(is_passport_valid, read_passport_data(path)))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
