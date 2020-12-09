"""Day 9"""
import sys
import itertools


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)
    for i, row in enumerate(data):
        if i <= 24:
            print(f"Premable -- skipping")
            continue

        current_value = int(row)

        sum_pair = False
        for pair in itertools.combinations(data[i - 25 : i], 2):
            first, second = (int(i) for i in pair)
            if (previous_sum := first + second) == current_value:
                sum_pair = True
                break
                # print(f"Found um {first} and {second}")

        if not sum_pair:
            print(f"Weird couldn't find a sum for {current_value}")
            break


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 8: XXX --------------------- \n")
    main(input_file)
