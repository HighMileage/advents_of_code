import csv
import itertools
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield int(value[0])


def main(file_path):
    for pair in itertools.combinations(inputs(file_path), 2):
        value_1, value_2 = pair
        if value_1 + value_2 == 2020:
            print(f"Part one solution: {value_1 * value_2}")
            break

    for triplet in itertools.combinations(inputs(file_path), 3):
        value_1, value_2, value_3 = triplet
        if value_1 + value_2 + value_3 == 2020:
            print(f"Part two solution: {value_1 * value_2 * value_3}")
            break


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 1: Report Repair --------------------- \n")
    main(input_file)
