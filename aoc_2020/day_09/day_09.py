"""Day 9"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)
    for i in data:
        print(i)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 8: XXX --------------------- \n")
    main(input_file)
