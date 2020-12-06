import csv
import sys
import math
from collections import namedtuple


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    boarding_passes = sorted(seat_information(file_path), key=lambda s: s.id)
    last_pass = boarding_passes[-1]
    print(
        f"Max id from all boarding passes: {last_pass.row} {last_pass.column} ----> {last_pass.id}"
    )

    for i in range(boarding_passes[0].id, last_pass.id + 1):
        if i == 0:
            continue
        if i not in [boarding_pass.id for boarding_pass in boarding_passes]:
            print(f"Seat ID: {i} not found")
            break


def seat_information(file_path):
    for line in inputs(file_path):
        seat_range = list(range(0, 128))
        column_range = list(range(0, 8))
        row = None

        Seat = namedtuple("Seat", ["boarding_pass", "row", "column", "id"])
        for i, command in enumerate(line):
            if i < 7:
                seat_range = pick_partition(seat_range, command)
            if i == 7:
                row = seat_range[0]
            if i >= 7:
                column_range = pick_partition(column_range, command)

        row = seat_range[0]
        column = column_range[0]
        yield Seat(line, row, column, row * 8 + column)

    # print(f"Your seat is Row {row}, Column {column}")


def pick_partition(input_range, instruction):
    front, back = split(input_range)
    if instruction in ("F", "L"):
        return front
    else:
        return back


def split(array):
    # What to do with odd numbers?
    half = math.floor(len(array) / 2)
    return (array[0:half], array[half:])


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 5: Binary Boarding --------------------- \n")
    main(input_file)
