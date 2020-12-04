import csv
import sys


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

    valid_passports = [passport for passport in passports if valid(passport)]
    invalid_passports = [passport for passport in passports if not valid(passport)]

    print(f"Found {len(valid_passports)} valid passports!")
    print(f"Found {len(invalid_passports)} invalid passports!")


def valid(passport):
    valid_passport_attrs = {
        "byr",
        "ecl",
        "eyr",
        "hcl",
        "hgt",
        "iyr",
        "pid",
    }

    valid_northpole_attrs = {
        "byr",
        "cid",
        "ecl",
        "eyr",
        "hcl",
        "hgt",
        "iyr",
        "pid",
    }

    return all(k in passport.keys() for k in valid_passport_attrs)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 4: XXX --------------------- \n")
    main(input_file)
