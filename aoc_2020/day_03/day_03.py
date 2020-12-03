import csv
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield value[0]


def main(file_path):

    x = 0
    trees = []
    rows = len(list(inputs(file_path)))
    expanded_size = rows * 3
    print(expanded_size)
    for i, line in enumerate(inputs(file_path)):
        limit = len(line)
        multiplier = int(expanded_size * limit)
        l = line * multiplier

        if l[x] == "#":
            trees.append(1)
        x += 3

    print(f"Looks like you'd hit {sum(trees)} trees")


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 2: XXX --------------------- \n")
    main(input_file)
