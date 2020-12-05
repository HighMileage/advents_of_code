import csv
import sys
import re
from collections import namedtuple


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = list(inputs(file_path))
    batch = ""
    entries = []
    for i, line in enumerate(data):
        batch = batch + " " + line
        if i + 1 < len(data) and data[i + 1] == "":
            entries.append(batch)
            batch = ""
        if i + 1 == len(data):
            entries.append(batch)

    passports = []
    for entry in entries:
        attributes = entry.strip().split(" ")
        meow = {}
        for i in attributes:
            k, v = i.split(":")
            meow[k] = v
        passports.append(meow)

    valid_passports = [
        passport for passport in passports if valid(passport) and present(passport)
    ]
    invalid_passports = [
        passport
        for passport in passports
        if (not valid(passport)) and present(passport)
    ]

    test = {
        "byr": "1950",
        "ecl": "hzl",
        "eyr": "2030",
        "hcl": "#623a2f",
        "pid": "742249321",
        "hgt": "158cm",
        "iyr": "2018",
    }

    print(f"Found {len(valid_passports)} valid passports!")
    print(f"Found {len(invalid_passports)} invalid passports!")


def present(passport):
    valid_passport_attrs = {
        "byr",
        "ecl",
        "eyr",
        "hcl",
        "hgt",
        "iyr",
        "pid",
    }

    return all(k in passport.keys() for k in valid_passport_attrs)


def _valid(passport):
    birth_year = int(passport.get("byr") or 0)
    issue_year = int(passport.get("iyr") or 0)
    exp_year = int(passport.get("eyr") or 0)
    height = passport.get("hgt") or ""
    eyecolor = passport.get("ecl") or ""
    pid = passport.get("pid") or ""
    hair_color = passport.get("hcl") or ""

    Validity = namedtuple(
        "validity",
        [
            "birth_year",
            "issue_year",
            "expr_year",
            "eye_color",
            "height",
            "pid",
            "hair_color",
        ],
    )
    return Validity(
        birth_year >= 1920 and birth_year <= 2002,
        issue_year >= 2010 and issue_year <= 2020,
        exp_year >= 2020 and exp_year <= 2030,
        eyecolor in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        valid_height(height),
        valid_passport_id(pid),
        valid_hair_color(hair_color),
    )


def valid(passport):

    return all(_valid(passport))


def valid_hair_color(color):
    return bool(re.match("^#[a-f0-9]{6}$", color))


def valid_passport_id(pid):
    if len(pid) != 9:
        return False
    if pid.isdigit():
        return True

    return False


def valid_height(height_value):
    if height_value == "":
        return False

    if len(height_value) <= 2:
        return False

    system = height_value[-2:]
    if system not in ["cm", "in"]:
        return False

    numeric_part = int(height_value.strip("cm").strip("in"))

    if system == "cm":
        return numeric_part >= 150 and numeric_part <= 193
    if system == "in":
        return numeric_part >= 59 and numeric_part <= 76


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 4: Passport Processing ssport Processing --------------------- \n")
    main(input_file)
