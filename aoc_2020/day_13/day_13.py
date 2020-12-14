"""Day 13"""
from aocd.models import Puzzle
from collections import Counter
import itertools
import io
import os
import sys
import math
from collections import namedtuple

DAY = int(os.path.splitext(os.path.basename(__file__))[0].split("_")[1])
Vector = namedtuple("Vector", "x y")


def process_data(input_data):
    return list(input_data)


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
    ready_at = int(d[0])
    cadences = [
        int(interval) for interval in sorted(d[1].split(",")) if interval != "x"
    ]

    wait_times = []
    print(ready_at)
    print(cadences)
    for cadence in cadences:
        meow = math.floor(ready_at / cadence)
        print(meow)
        time_to_wait = ((meow + 1) * cadence) - ready_at
        print("FOUND", time_to_wait)
        wait_times.append((cadence, time_to_wait))

    wait_times = sorted(wait_times, key=lambda x: x[1])
    print(f"Shortest wait time is: {wait_times[0][1]}")
    print(f"Solution is {wait_times[0][0]*wait_times[0][1]}")


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
