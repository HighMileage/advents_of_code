"""Day 12"""
from aocd.models import Puzzle
from collections import Counter
import itertools
import io
import os
import sys
from collections import namedtuple

DAY = int(os.path.splitext(os.path.basename(__file__))[0].split("_")[1])


def process_data(input_data):
    data = []
    for instruct in input_data:
        action = instruct[0]
        units = int(instruct[1:])
        data.append((action, units))

    return data


def get_data(filepath=None):

    data = []
    if filepath:
        with open(filepath, "r") as input_file:
            for line in input_file.readlines():
                yield line.strip()
    else:
        puzzle = Puzzle(year=2020, day=DAY)
        data = io.StringIO(puzzle.input_data)

        for line in data.readlines():
            yield line.strip()


def main(data):
    d = process_data(data)

    vectors = []
    cardinal = {0: "N", 1: "E", 2: "S", 3: "W"}
    headings = {value: key for key, value in cardinal.items()}

    right_degree_conv = {90: 1, 180: 2, 270: 3}
    left_degree_conv = {90: 3, 180: 2, 270: 1}
    heading = 1

    for instruction in d:
        action, units = instruction

        if action == "F":
            vectors.append((heading, units))

        if action == "R":
            heading = (heading + right_degree_conv[units]) % 4

        if action == "L":
            heading = (heading + left_degree_conv[units]) % 4

        if action in headings.keys():
            direction = headings[action]
            vectors.append((direction, units))

    NS = 0
    EW = 0
    for d, u in [(cardinal[k], unit) for k, unit in vectors]:
        print(d, u)
        if d in ("S", "N"):
            NS += u * (-1 if d == "S" else 1)

        if d in ("E", "W"):
            EW += u * (-1 if d == "W" else 1)

    print(NS, EW)


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
