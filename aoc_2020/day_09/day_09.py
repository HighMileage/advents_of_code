"""Day 9"""
import sys
import itertools


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [int(line.strip()) for line in lines]


-def find_no_sum_element(file_path):
    data = inputs(file_path)
    for i, row in enumerate(data):
        if i <= 24:
            continue

        sum_pair = False
        for pair in itertools.combinations(data[i - 25 : i], 2):
            first, second = (int(i) for i in pair)
            if (previous_sum := first + second) == row:
                sum_pair = True
                break

        if not sum_pair:
            print("Weird couldn't find a sum for {:,}".format(row))
            return row


def scan_for_contiguous_matches(file_path, number):
    data = inputs(file_path)

    for group_size in range(2, 20):
        print(
            "Looking for a contiguous group of size {} whose elements sum to {:,}".format(
                group_size, number
            )
        )

        for offset, row in enumerate(data):
            if len(data) - 1 == group_size + offset:
                break

            group = sorted([data[i] for i in range(0 + offset, group_size + offset)])

            if sum(group) == number:
                print(
                    f"\tFounding matching group with {group_size} elements: {group}",
                )
                print(
                    f"\tSum of highest ({group[1]}) and lowest ({group[0]}) elements is {group[0] + group[-1]}"
                )
                return


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 9: Encoding Error --------------------- \n")
    number = find_no_sum_element(input_file)
    scan_for_contiguous_matches(input_file, number)
