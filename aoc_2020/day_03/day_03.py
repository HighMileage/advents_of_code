import csv
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield value[0]


def main(file_path, run, rise):

    x = 0
    trees_hit = 0

    for i, line in enumerate(inputs(file_path)):
        if i % rise != 0:
            continue

        if line[x % len(line)] == "#":
            trees += 1
        x += run

    print(
        f"With a run of {run} and rise of {rise}, looks like you'd hit {sum(trees)} trees"
    )
    return sum(trees)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 2: XXX --------------------- \n")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for slope in slopes:
        run, rise = slope
        total = total * main(input_file, run, rise)
    print(f"\nTotal tree count is lookin' like: {total}")
