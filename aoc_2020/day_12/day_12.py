"""Day 12"""
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


def vector_translation(degrees, v):
    if degrees in (-90, 270):
        return Vector(-v.y, v.x)

    if degrees in (180, -180):
        return Vector(-v.x, -v.y)

    if degrees in (90, -270):
        return Vector(v.y, -v.x)


def main(data):
    d = process_data(data)

    vectors = []
    cardinal = {0: "N", 1: "E", 2: "S", 3: "W"}
    headings = {value: key for key, value in cardinal.items()}

    right_degree_conv = {90: 1, 180: 2, 270: 3}
    left_degree_conv = {90: 3, 180: 2, 270: 1}
    heading = 1
    waypoint = Vector(10, 1)

    for instruction in d:
        print(waypoint)
        action, units = instruction

        if action == "F":
            new_x = (units) * waypoint.x
            new_y = (units) * waypoint.y
            waypoints = Vector(new_x + waypoint.x, new_y + waypoint.y)
            vectors.append((new_x, new_y))

        if action in ("L", "R"):
            degrees = units * (-1 if action == "L" else 1)
            waypoint = vector_translation(degrees, waypoint)

        if action in ("N", "S"):
            sign = -1 if action == "S" else 1
            waypoint = Vector(waypoint.x, waypoint.y + units * sign)

        if action in ("E", "W"):
            sign = -1 if action == "W" else 1
            waypoint = Vector(waypoint.x + units * sign, waypoint.y)

    ns = 0
    ew = 0

    for vector in vectors:
        east_west, north_south = vector
        ns += north_south
        ew += east_west

    print(f"Total distance is {abs(ew) + abs(ns)}")


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
