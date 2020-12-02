import csv
import sys

def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield int(value[0])

def main(file_path):
    for x in inputs(file_path):
        print(x)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 2: XXXXX --------------------- \n")
    main(input_file)
