"""Day 7"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)

    for i, line in enumerate(data):
        if line == "":
            continue

        print(line)


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 6: XXX --------------------- \n")
    main(input_file)
