"""Day 13"""
from aocd.models import Puzzle
from collections import Counter
import itertools
import io
import os
import sys
from collections import namedtuple

DAY = int(os.path.splitext(os.path.basename(__file__))[0].split("_")[1])
Vector = namedtuple("Vector", "x y")


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
    for i in d:
        print(i)


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
