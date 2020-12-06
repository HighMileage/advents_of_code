"""Day 6"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    for line in inputs(file_path):
        print(line)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 6: Custom Customs --------------------- \n")
    main(input_file)
